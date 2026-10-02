"""جاروی دوره‌ای ردیف‌های pending (مرحلهٔ ۶) — ADR-0010.

- هر notify.retry_interval ردیف‌های pendingِ سررسیدشده قدیمی‌ترین اول
  ارسال می‌شوند؛ سقف sweep_max_sends پیام در هر دور به‌ازای هر کانال
  (مازاد به سویپ بعدی می‌رود)
- فاصلهٔ ~۱ ثانیه بین پیام‌های تلگرام و ~۲ ثانیه ایمیل؛ کانال‌ها
  مستقل و موازی پیش می‌روند (خطای یکی مانع دیگری نیست)
- علامت sent فقط بعد از موفقیت؛ خطا سه دسته می‌شود:
  گذرا → سویپ بعدی، قابل‌احیا → next_attempt_at با backoff نمایی تا
  سقف ۲۴ ساعت، ابدی → dead (ADR-0010 اصلاح ۲۰۲۶-۰۹-۱۸)
"""

import asyncio
import datetime
from dataclasses import dataclass, field

from top_divar.notify.errors import ETERNAL, RESURRECTABLE, SendError
from top_divar.notify.message import (
    build_email_body,
    build_email_subject,
    build_telegram_message,
)
from top_divar.notify.planner import resolve_search_label
from top_divar.notify.settings import NotifySettings
from top_divar.shared.logging import get_logger
from top_divar.storage.timestamps import utc_now

_log = get_logger("notify.sweep")

BACKOFF_CAP_SECONDS = 24.0 * 3600.0
DEFAULT_CHANNEL_PAUSES = {"telegram": 1.0, "email": 2.0}


def compute_backoff_seconds(attempts: int, base_seconds: float) -> float:
    """backoff نمایی ردیف‌محور: base × 2^(n−1) با سقف ۲۴ ساعت (attempts ≥ ۱)."""
    exponent = max(int(attempts) - 1, 0)
    return min(max(base_seconds, 0.0) * (2**exponent), BACKOFF_CAP_SECONDS)


@dataclass
class ChannelSweepResult:
    channel: str
    attempted: int = 0
    sent: int = 0
    transient: int = 0
    resurrectable: int = 0
    dead: int = 0


@dataclass
class SweepOutcome:
    channels: list = field(default_factory=list)


def telegram_sender(notifier):
    """پیچیدن TelegramNotifier به شکل (ad, recipient, label) → SendError."""

    async def _send(ad: dict, recipient: str, label: str) -> None:
        await notifier.send_message(recipient, build_telegram_message(ad, label))

    return _send


def email_sender(notifier):
    """پیچیدن EmailNotifier به شکل (ad, recipient, label) → SendError."""

    async def _send(ad: dict, recipient: str, label: str) -> None:
        await notifier.send_message(
            recipient, build_email_subject(ad), build_email_body(ad, label)
        )

    return _send


class DeliverySweeper:
    """ارسال دوره‌ای ردیف‌های pending هر کانال با سقف و فاصلهٔ مجاز."""

    def __init__(
        self,
        repository,
        senders: dict,
        settings: NotifySettings,
        *,
        searches_by_id: dict = None,
        pauses: dict = None,
        sleeper=None,
        clock=None,
    ):
        self._repository = repository
        self._senders = dict(senders)
        self._settings = settings
        self._searches_by_id = searches_by_id or {}
        self._pauses = dict(DEFAULT_CHANNEL_PAUSES)
        if pauses:
            self._pauses.update(pauses)
        self._sleeper = sleeper or asyncio.sleep
        self._clock = clock or utc_now
        self._lock = asyncio.Lock()

    async def sweep_once(self) -> SweepOutcome:
        """یک دور جارو؛ اگر دور دیگری مشغول است بی‌کار برمی‌گردد."""
        if self._lock.locked():
            return SweepOutcome()
        async with self._lock:
            outcome = SweepOutcome()
            results = await asyncio.gather(
                *(
                    self._sweep_channel(channel)
                    for channel in sorted(self._senders)
                )
            )
            outcome.channels = list(results)
        for result in outcome.channels:
            if result.attempted:
                _log.info(
                    "دور جاروی تحویل کانال «%s» تمام شد.",
                    result.channel,
                    extra={
                        "fields": {
                            "event": "delivery_sweep_finished",
                            "channel": result.channel,
                            **{
                                key: getattr(result, key)
                                for key in (
                                    "attempted",
                                    "sent",
                                    "transient",
                                    "resurrectable",
                                    "dead",
                                )
                            },
                        }
                    },
                )
        return outcome

    async def backfill_recipient(
        self, channel: str, recipient: str, *, since=None
    ) -> ChannelSweepResult:
        """جبران تعاملی: pendingهای یک گیرنده، فوری و قدیمی‌ترین اول (G5).

        بی‌تاب به next_attempt_at (تعامل کاربر = ارسال فوری)؛ ردیف‌های
        dead برنمی‌گردند. همان قفل جارو را می‌گیرد تا با سویپ تداخل نکند.
        """
        result = ChannelSweepResult(channel=channel)
        if channel not in self._senders:
            return result
        if self._lock.locked():
            return result
        async with self._lock:
            rows = await self._repository.get_pending_deliveries(
                channel=channel, recipient=recipient, since=since
            )
            return await self._deliver_rows(channel, rows)

    def apply_config(
        self,
        settings: NotifySettings,
        searches_by_id: dict,
        *,
        senders: dict = None,
    ) -> None:
        """به‌روزرسانی زندهٔ تنظیمات بعد از SIGHUP (مرحلهٔ ۷ — ADR-0011)."""
        self._settings = settings
        self._searches_by_id = dict(searches_by_id or {})
        if senders is not None:
            self._senders = dict(senders)

    async def _sweep_channel(self, channel: str) -> ChannelSweepResult:
        send = self._senders[channel]
        result = ChannelSweepResult(channel=channel)
        rows = await self._repository.get_due_deliveries(
            channel=channel, limit=self._settings.sweep_max_sends
        )
        return await self._deliver_rows(channel, rows, result=result)

    async def _deliver_rows(
        self,
        channel: str,
        rows: list,
        *,
        result: ChannelSweepResult = None,
    ) -> ChannelSweepResult:
        """ارسال ردیف‌های تحویل با علامت‌گذاری و فاصلهٔ مجاز کانال."""
        result = result or ChannelSweepResult(channel=channel)
        labels = {}
        for index, row in enumerate(rows):
            delivery, ad = row["delivery"], row["ad"]
            result.attempted += 1
            if ad["id"] not in labels:
                labels[ad["id"]] = await resolve_search_label(
                    self._repository, self._searches_by_id, ad["id"]
                )
            label = labels[ad["id"]]
            try:
                await self._senders[channel](ad, delivery["recipient"], label)
            except SendError as exc:
                await self._mark_failure(delivery, exc, result)
            else:
                await self._repository.mark_delivery(delivery["id"], "sent")
                result.sent += 1
                _log.info(
                    "پیام به %s:%s ارسال شد.",
                    channel,
                    delivery["recipient"],
                    extra={
                        "fields": {
                            "event": "delivery_sent",
                            "channel": channel,
                            "recipient": delivery["recipient"],
                            "ad_id": delivery["ad_id"],
                        }
                    },
                )
            if index + 1 < len(rows):
                await self._sleeper(self._pauses.get(channel, 1.0))
        return result

    async def _mark_failure(
        self, delivery: dict, exc: SendError, result: ChannelSweepResult
    ) -> None:
        if exc.category == ETERNAL:
            await self._repository.mark_delivery(
                delivery["id"], "dead", error=str(exc)
            )
            result.dead += 1
            _log.error(
                "خطای ابدی تحویل — ردیف dead شد: %s",
                exc,
                extra={
                    "fields": {
                        "event": "delivery_dead",
                        "channel": delivery["channel"],
                        "recipient": delivery["recipient"],
                        "ad_id": delivery["ad_id"],
                        "error": str(exc),
                    }
                },
            )
            return
        if exc.category == RESURRECTABLE:
            delay = compute_backoff_seconds(
                delivery["attempts"] + 1, self._settings.retry_interval
            )
            if exc.retry_after is not None:
                delay = min(max(delay, float(exc.retry_after)), BACKOFF_CAP_SECONDS)
            next_attempt = self._clock() + datetime.timedelta(seconds=delay)
            await self._repository.mark_delivery(
                delivery["id"], "pending", error=str(exc), next_attempt_at=next_attempt
            )
            result.resurrectable += 1
            _log.warning(
                "خطای قابل‌احیا — تلاش بعدی %s ثانیه دیگر: %s",
                delay,
                exc,
                extra={
                    "fields": {
                        "event": "delivery_backoff",
                        "channel": delivery["channel"],
                        "recipient": delivery["recipient"],
                        "ad_id": delivery["ad_id"],
                        "next_attempt_in_seconds": delay,
                        "error": str(exc),
                    }
                },
            )
            return
        await self._repository.mark_delivery(
            delivery["id"], "pending", error=str(exc)
        )
        result.transient += 1
        _log.warning(
            "خطای گذرای ارسال — تلاش در سویپ بعدی: %s",
            exc,
            extra={
                "fields": {
                    "event": "delivery_transient_error",
                    "channel": delivery["channel"],
                    "recipient": delivery["recipient"],
                    "ad_id": delivery["ad_id"],
                    "error": str(exc),
                }
            },
        )

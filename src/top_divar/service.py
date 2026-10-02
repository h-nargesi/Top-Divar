"""اجرا و پایداری سرویس (مرحلهٔ ۷) — ADR-0003/0011/0012.

یک حلقهٔ رویداد asyncio با چهار تسک مستقل روی همان حلقه:

| تسک | کار |
|---|---|
| scheduler | poll جستجوها + صف درخواست‌های دیوار (concurrency = ۱) |
| bot-gateway | long-polling getUpdates + پاسخ دستورات + جبران تعاملی |
| sweep | ارسال دوره‌ای ردیف‌های pending (ADR-0010) |
| heartbeat | sd_notify دوره‌ای برای WatchdogSec — جدا از صف کاری |

SIGHUP کانفیگ را دوباره می‌خواند و زنده اعمال می‌کند؛ YAML خراب سرویس
را نمی‌کشد (ADR-0011). خطای متوالی دیوار و بروت‌فورس پسورد، پیام هشدار
اپراتور می‌رود (ADR-0003 — throttle ۱/۲۴h برای خطای دیوار).
"""

import asyncio
import signal
import threading

from top_divar import __version__
from top_divar.bot import BotGateway, TelegramBotClient
from top_divar.config import ConfigFileError, load_yaml_file, validate_config
from top_divar.core import PollScheduler, PollingSettings, poll_search, score_pending_ads
from top_divar.divar.fetcher import DivarFetcher
from top_divar.divar.queue import DivarRequestQueue
from top_divar.notify import (
    DeliverySweeper,
    EmailNotifier,
    NotifySettings,
    TelegramNotifier,
    email_sender,
    plan_delivery_rows,
    telegram_sender,
)
from top_divar.notify.errors import SendError
from top_divar.shared.logging import get_logger
from top_divar.systemd import heartbeat_loop, sd_notify
from top_divar.storage.timestamps import utc_now

OPS_ALERT_THROTTLE_SECONDS = 24.0 * 3600.0


class OpsAlerter:
    """پیام هشدار به chat اپراتور — حداکثر یک پیام در هر ۲۴ ساعت (ADR-0003)."""

    def __init__(self, sender, chat_id, *, throttle_seconds=OPS_ALERT_THROTTLE_SECONDS, clock=None):
        self._sender = sender  # (chat_id, text) → awaitable
        self._chat_id = chat_id
        self._throttle = float(throttle_seconds)
        self._clock = clock or utc_now
        self._last_sent = None
        self._dropped = 0

    async def send(self, text: str) -> bool:
        now = self._clock()
        if self._last_sent is not None and (now - self._last_sent).total_seconds() < self._throttle:
            self._dropped += 1
            return False
        self._last_sent = now
        try:
            await self._sender(self._chat_id, text)
        except SendError as exc:
            get_logger("service.ops").error(
                "ارسال هشدار اپراتور شکست خورد: %s",
                exc,
                extra={"fields": {"event": "ops_alert_send_failed", "error": str(exc)}},
            )
            return False
        return True


class ServiceTaskDied(Exception):
    """یک تسک اصلی سرویس به خطا افتاد — سرویس می‌ایستد تا systemd ری‌استارت کند."""


class Service:
    """مونتاژ حلقهٔ اصلی: چهار تسک مستقل + reload زندهٔ کانفیگ."""

    def __init__(
        self,
        repository,
        raw: dict,
        env: dict,
        *,
        config_path,
        env_path=None,
        log=None,
    ):
        self._repository = repository
        self._env = dict(env)
        self._config_path = config_path
        self._env_path = env_path
        self._log = log or get_logger("service")
        self._scheduler = None
        self._sweeper = None
        self._gateway = None
        self._notifier = None
        self._ops_alerter = None
        self._build_notifier_and_ops()
        self._apply_config(raw)
        self._build_gateway()
        self._scheduler = PollScheduler(
            self._searches,
            self._polling_settings,
            self._poll,
            on_paused=self._on_polling_paused,
        )

    # --- ساخت و به‌روزرسانی کانفیگ زنده -------------------------------------

    @property
    def scheduler(self):
        return self._scheduler

    @property
    def sweeper(self):
        return self._sweeper

    @property
    def gateway(self):
        return self._gateway

    def _apply_config(self, raw: dict) -> None:
        """اعمال کانفیگ (در ساخت اولیه و reload) روی همهٔ اجزا."""
        self._raw = raw
        self._polling_settings = PollingSettings.from_config(raw)
        self._notify_settings = NotifySettings.from_config(raw)
        searches = raw.get("searches") if isinstance(raw, dict) else None
        self._searches = [
            search
            for search in searches or []
            if isinstance(search, dict) and search.get("enabled", True)
        ]
        self._searches_by_id = {
            search["id"]: search
            for search in self._searches
            if isinstance(search.get("id"), str)
        }
        queue = DivarRequestQueue(
            search_min_interval=self._polling_settings.search_min_interval,
            detail_min_interval=self._polling_settings.detail_min_interval,
        )
        self._fetcher = DivarFetcher(queue=queue)
        if self._scheduler is not None:
            changed = self._scheduler.refresh(self._searches, self._polling_settings)
            self._log.info(
                "جستجوهای نوبت‌بندی به‌روز شدند.",
                extra={
                    "fields": {
                        "event": "scheduler_refreshed",
                        **changed,
                    }
                },
            )
        self._refresh_sweeper()
        if self._gateway is not None:
            self._gateway.apply_config(
                self._searches_by_id,
                backfill_days=self._notify_settings.telegram.backfill_days,
            )

    def _refresh_sweeper(self) -> None:
        """ساخت/به‌روزرسانی جارو از کانال‌های فعال — در ساخت و reload.

        روشن‌شدن کانال‌ها در SIGHUP همین‌جا جارو را می‌سازد؛ خاموشی،
        فرستنده‌هایش را خالی می‌کند.
        """
        senders = self._build_senders()
        if senders:
            if self._sweeper is None:
                self._sweeper = DeliverySweeper(
                    self._repository,
                    senders,
                    self._notify_settings,
                    searches_by_id=self._searches_by_id,
                )
            else:
                self._sweeper.apply_config(
                    self._notify_settings, self._searches_by_id, senders=senders
                )
        elif self._sweeper is not None:
            self._sweeper.apply_config(
                self._notify_settings, self._searches_by_id, senders={}
            )
        if self._gateway is not None:
            self._gateway.set_sweeper(self._sweeper)

    def _build_notifier_and_ops(self) -> None:
        """ساخت notifier تلگرام و هشدار اپراتور — فقط وابسته به env."""
        token = self._env.get("TELEGRAM_BOT_TOKEN", "")
        proxy = self._env.get("HTTPS_PROXY") or None
        ops_chat_id = self._env.get("TELEGRAM_OPS_CHAT_ID") or None

        if token:
            self._notifier = TelegramNotifier(token, proxy=proxy)
        else:
            self._log.warning(
                "TELEGRAM_BOT_TOKEN نیست — ارسال تلگرام، بات و هشدار اپراتور خاموش‌اند.",
                extra={"fields": {"event": "telegram_disabled"}},
            )
        if self._notifier is not None and ops_chat_id:
            self._ops_alerter = OpsAlerter(self._notifier.send_message, ops_chat_id)
        else:
            self._log.warning(
                "TELEGRAM_OPS_CHAT_ID نیست — پیام‌های هشدار اپراتور مقصدی ندارند.",
                extra={"fields": {"event": "ops_alert_disabled"}},
            )

    def _build_gateway(self) -> None:
        """ساخت درگاه بات (یک‌بار، فقط وابسته به env)."""
        token = self._env.get("TELEGRAM_BOT_TOKEN", "")
        proxy = self._env.get("HTTPS_PROXY") or None
        ops_chat_id = self._env.get("TELEGRAM_OPS_CHAT_ID") or None
        password = self._env.get("TELEGRAM_BOT_PASSWORD", "")
        if token and password:
            self._gateway = BotGateway(
                self._repository,
                TelegramBotClient(token, proxy=proxy),
                password=password,
                ad_sender=self._notifier.send_message if self._notifier else None,
                sweeper=self._sweeper,
                ops_chat_id=ops_chat_id,
                searches_by_id=self._searches_by_id,
                backfill_days=self._notify_settings.telegram.backfill_days,
            )
            self._log.info(
                "درگاه بات فعال است (getUpdates یعنی فقط یک نمونهٔ فعال).",
                extra={"fields": {"event": "bot_gateway_enabled"}},
            )
        else:
            self._log.info(
                "درگاه بات خاموش است — TELEGRAM_BOT_TOKEN/TELEGRAM_BOT_PASSWORD لازم است.",
                extra={"fields": {"event": "bot_gateway_disabled"}},
            )

    def _build_senders(self) -> dict:
        senders = {}
        if self._notify_settings.telegram_enabled and self._notifier is not None:
            senders["telegram"] = telegram_sender(self._notifier)
        if self._notify_settings.email_enabled:
            smtp = self._notify_settings.email.smtp
            senders["email"] = email_sender(
                EmailNotifier(smtp, self._env.get(smtp.password_env))
            )
        return senders

    def reload_config(self) -> None:
        """SIGHUP: خواندن دوبارهٔ کانفیگ؛ خراب/نامعتبر → کانفیگ قبلی می‌ماند."""
        try:
            raw = load_yaml_file(self._config_path)
        except ConfigFileError as exc:
            self._log.error(
                "بارگذاری مجدد ناموفق — کانفیگ قبلی سر جایش می‌ماند: %s",
                exc,
                extra={"fields": {"event": "config_reload_failed"}},
            )
            return
        report = validate_config(raw, self._env)
        if not report.ok:
            self._log.error(
                "کانفیگ جدید نامعتبر است — کانفیگ قبلی سر جایش می‌ماند.",
                extra={"fields": {"event": "config_reload_rejected"}},
            )
            for error in report.errors:
                self._log.error(error.message)
            return
        for warning in report.warnings:
            self._log.warning(warning.message)
        self._apply_config(raw)
        self._log.info(
            "کانفیگ با SIGHUP دوباره خوانده و زنده اعمال شد.",
            extra={
                "fields": {
                    "event": "config_reloaded",
                    "searches": len(self._searches),
                }
            },
        )

    # --- حلقهٔ اصلی ----------------------------------------------------------

    async def run(self) -> None:
        stop = asyncio.Event()
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, self._request_stop, stop)
        if hasattr(signal, "SIGHUP"):
            loop.add_signal_handler(signal.SIGHUP, self.reload_config)

        await self._log_orphan_watermarks()
        sd_notify("READY=1")
        # آشتی‌سازی startup: pendingهای باقی‌مانده از اجرای قبل امتیاز می‌گیرند
        # و ردیف‌های تحویل معلق در اولین دور جارو ارسال می‌شوند
        await self._score_pending()
        tasks = [
            asyncio.create_task(self._scheduler.run(stop), name="scheduler"),
            asyncio.create_task(self._sweep_loop(stop), name="sweep"),
            asyncio.create_task(heartbeat_loop(stop), name="heartbeat"),
        ]
        if self._gateway is not None:
            tasks.append(asyncio.create_task(self._gateway.run(stop), name="bot-gateway"))
        self._log.info(
            "سرویس راه‌اندازی شد.",
            extra={
                "fields": {
                    "event": "service_started",
                    "version": __version__,
                    "searches": len(self._searches),
                    "tasks": [task.get_name() for task in tasks],
                    "channels": list(self._build_senders()),
                    "bot_enabled": self._gateway is not None,
                }
            },
        )
        stop_waiter = asyncio.create_task(stop.wait())
        try:
            done, _ = await asyncio.wait(
                [*tasks, stop_waiter], return_when=asyncio.FIRST_COMPLETED
            )
        finally:
            stop_waiter.cancel()
            for task in tasks:
                task.cancel()
            await asyncio.gather(stop_waiter, *tasks, return_exceptions=True)
        sd_notify("STOPPING=1")
        if not stop.is_set():
            # تسکی بدون انتظار مرد؛ سرویس می‌ایستد تا systemd ری‌استارت کند
            dead = next(task for task in done if task is not stop_waiter)
            exc = dead.exception()
            self._log.error(
                "تسک «%s» از راه افتاد — سرویس می‌ایستد تا ری‌استارت شود.",
                dead.get_name(),
                extra={
                    "fields": {
                        "event": "service_task_died",
                        "task": dead.get_name(),
                        "error": str(exc) if exc else None,
                    }
                },
            )
            if exc is not None:
                raise ServiceTaskDied(dead.get_name()) from exc
            raise ServiceTaskDied(dead.get_name())

    @staticmethod
    def _request_stop(stop: asyncio.Event) -> None:
        stop.set()

    async def _sweep_loop(self, stop) -> None:
        """جاروی دوره‌ای ردیف‌های pending (ADR-0010 — هر retry_interval)."""
        while not _is_stopped(stop):
            await asyncio.sleep(self._notify_settings.retry_interval)
            await self._sweep_quietly()

    # --- خط لولهٔ poll → امتیاز → ردیف تحویل → ارسال --------------------------

    async def _poll(self, search: dict) -> None:
        try:
            await poll_search(
                self._fetcher, self._repository, search, self._polling_settings
            )
        finally:
            # اول ذخیره با وضعیت در انتظار، بعد امتیاز دسته — حتی اگر poll
            # وسط راه شکست خورد، ذخیره‌شده‌ها امتیاز می‌گیرند
            await self._score_pending()

    async def _score_pending(self) -> None:
        """مرحلهٔ دوم خط لوله: امتیازدهی دستهٔ در انتظار (مرحلهٔ ۵)."""
        try:
            await score_pending_ads(
                self._repository, self._raw, on_notable=self._plan_delivery
            )
        except Exception as exc:  # noqa: BLE001 - شکست این دور کشنده نیست
            self._log.error(
                "امتیازدهی دسته شکست خورد؛ در دور بعد دوباره تلاش می‌شود: %s",
                exc,
                extra={"fields": {"event": "scoring_batch_failed"}},
            )
        await self._sweep_quietly()

    async def _plan_delivery(self, row: dict) -> None:
        """ردیف‌های delivery قبل از ارسال (ADR-0010)."""
        try:
            await plan_delivery_rows(
                self._repository, self._notify_settings, row["id"]
            )
        except Exception as exc:  # noqa: BLE001 - شکست برنامه‌ریزی دور بعد جبران نمی‌شود
            self._log.error(
                "ساخت ردیف تحویل برای آگهی %s شکست خورد: %s",
                row.get("token"),
                exc,
                extra={
                    "fields": {
                        "event": "delivery_planning_failed",
                        "token": row.get("token"),
                    }
                },
            )

    async def _sweep_quietly(self) -> None:
        if self._sweeper is None:
            return
        try:
            await self._sweeper.sweep_once()
        except Exception as exc:  # noqa: BLE001 - جارو نباید سرویس را بخواباند
            self._log.error(
                "دور جاروی تحویل شکست خورد: %s",
                exc,
                extra={"fields": {"event": "delivery_sweep_failed"}},
            )

    async def _on_polling_paused(self, schedule, exc: Exception) -> None:
        """هشدار اپراتور بعد از خطای متوالی دیوار (ADR-0003 — throttle ۱/۲۴h)."""
        text = (
            f"هشدار: پایش جستجوی «{schedule.search_id}» بعد از "
            f"{self._polling_settings.max_consecutive_errors} خطای متوالی دیوار "
            f"متوقف شد؛ آخرین خطا: {exc}"
        )
        if self._ops_alerter is None:
            self._log.error(
                text,
                extra={"fields": {"event": "polling_paused_no_ops_channel"}},
            )
            return
        sent = await self._ops_alerter.send(text)
        self._log.error(
            text,
            extra={
                "fields": {
                    "event": "polling_paused",
                    "search_id": schedule.search_id,
                    "ops_alert_sent": sent,
                }
            },
        )

    async def _log_orphan_watermarks(self) -> None:
        """watermark بی‌صاحب فقط لاگ اطلاعاتی — حذف نمی‌شود (ADR-0011)."""
        try:
            known = set(self._searches_by_id)
            rows = await self._repository.list_watermarks()
        except Exception as exc:  # noqa: BLE001 - لاگ اطلاعاتی نباید سرویس را بخواباند
            self._log.warning(
                "بررسی watermarkهای بی‌صاحب شکست خورد: %s",
                exc,
                extra={"fields": {"event": "orphan_watermark_check_failed"}},
            )
            return
        for row in rows:
            if row["search_id"] not in known:
                self._log.info(
                    "خط مرز جستجوی «%s» در پایگاه هست ولی جستجو در کانفیگ فعال نیست؛ "
                    "نگه داشته می‌شود و با برگشت همان id ادامه می‌دهد.",
                    row["search_id"],
                    extra={
                        "fields": {
                            "event": "orphan_watermark",
                            "search_id": row["search_id"],
                            "sort_date": row["sort_date"],
                        }
                    },
                )


def _is_stopped(stop) -> bool:
    if stop is None:
        return False
    if isinstance(stop, (asyncio.Event, threading.Event)):
        return stop.is_set()
    if callable(stop):
        return bool(stop())
    return bool(stop)

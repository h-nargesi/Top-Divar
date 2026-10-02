"""زمان‌بند پایش (مرحلهٔ ۴) — configuration.md بخش ۴ و divar-api.md بخش ۱۰.

- هر جستجوی فعال با بازهٔ خودش + لرزش تصادفی (jitter) poll می‌شود؛
  کف `polling.min_interval` بعد از jitter هم رعایت می‌شود
- خطای متوالی دیوار → backoff نمایی (و Retry-After اگر دیوار داد)؛
  بعد از `max_consecutive_errors` خطای متوالی، توقف موقت + لاگ
- concurrency = ۱: درخواست‌های واقعی از صف دیوار عبور می‌کنند (ADR-0012)؛
  زمان‌بند فقط سر رسیدها را حساب می‌کند
"""

import asyncio
import random
import threading
import time
from dataclasses import dataclass

from top_divar.config.durations import DurationError, parse_duration
from top_divar.core.settings import PollingSettings
from top_divar.divar.errors import DivarError
from top_divar.shared.logging import get_logger

_log = get_logger("core.scheduler")

MAX_ERROR_BACKOFF_SECONDS = 3600.0
RUN_WAKEUP_SECONDS = 1.0


def resolve_search_interval(search: dict, settings: PollingSettings) -> float:
    """بازهٔ poll یک جستجو: interval خودش، وگرنه default_interval."""
    value = search.get("interval")
    if value is None:
        return settings.default_interval
    try:
        return parse_duration(value, what="interval")
    except DurationError:
        return settings.default_interval


@dataclass
class _SearchSchedule:
    search: dict
    interval: float
    next_due: float
    consecutive_errors: int = 0

    @property
    def search_id(self):
        return self.search.get("id")


def _uniform(low: float, high: float) -> float:
    return random.uniform(low, high)


class PollScheduler:
    """اجرای poll جستجوها روی سر رسید، با jitter و توقف موقت روی خطای متوالی."""

    def __init__(self, searches, settings: PollingSettings, poll, *, clock=None, sleeper=None, rng=None):
        self._settings = settings
        self._poll = poll
        self._clock = clock or time.monotonic
        self._sleeper = sleeper or asyncio.sleep
        self._rng = rng or _uniform
        now = self._clock()
        self._schedules = []
        for search in searches:
            if not isinstance(search, dict) or not search.get("enabled", True):
                continue
            interval = resolve_search_interval(search, settings)
            self._schedules.append(
                _SearchSchedule(search=search, interval=interval, next_due=now)
            )

    @property
    def schedules(self) -> list:
        return list(self._schedules)

    def _jittered_delay(self, schedule: _SearchSchedule) -> float:
        offset = self._rng(-self._settings.jitter, self._settings.jitter)
        # کف سخت interval بعد از لرزش منفی هم حفظ می‌شود
        return max(schedule.interval + offset, self._settings.min_interval)

    def _error_delay(self, schedule: _SearchSchedule, exc: Exception) -> float:
        retry_after = getattr(exc, "retry_after", None)
        base = schedule.interval * (2 ** min(schedule.consecutive_errors, 10))
        delay = min(base, MAX_ERROR_BACKOFF_SECONDS)
        if retry_after is not None:
            try:
                delay = max(delay, min(float(retry_after), MAX_ERROR_BACKOFF_SECONDS))
            except (TypeError, ValueError):
                pass
        return delay

    async def run_once(self) -> int:
        """poll همهٔ جستجوهای سررسیدشده؛ خروجی تعداد pollهای اجراشده."""
        polled = 0
        for schedule in self._schedules:
            if schedule.next_due > self._clock():
                continue
            polled += 1
            try:
                await self._poll(schedule.search)
            except DivarError as exc:
                schedule.consecutive_errors += 1
                delay = self._error_delay(schedule, exc)
                schedule.next_due = self._clock() + delay
                self._log_poll_failure(schedule, exc, delay)
            else:
                schedule.consecutive_errors = 0
                schedule.next_due = self._clock() + self._jittered_delay(schedule)
        return polled

    def _log_poll_failure(self, schedule: _SearchSchedule, exc: Exception, delay: float) -> None:
        fields = {
            "event": "poll_failed",
            "search_id": schedule.search_id,
            "consecutive_errors": schedule.consecutive_errors,
            "retry_in_seconds": delay,
            "error": str(exc),
        }
        status = getattr(exc, "status", None)
        if status is not None:
            fields["status"] = status
        if schedule.consecutive_errors >= self._settings.max_consecutive_errors:
            fields["event"] = "polling_paused"
            _log.error(
                "توقف موقت پایش جستجوی «%s» بعد از %s خطای متوالی دیوار؛ "
                "حداکثر %s ثانیه دیگر دوباره تلاش می‌کنیم.",
                schedule.search_id,
                schedule.consecutive_errors,
                delay,
                extra={"fields": fields},
            )
        else:
            _log.warning(
                "poll جستجوی «%s» شکست خورد؛ تا %s ثانیه دیگر دوباره تلاش می‌شود: %s",
                schedule.search_id,
                delay,
                exc,
                extra={"fields": fields},
            )

    def seconds_until_next_due(self) -> float:
        if not self._schedules:
            return RUN_WAKEUP_SECONDS
        return max(
            0.0,
            min(schedule.next_due for schedule in self._schedules) - self._clock(),
        )

    async def run(self, stop=None, *, wakeup_seconds: float = RUN_WAKEUP_SECONDS) -> None:
        """حلقهٔ اجرا تا set شدن stop (asyncio.Event / threading.Event / callable)."""
        while not _is_stopped(stop):
            delay = self.seconds_until_next_due()
            if delay > 0:
                await self._sleeper(min(delay, wakeup_seconds))
                continue
            await self.run_once()


def _is_stopped(stop) -> bool:
    if stop is None:
        return False
    if isinstance(stop, (asyncio.Event, threading.Event)):
        return stop.is_set()
    if callable(stop):
        return bool(stop())
    return bool(stop)

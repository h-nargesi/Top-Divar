"""تنظیمات پایش به شکل قابل استفاده در اجرا (مرحلهٔ ۴).

مقادیر از بلوک `polling` کانفیگ خوانده می‌شوند؛ اعتبارسنجی در startup
مال `config.validator` است — اینجا فقط خواندن دفاعی با پیش‌فرض‌های
همان‌جا (configuration.md بخش ۴).
"""

from dataclasses import dataclass

from top_divar.config.durations import DurationError, parse_duration
from top_divar.config.validator import (
    DEFAULT_DEFAULT_INTERVAL,
    DEFAULT_DETAIL_MIN_INTERVAL,
    DEFAULT_JITTER,
    DEFAULT_MAX_CONSECUTIVE_ERRORS,
    DEFAULT_MAX_PAGES_PER_POLL,
    DEFAULT_MIN_INTERVAL,
    DEFAULT_SEARCH_MIN_INTERVAL,
)


@dataclass(frozen=True)
class PollingSettings:
    """کلیدهای بلوک polling بعد از اعتبارسنجی، به ثانیه."""

    search_min_interval: float = parse_duration(DEFAULT_SEARCH_MIN_INTERVAL)
    detail_min_interval: float = parse_duration(DEFAULT_DETAIL_MIN_INTERVAL)
    min_interval: float = parse_duration(DEFAULT_MIN_INTERVAL)
    default_interval: float = parse_duration(DEFAULT_DEFAULT_INTERVAL)
    jitter: float = parse_duration(DEFAULT_JITTER)
    max_consecutive_errors: int = DEFAULT_MAX_CONSECUTIVE_ERRORS
    max_pages_per_poll: int = DEFAULT_MAX_PAGES_PER_POLL
    notify_on_bump: bool = False
    fetch_post_detail: bool = True

    @classmethod
    def from_config(cls, raw: dict) -> "PollingSettings":
        polling = raw.get("polling") if isinstance(raw, dict) else None
        if not isinstance(polling, dict):
            polling = {}

        def duration(key: str, default: str) -> float:
            try:
                return parse_duration(
                    polling.get(key, default), what=f"polling.{key}"
                )
            except DurationError:
                return parse_duration(default, what=f"polling.{key}")

        def positive_int(key: str, default: int) -> int:
            value = polling.get(key)
            if isinstance(value, int) and not isinstance(value, bool) and value >= 1:
                return value
            return default

        return cls(
            search_min_interval=duration(
                "search_min_interval", DEFAULT_SEARCH_MIN_INTERVAL
            ),
            detail_min_interval=duration(
                "detail_min_interval", DEFAULT_DETAIL_MIN_INTERVAL
            ),
            min_interval=duration("min_interval", DEFAULT_MIN_INTERVAL),
            default_interval=duration("default_interval", DEFAULT_DEFAULT_INTERVAL),
            jitter=duration("jitter", DEFAULT_JITTER),
            max_consecutive_errors=positive_int(
                "max_consecutive_errors", DEFAULT_MAX_CONSECUTIVE_ERRORS
            ),
            max_pages_per_poll=positive_int(
                "max_pages_per_poll", DEFAULT_MAX_PAGES_PER_POLL
            ),
            notify_on_bump=bool(polling.get("notify_on_bump", False)),
            fetch_post_detail=bool(polling.get("fetch_post_detail", True)),
        )

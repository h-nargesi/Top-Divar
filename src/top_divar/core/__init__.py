"""پکیج core — زمان‌بند پایش و تشخیص جدید (مرحلهٔ ۴؛ architecture.md بخش ۲)."""

from top_divar.core.detector import BumpEvent, PollOutcome, poll_search
from top_divar.core.scheduler import PollScheduler, resolve_search_interval
from top_divar.core.settings import PollingSettings

__all__ = [
    "BumpEvent",
    "PollOutcome",
    "PollScheduler",
    "PollingSettings",
    "poll_search",
    "resolve_search_interval",
]

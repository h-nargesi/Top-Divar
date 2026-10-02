"""پکیج core — زمان‌بند پایش، تشخیص جدید و امتیاز مطلق (مرحلهٔ ۴ و ۵؛ architecture.md بخش ۲)."""

from top_divar.core.detector import BumpEvent, PollOutcome, poll_search
from top_divar.core.pipeline import ScoringBatchOutcome, score_pending_ads
from top_divar.core.scheduler import PollScheduler, resolve_search_interval
from top_divar.core.scoring import (
    RuleMatch,
    ScoreResult,
    ScoringBlock,
    fields_from_ad_row,
    format_breakdown,
    load_scoring_blocks,
)
from top_divar.core.settings import PollingSettings

__all__ = [
    "BumpEvent",
    "PollOutcome",
    "PollScheduler",
    "PollingSettings",
    "RuleMatch",
    "ScoreResult",
    "ScoringBatchOutcome",
    "ScoringBlock",
    "fields_from_ad_row",
    "format_breakdown",
    "load_scoring_blocks",
    "poll_search",
    "resolve_search_interval",
    "score_pending_ads",
]

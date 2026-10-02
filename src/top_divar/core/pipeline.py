"""خط لولهٔ دو مرحله‌ای poll (مرحلهٔ ۵) — architecture.md «جریان داده».

مرحلهٔ ذخیره مال detector است: آگهی با `scoring_state: pending` می‌نشیند.
اینجا مرحلهٔ دوم است: بعد از پایان ذخیره (و در startup برای آشتی‌سازی
باقی‌ماندهٔ کرش/ری‌استارت)، دستهٔ در انتظار امتیاز می‌گیرد.

- بلوک امتیاز هر آگهی از اولین جستجوی مچ‌شده (matched_searches) می‌آید؛
  ADR-0007 — برچسب/بلوک آگهی مشترک = اولین جستجو
- عبور از حد (score >= min_score) فقط «ممتاز» علامت می‌خورد و لاگ
  می‌شود؛ ردیف تحویل مال مرحلهٔ ۶ است و زیر حد هیچ‌وقت ساخته نمی‌شود
"""

from dataclasses import dataclass, field

from top_divar.core.scoring import (
    DEFAULT_BLOCK_NAME,
    fields_from_ad_row,
    load_scoring_blocks,
)
from top_divar.shared.logging import get_logger

_log = get_logger("core.pipeline")


@dataclass
class ScoringBatchOutcome:
    """نتیجهٔ یک دور امتیازدهی دسته برای لاگ و تست‌ها."""

    scored: int = 0
    notable: int = 0
    unresolved: int = 0   # بلوک امتیاز پیدا نشد؛ آگی pending ماند
    tokens_notable: list = field(default_factory=list)


def resolve_block_name(search_ids, searches_by_id: dict) -> str:
    """اولین جستجوی مچ‌شده → scoring_ref آن (پیش‌فرض default)."""
    for search_id in search_ids:
        search = searches_by_id.get(search_id)
        if isinstance(search, dict):
            ref = search.get("scoring_ref")
            if isinstance(ref, str) and ref:
                return ref
            return DEFAULT_BLOCK_NAME
    return DEFAULT_BLOCK_NAME


async def score_pending_ads(repository, raw_config) -> ScoringBatchOutcome:
    """امتیازدهی همهٔ آگهی‌های pending با بلوک امتیاز جستجوی خودشان."""
    scoring = raw_config.get("scoring") if isinstance(raw_config, dict) else None
    blocks = load_scoring_blocks(scoring)
    searches_by_id = {}
    if isinstance(raw_config, dict):
        for search in raw_config.get("searches") or []:
            if isinstance(search, dict) and isinstance(search.get("id"), str):
                searches_by_id[search["id"]] = search
    outcome = ScoringBatchOutcome()
    pending = await repository.get_pending_ads()
    if not pending:
        return outcome
    for row in pending:
        search_ids = await repository.get_matched_searches(row["id"])
        block_name = resolve_block_name(search_ids, searches_by_id)
        block = blocks.get(block_name)
        if block is None:
            outcome.unresolved += 1
            _log.error(
                "بلوک امتیاز «%s» برای آگهی %s پیدا نشد؛ آگهی pending ماند "
                "(کانفیگ را اصلاح کنید).",
                block_name,
                row["token"],
                extra={
                    "fields": {
                        "event": "scoring_block_missing",
                        "token": row["token"],
                        "block": block_name,
                    }
                },
            )
            continue
        result = block.evaluate(fields_from_ad_row(row))
        await repository.store_score(
            row["token"], result.total, result.breakdown_json()
        )
        outcome.scored += 1
        if result.notable:
            outcome.notable += 1
            outcome.tokens_notable.append(row["token"])
            _log.info(
                "آگهی ممتاز: %s با امتیاز %s (حد %s).",
                row["token"],
                result.total,
                result.min_score,
                extra={
                    "fields": {
                        "event": "ad_notable",
                        "token": row["token"],
                        "score": result.total,
                        "min_score": result.min_score,
                        "block": block_name,
                    }
                },
            )
    _log.info(
        "دور امتیازدهی دسته تمام شد.",
        extra={
            "fields": {
                "event": "scoring_batch_finished",
                "pending": len(pending),
                "scored": outcome.scored,
                "notable": outcome.notable,
                "unresolved": outcome.unresolved,
            }
        },
    )
    return outcome

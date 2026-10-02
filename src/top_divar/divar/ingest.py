"""تبدیل یک صفحهٔ search به ردیف‌های پایگاه (مرحلهٔ ۳).

یک جستجوی کانفیگ → کارت‌ها → جزئیات هر آگهی → درج در پایگاه با
فیلدهای نرمال‌شده. تشخیص «جدید» (watermark/نردبان) مال مرحلهٔ ۴
است؛ اینجا فقط درج انجام می‌شود و توکن تکراری بی‌صدا رد می‌شود.
"""

import json
from dataclasses import dataclass

from top_divar.divar.errors import DivarError
from top_divar.divar.models import AdCard, PostDetail
from top_divar.shared.logging import get_logger
from top_divar.storage.errors import DuplicateTokenError

_log = get_logger("divar.ingest")


@dataclass
class IngestResult:
    cards: int = 0
    stored: int = 0
    duplicates: int = 0
    details_failed: int = 0


def build_ad_record(card: AdCard, detail: PostDetail = None) -> dict:
    """ادغام کارت search و جزئیات → آرگومان‌های insert_ad (بخش ۷)."""
    price = card.price
    price_agreed = card.price_agreed
    if detail is not None and (detail.price is not None or detail.price_agreed):
        price = detail.price
        price_agreed = detail.price_agreed
    raw_payload = {"search_card": card.raw}
    if detail is not None:
        raw_payload["post_detail"] = detail.raw
    record = {
        "token": card.token,
        "sort_date": card.sort_date,
        "title": card.title,
        "price": price,
        "price_per_square": detail.price_per_square if detail else None,
        "size": detail.size if detail else None,
        "rooms": detail.rooms if detail else None,
        "construction_year": detail.construction_year if detail else None,
        "building_age": detail.building_age if detail else None,
        "floor": detail.floor if detail else None,
        "total_floors": detail.total_floors if detail else None,
        "has_parking": detail.has_parking if detail else None,
        "has_elevator": detail.has_elevator if detail else None,
        "has_warehouse": detail.has_warehouse if detail else None,
        "district": (detail.district if detail else None) or card.district,
        "city": (detail.city if detail else None) or card.city,
        "is_promoted": card.is_promoted,
        "image_count": card.image_count,
        "published_at": detail.published_at if detail else None,
        "last_bumped_at": detail.last_bumped_at if detail else None,
        "last_updated_at": detail.last_updated_at if detail else None,
        "raw_json": json.dumps(raw_payload, ensure_ascii=False),
    }
    if price_agreed:
        record["price"] = None
    return record


async def ingest_search_page(fetcher, repository, search: dict) -> IngestResult:
    """واکشی صفحهٔ اول جستجو و ذخیرهٔ همهٔ کارت‌ها با جزئیات (بدون تشخیص جدید)."""
    page = await fetcher.search(search)
    result = IngestResult(cards=len(page.cards))
    for card in page.cards:
        detail = None
        try:
            detail = await fetcher.get_post(card.token)
        except DivarError as exc:
            result.details_failed += 1
            _log.warning(
                "گرفتن جزئیات %s نشد؛ آگهی با فیلدهای غایب ذخیره می‌شود: %s",
                card.token,
                exc,
                extra={"fields": {"event": "post_detail_failed", "token": card.token}},
            )
        if detail is not None and detail.token and detail.token != card.token:
            _log.warning(
                "توکن جزئیات (%s) با توکن جستجو (%s) یکی نیست.",
                detail.token,
                card.token,
                extra={"fields": {"event": "token_mismatch", "token": card.token}},
            )
        if card.sort_date is None:
            _log.warning(
                "کارت %s بدون sort_date ذخیره نشد.",
                card.token,
                extra={"fields": {"event": "card_without_sort_date", "token": card.token}},
            )
            continue
        record = build_ad_record(card, detail)
        try:
            await repository.insert_ad(**record)
            result.stored += 1
        except DuplicateTokenError:
            result.duplicates += 1
    return result

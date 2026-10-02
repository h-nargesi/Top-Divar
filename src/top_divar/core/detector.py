"""تشخیص آگهی جدید در هر poll (مرحلهٔ ۴) — divar-api.md بخش ۹.

- خط مرز (watermark) روی زمان مرتب‌سازی؛ صفحه‌بندی تا خط مرز یا سقف صفحات
- نوبت اول هر جستجو (بدون watermark) = baseline: فقط صفحهٔ اول با پردازش کامل
- توکن یکتا سراسری بین جستجوهاست؛ جستجوی بعدی فقط فهرست مچ
  (matched_searches) را کامل می‌کند (ADR-0007)
- نردبان/ویرایش: token موجود با sort_date تازه‌تر → دوباره جزئیات +
  به‌روزرسانی ردیف؛ پیام مجدد فقط با notify_on_bump (خودِ پیام مال مرحلهٔ ۶)
- سنگ قبر یعنی «دیده‌شده» — آگهی purgeشده هرگز دوباره جدید نیست (ADR-0001)

امتیاز و ارسال در این مرحله ساخته نمی‌شوند.
"""

import datetime
from dataclasses import dataclass, field

from top_divar.core.settings import PollingSettings
from top_divar.divar.errors import DivarError
from top_divar.divar.ingest import build_ad_record
from top_divar.divar.models import AdCard
from top_divar.shared.logging import get_logger
from top_divar.storage.timestamps import to_utc_datetime

_log = get_logger("core.detector")


@dataclass
class BumpEvent:
    """یک sighting نردبان/ویرایش — شواهد جزئیات برای راستی‌آزمایی لاگ (بخش ۹.۹)."""

    token: str
    search_id: str
    sort_date: str
    published_at: str = None
    last_bumped_at: str = None
    last_updated_at: str = None


@dataclass
class PollOutcome:
    """نتیجهٔ یک poll برای لاگ و تست‌ها."""

    search_id: str
    first_poll: bool = False
    pages_fetched: int = 0
    cards_seen: int = 0
    new_ads: int = 0
    duplicates: int = 0
    bumps: list = field(default_factory=list)
    matches_added: int = 0
    details_failed: int = 0
    watermark: str = None            # جدیدترین sort_date دیده‌شده در همین poll
    watermark_reached: bool = False  # صفحه‌بندی روی خط مرز ایستاد
    page_cap_hit: bool = False       # سقف صفحات قبل از خط مرز پر شد
    last_page_reached: bool = False  # has_next_page نبود


async def poll_search(fetcher, repository, search: dict, settings=None) -> PollOutcome:
    """یک poll کامل جستجو: صفحهٔ اول + صفحه‌بندی تا خط مرز (بخش ۹)."""
    if settings is None:
        settings = PollingSettings()
    search_id = search.get("id")
    watermark = await repository.get_watermark(search_id)
    first_poll = watermark is None
    watermark_dt = (
        to_utc_datetime(watermark, what="sort_date") if watermark is not None else None
    )
    outcome = PollOutcome(search_id=search_id, first_poll=first_poll)
    seen_tokens = set()
    newest_seen = None  # datetime
    pagination_data = None
    while True:
        page = await fetcher.search(search, pagination_data=pagination_data)
        outcome.pages_fetched += 1
        outcome.cards_seen += len(page.cards)
        page_newest = _page_newest_sort_date(page.cards)
        for card in page.cards:
            if not card.sort_date:
                _log.warning(
                    "کارت %s بدون sort_date رد شد.",
                    card.token,
                    extra={
                        "fields": {
                            "event": "card_without_sort_date",
                            "token": card.token,
                            "search_id": search_id,
                        }
                    },
                )
                continue
            moment = to_utc_datetime(card.sort_date, what="sort_date")
            if newest_seen is None or moment > newest_seen:
                newest_seen = moment
            if card.token in seen_tokens:
                outcome.duplicates += 1
                continue
            seen_tokens.add(card.token)
            await _process_card(
                card,
                moment,
                fetcher=fetcher,
                repository=repository,
                search_id=search_id,
                settings=settings,
                outcome=outcome,
            )
        if newest_seen is not None:
            outcome.watermark = newest_seen.isoformat()
        if first_poll:
            # نوبت اول = baseline: فقط صفحهٔ اول، پردازش کامل (بخش ۹.۵)
            break
        if not page.has_next_page:
            outcome.last_page_reached = True
            break
        if page_newest is None or (
            watermark_dt is not None and page_newest < watermark_dt
        ):
            # جدیدترینِ صفحه زیر خط مرز است؛ آیتم‌های هم‌زمان با مرز پردازش شدند
            outcome.watermark_reached = True
            break
        if outcome.pages_fetched >= settings.max_pages_per_poll:
            # سقف صفحات قبل از رسیدن به خط مرز پر شد (بخش ۹.۴)
            outcome.page_cap_hit = True
            _log.warning(
                "سقف %s صفحهٔ poll جستجوی «%s» قبل از رسیدن به خط مرز (%s) پر شد — "
                "احتمال از دست رفتن آگهی؛ فیلتر recent_ads آسیب را محدود می‌کند.",
                settings.max_pages_per_poll,
                search_id,
                watermark,
                extra={
                    "fields": {
                        "event": "watermark_not_reached",
                        "search_id": search_id,
                        "pages": outcome.pages_fetched,
                        "watermark": watermark,
                    }
                },
            )
            break
        pagination_data = page.pagination_data
    if outcome.watermark is not None:
        await repository.update_watermark(search_id, outcome.watermark)
    _log.info(
        "poll جستجوی «%s» تمام شد.",
        search_id,
        extra={
            "fields": {
                "event": "poll_finished",
                "search_id": search_id,
                "first_poll": first_poll,
                "pages": outcome.pages_fetched,
                "cards_seen": outcome.cards_seen,
                "new_ads": outcome.new_ads,
                "duplicates": outcome.duplicates,
                "bumps": len(outcome.bumps),
                "matches_added": outcome.matches_added,
                "details_failed": outcome.details_failed,
                "watermark": outcome.watermark,
                "watermark_reached": outcome.watermark_reached,
                "page_cap_hit": outcome.page_cap_hit,
            }
        },
    )
    return outcome


def _page_newest_sort_date(cards) -> datetime.datetime:
    moments = [
        to_utc_datetime(card.sort_date, what="sort_date")
        for card in cards
        if card.sort_date
    ]
    return max(moments) if moments else None


async def _process_card(
    card: AdCard,
    moment: datetime.datetime,
    *,
    fetcher,
    repository,
    search_id: str,
    settings,
    outcome: PollOutcome,
) -> None:
    existing = await repository.get_ad_by_token(card.token)
    if existing is None:
        touched = await repository.touch_tombstone(card.token, card.sort_date)
        if touched is not None:
            # سنگ قبر: purge شده و هرگز دوباره «جدید» نیست (ADR-0001)
            outcome.duplicates += 1
            return
        detail = await _fetch_detail(fetcher, card.token, settings, outcome)
        record = build_ad_record(card, detail)
        ad_id = await repository.insert_ad(**record)
        await repository.record_search_match(ad_id, search_id)
        outcome.new_ads += 1
        return
    linked = await repository.record_search_match(existing["id"], search_id)
    if linked:
        # token سراسری است؛ این جستجو فقط فهرست مچ را کامل کرد (بخش ۹.۱۰)
        outcome.matches_added += 1
    existing_moment = to_utc_datetime(existing["sort_date"], what="sort_date")
    if moment <= existing_moment:
        outcome.duplicates += 1
        return
    # نردبان/ویرایش: token موجود با sort_date تازه‌تر → دوباره جزئیات (بخش ۹.۹)
    detail = await _fetch_detail(fetcher, card.token, settings, outcome)
    if detail is None:
        await repository.refresh_ad_from_card(
            card.token,
            card.sort_date,
            title=card.title,
            is_promoted=card.is_promoted,
            image_count=card.image_count,
        )
    else:
        await repository.refresh_ad(card.token, build_ad_record(card, detail))
    event = BumpEvent(
        token=card.token,
        search_id=search_id,
        sort_date=card.sort_date,
        published_at=detail.published_at if detail else None,
        last_bumped_at=detail.last_bumped_at if detail else None,
        last_updated_at=detail.last_updated_at if detail else None,
    )
    outcome.bumps.append(event)
    _log.info(
        "نردبان/ویرایش شناسایی شد: token «%s» در جستجوی «%s» با sort_date تازه‌تر (%s).",
        card.token,
        search_id,
        card.sort_date,
        extra={
            "fields": {
                "event": "bump_detected",
                "token": card.token,
                "search_id": search_id,
                "sort_date": card.sort_date,
                "old_sort_date": existing["sort_date"],
                "published_at": event.published_at,
                "last_bumped_at": event.last_bumped_at,
                "last_updated_at": event.last_updated_at,
                "notify_on_bump": settings.notify_on_bump,
            }
        },
    )


async def _fetch_detail(fetcher, token: str, settings, outcome: PollOutcome):
    """جزئیات آگهی برای همهٔ آگهی‌های جدید/نردبان (ADR-0009)؛ شکست → None."""
    if not settings.fetch_post_detail:
        return None
    try:
        return await fetcher.get_post(token)
    except DivarError as exc:
        outcome.details_failed += 1
        _log.warning(
            "گرفتن جزئیات %s نشد؛ فیلدهای جزئیات غایب/قبلی می‌مانند: %s",
            token,
            exc,
            extra={"fields": {"event": "post_detail_failed", "token": token}},
        )
        return None

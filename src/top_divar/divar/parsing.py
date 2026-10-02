"""پارسرهای پاسخ دیوار (مرحلهٔ ۳) — divar-api.md بخش ۵، ۷ و ۱۲.

- parse_search_page: کارت‌های POST_ROW + صفحه‌بندی (بخش ۷.۱)
- parse_post_detail_json: جزئیات posts-v2/web (آرایهٔ sections)
- parse_post_detail_html: fallback صفحهٔ SSR با __PRELOADED_STATE__
- پارسر جزئیات روی ویجت‌های {widget_type, data} با عنوان فارسی کار می‌کند؛
  هر دو شکل JSON و HTML به همین لیست نرمال می‌شوند (بخش ۱۲.۲).
"""

import json
import re

from top_divar.divar.errors import DivarSchemaError
from top_divar.divar.models import AdCard, PostDetail, SearchPage
from top_divar.divar.normalization import (
    amenity_from_title,
    building_age_from_year,
    epoch_microseconds_to_iso,
    normalize_text,
    parse_floor_text,
    parse_int_text,
    parse_price_text,
    parse_persian_datetime,
    parse_rooms_value,
)
from top_divar.shared.logging import get_logger

_log = get_logger("divar.parsing")

SEARCH_BASE_URL = "https://api.divar.ir/v8/postlist/w/search"
POST_DETAIL_BASE_URL = "https://api.divar.ir/v8/posts-v2/web"
POST_PAGE_BASE_URL = "https://divar.ir/v"

_PROMOTED_RED_TEXT = "نردبان شده"

_PRELOADED_STATE_PATTERN = re.compile(r"window\.__PRELOADED_STATE__\s*=\s*")

_DATE_ROW_PREFIXES = (
    ("انتشار آگهی", "published_at"),
    ("آخرین نردبان", "last_bumped_at"),
    ("آخرین به‌روزرسانی", "last_updated_at"),
)

_INFO_ITEM_TITLES = {
    "متراژ": "size",
    "ساخت": "construction_year",
    "اتاق": "rooms",
}

_UNEXPANDABLE_TITLES = {
    "قیمت کل": "price",
    "قیمت هر متر": "price_per_square",
    "طبقه": "floor",
}


def parse_search_page(payload: dict) -> SearchPage:
    """پاسخ postlist/w/search → SearchPage؛ پاسخ خالی بدون list_widgets طبیعی است."""
    if not isinstance(payload, dict):
        raise DivarSchemaError("پاسخ search آبجکت JSON نیست.")
    widgets = payload.get("list_widgets")
    no_result = widgets is None
    cards = []
    for widget in widgets or []:
        if widget.get("widget_type") != "POST_ROW":
            continue
        card = _parse_post_row(widget)
        if card is not None:
            cards.append(card)
    pagination = payload.get("pagination") or {}
    page = SearchPage(
        cards=cards,
        has_next_page=bool(pagination.get("has_next_page", False)),
        pagination_data=pagination.get("data"),
        no_result=no_result,
        raw=payload,
    )
    _fill_sort_dates_from_metadata(page)
    return page


def _parse_post_row(widget: dict):
    data = widget.get("data") or {}
    token = data.get("token")
    web_info = {}
    action = data.get("action") or {}
    payload = action.get("payload") or {}
    if not token:
        token = payload.get("token")
    web_info = payload.get("web_info") or {}
    if not token:
        _log.warning(
            "کارت POST_ROW بدون توکن رد شد.",
            extra={"fields": {"event": "post_row_without_token"}},
        )
        return None
    sort_date = None
    info = ((widget.get("action_log") or {}).get("server_side_info") or {}).get("info") or {}
    if info.get("sort_date"):
        sort_date = info["sort_date"]
    price, agreed = parse_price_text(data.get("middle_description_text"))
    return AdCard(
        token=token,
        title=data.get("title"),
        price=price,
        price_agreed=agreed,
        is_promoted=data.get("red_text") == _PROMOTED_RED_TEXT,
        district=normalize_text(web_info.get("district_persian") or "") or None,
        city=normalize_text(web_info.get("city_persian") or "") or None,
        image_count=data.get("image_count"),
        sort_date=sort_date,
        raw=widget,
    )


def _fill_sort_dates_from_metadata(page: SearchPage) -> None:
    """راستی‌آزمایی/جایگزینی sort_date از posts_metadata سطح پاسخ (بخش ۵)."""
    info = ((page.raw.get("action_log") or {}).get("server_side_info") or {}).get("info") or {}
    metadata = info.get("posts_metadata") or []
    by_token = {
        item.get("token"): item.get("sort_date")
        for item in metadata
        if isinstance(item, dict)
    }
    if not by_token:
        return
    for card in page.cards:
        if card.sort_date:
            continue
        epoch = by_token.get(card.token)
        if epoch:
            card.sort_date = epoch_microseconds_to_iso(epoch)


def parse_post_detail(payload: dict) -> PostDetail:
    """جزئیات آگهی در شکل JSON API (sections آرایه) → PostDetail."""
    if not isinstance(payload, dict) or not isinstance(payload.get("sections"), list):
        raise DivarSchemaError("پاسخ جزئیات ساختار sections آرایه‌ای ندارد.")
    sections = {}
    for section in payload["sections"]:
        name = section.get("section_name")
        if name:
            sections.setdefault(name, []).extend(section.get("widgets") or [])
    seo = payload.get("seo") or {}
    web_info = seo.get("web_info") or seo.get("webInfo") or {}
    seo_schema = seo.get("post_seo_schema") or seo.get("postSeoSchema") or {}
    token = (payload.get("webengage") or {}).get("token") or _token_from_share(payload.get("share") or {})
    return _build_detail(sections, web_info, seo_schema, token, raw=payload)


def parse_post_detail_html(html: str) -> PostDetail:
    """صفحهٔ SSR آگهی: __PRELOADED_STATE__ → همان پارسر ویجتی (بخش ۱۲.۲)."""
    state = extract_preloaded_state(html)
    if state is None:
        raise DivarSchemaError("صفحهٔ HTML آگهیت __PRELOADED_STATE__ نداشت.")
    post = ((state.get("currentPost") or {}).get("post")) or {}
    raw_sections = post.get("sections") or {}
    if not isinstance(raw_sections, dict):
        raise DivarSchemaError("sections حالت SSR کلیددار نیست.")
    sections = {}
    for name, items in raw_sections.items():
        widgets = []
        for item in items or []:
            if not isinstance(item, dict):
                continue
            widget = item.get("dto") if isinstance(item.get("dto"), dict) else item
            widget_type = widget.get("widget_type") or item.get("widgetType")
            if widget_type:
                widgets.append({"widget_type": widget_type, "data": widget.get("data") or {}})
        sections[name] = widgets
    seo = post.get("seo") or {}
    web_info = seo.get("webInfo") or seo.get("web_info") or {}
    seo_schema = seo.get("postSeoSchema") or seo.get("post_seo_schema") or {}
    token = post.get("token") or _token_from_share(post.get("share") or {})
    return _build_detail(sections, web_info, seo_schema, token, raw=post)


def extract_preloaded_state(html: str):
    """یافتن و پارس JSON بعد از window.__PRELOADED_STATE__ = (با شمارش آکولاد)."""
    match = _PRELOADED_STATE_PATTERN.search(html)
    if match is None:
        return None
    start = html.find("{", match.end())
    if start == -1:
        return None
    depth = 0
    in_string = False
    escaped = False
    for index in range(start, len(html)):
        char = html[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(html[start : index + 1])
                except json.JSONDecodeError as exc:
                    raise DivarSchemaError(
                        f"JSON __PRELOADED_STATE__ خراب است: {exc}"
                    ) from exc
    return None


def _token_from_share(share: dict):
    url = share.get("web_url") or share.get("webUrl") or ""
    token = url.rstrip("/").rsplit("/", 1)[-1]
    return token or None


def _build_detail(sections: dict, web_info: dict, seo_schema: dict, token, *, raw) -> PostDetail:
    detail = PostDetail(token=token, raw=raw)
    amenities = {}
    for widget in sections.get("LIST_DATA", []):
        widget_type = widget.get("widget_type")
        data = widget.get("data") or {}
        if widget_type == "GROUP_INFO_ROW":
            _apply_info_items(detail, data.get("items") or [])
        elif widget_type == "UNEXPANDABLE_ROW":
            _apply_unexpandable_row(detail, data)
        elif widget_type == "GROUP_FEATURE_ROW":
            _apply_feature_items(amenities, data.get("items") or [])
        elif widget_type == "SELECTOR_ROW":
            _apply_feature_modal(amenities, data)
    for field, value in amenities.items():
        setattr(detail, field, value)
    _apply_title_dates(detail, sections.get("TITLE", []))
    detail.district = normalize_text(web_info.get("district_persian") or "") or None
    detail.city = normalize_text(web_info.get("city_persian") or "") or None
    _apply_seo_fallbacks(detail, seo_schema)
    _reconcile_price(detail, raw)
    detail.building_age = building_age_from_year(detail.construction_year)
    return detail


def _apply_info_items(detail: PostDetail, items) -> None:
    for item in items:
        field = _INFO_ITEM_TITLES.get(normalize_text(item.get("title") or ""))
        if field is None:
            continue
        value = item.get("value")
        if field == "size":
            detail.size = parse_int_text(value)
        elif field == "construction_year":
            detail.construction_year = parse_int_text(value)
        elif field == "rooms":
            detail.rooms = parse_rooms_value(value)


def _apply_unexpandable_row(detail: PostDetail, data: dict) -> None:
    field = _UNEXPANDABLE_TITLES.get(normalize_text(data.get("title") or ""))
    if field is None:
        return
    value = data.get("value")
    if field == "price":
        detail.price, detail.price_agreed = parse_price_text(value)
    elif field == "price_per_square":
        pps, _ = parse_price_text(value)
        detail.price_per_square = pps
    elif field == "floor":
        detail.floor, detail.total_floors = parse_floor_text(value)


def _apply_feature_items(amenities: dict, items) -> None:
    for item in items:
        field, value = amenity_from_title(item.get("title"))
        if field is None:
            continue
        if value is None:
            value = bool(item.get("available", True))
        elif item.get("available") is not None and bool(item["available"]) != value:
            _log.warning(
                "کلید available با قاعدهٔ عنوان امکانات تناقض دارد (title=%r).",
                item.get("title"),
                extra={"fields": {"event": "amenity_conflict"}},
            )
        icon_color = (item.get("icon") or {}).get("icon_color")
        if icon_color == "ICON_HINT" and value:
            _log.warning(
                "icon_color=ICON_HINT اما قاعدهٔ عنوان امکان را موجود گفت (title=%r).",
                item.get("title"),
                extra={"fields": {"event": "amenity_icon_conflict"}},
            )
        amenities[field] = value


def _apply_feature_modal(amenities: dict, data: dict) -> None:
    modal = ((data.get("action") or {}).get("payload") or {}).get("modal_page") or {}
    for widget in modal.get("widget_list") or []:
        if widget.get("widget_type") != "FEATURE_ROW":
            continue
        field, value = amenity_from_title((widget.get("data") or {}).get("title"))
        if field is None:
            continue
        if value is None:
            # آیتم مودال بدون پسوند و بدون کلید available → موجود (بخش ۸.۷ بند ۴)
            value = True
        amenities.setdefault(field, value)


def _apply_title_dates(detail: PostDetail, widgets) -> None:
    for widget in widgets:
        if widget.get("widget_type") != "EXPANDABLE_SECTION":
            continue
        for inner in (widget.get("data") or {}).get("widget_list") or []:
            if inner.get("widget_type") != "DESCRIPTION_ROW":
                continue
            text = (inner.get("data") or {}).get("text") or ""
            _parse_date_rows(detail, text)


def _parse_date_rows(detail: PostDetail, text: str) -> None:
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        head, separator, rest = line.partition(":")
        if not separator:
            continue
        squashed = head.replace("\u200c", "").replace(" ", "")
        for prefix, field in _DATE_ROW_PREFIXES:
            if squashed == prefix.replace("\u200c", "").replace(" ", ""):
                parsed = parse_persian_datetime(rest.strip())
                if parsed is not None:
                    setattr(detail, field, parsed)


def _apply_seo_fallbacks(detail: PostDetail, seo_schema: dict) -> None:
    if detail.size is None:
        floor_size = seo_schema.get("floorSize") or {}
        detail.size = parse_int_text(str(floor_size.get("value"))) if floor_size.get("value") is not None else None
    if detail.rooms is None:
        detail.rooms = parse_rooms_value(seo_schema.get("numberOfRooms"))


def _reconcile_price(detail: PostDetail, raw: dict) -> None:
    """آشتی قیمت کل / قیمت هر متر / متراژ — بخش ۸.۶."""
    webengage_price = (raw.get("webengage") or {}).get("price") if isinstance(raw, dict) else None
    if (
        detail.price is None
        and not detail.price_agreed
        and detail.price_per_square is None
        and isinstance(webengage_price, (int, float))
    ):
        detail.price = int(round(webengage_price / 1_000_000) * 1_000_000)
    if detail.price_agreed:
        return
    if detail.price is not None and detail.price_per_square is not None and detail.size:
        product = detail.price_per_square * detail.size
        difference = abs(detail.price - product)
        consistent = (
            difference <= 1_000_000
            or difference / max(detail.price, product) <= 0.001
        )
        if not consistent:
            _log.warning(
                "قیمت کل با متری×متراژ ناسازگار است (price=%s، pps=%s، size=%s)؛ مقادیر نمایشی ماند.",
                detail.price,
                detail.price_per_square,
                detail.size,
                extra={
                    "fields": {
                        "event": "price_mismatch",
                        "price": detail.price,
                        "pps": detail.price_per_square,
                        "size": detail.size,
                    }
                },
            )
        return
    if detail.price is None and detail.price_per_square is not None and detail.size:
        detail.price = detail.price_per_square * detail.size
        return
    if detail.price_per_square is None and detail.price is not None and detail.size:
        detail.price_per_square = int(round(detail.price / detail.size))

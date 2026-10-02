"""قالب پیام اطلاع‌رسانی (مرحلهٔ ۶) — configuration.md بخش ۳.۲ تا ۳.۴.

- تلگرام: HTML ایمن (escape فقط متن‌های متغیر)، همیشه تک‌پیام،
  برش از میانه با نشانگر «…»؛ خط اول، خط امتیاز و لینک محفوظ می‌مانند
- ایمیل: متن ساده با همان فیلدها + موضوع مصوب `Top Divar — {عنوان} (امتیاز {N})`
- فیلد غایب → آن خط از پیام حذف می‌شود
- زمان‌ها شمسی/تهران با قالب خود دیوار: «روز ماه سال، ساعت»
"""

import datetime
import json

from top_divar.divar.jalali import (
    TEHRAN_UTC_OFFSET,
    gregorian_to_jalali,
    jalali_month_name,
)
from top_divar.storage.errors import StorageError
from top_divar.storage.timestamps import to_utc_datetime

TELEGRAM_MAX_CHARS = 4096
CUT_MARKER = "…"
POST_LINK_PREFIX = "https://divar.ir/v/"

_PERSIAN_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

_AMENITY_LABELS = (
    ("has_parking", "پارکینگ"),
    ("has_elevator", "آسانسور"),
    ("has_warehouse", "انباری"),
)

FALLBACK_TITLE = "آگهی دیوار"


def escape_html(text: str) -> str:
    """escape استاندارد متن متغیر — & < > (ADR-0002)."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def to_persian_digits(text) -> str:
    return str(text).translate(_PERSIAN_DIGITS)


def format_number(value) -> str:
    """عدد با جداکنندهٔ هزارگان و ارقام فارسی: ۱۲,۹۰۰,۰۰۰,۰۰۰."""
    return to_persian_digits(f"{int(value):,}")


def format_jalali_moment(value) -> str:
    """UTC ISO → «۲۲ شهریور ۱۴۰۵، ۱۷:۱۹» به وقت تهران (بخش ۳.۲)."""
    moment = to_utc_datetime(value, what="زمان پیام").astimezone(
        datetime.timezone(TEHRAN_UTC_OFFSET)
    )
    year, month, day = gregorian_to_jalali(moment.year, moment.month, moment.day)
    clock = f"{moment.hour:02d}:{moment.minute:02d}"
    return (
        f"{to_persian_digits(day)} {jalali_month_name(month)} "
        f"{to_persian_digits(year)}، {to_persian_digits(clock)}"
    )


def breakdown_items(score_breakdown) -> list:
    """شکست امتیاز ذخیره‌شده → [(label, points), ...]؛ خراب → تهی."""
    if not isinstance(score_breakdown, str) or not score_breakdown:
        return []
    try:
        payload = json.loads(score_breakdown)
    except json.JSONDecodeError:
        return []
    if not isinstance(payload, list):
        return []
    items = []
    for entry in payload:
        if isinstance(entry, dict) and isinstance(entry.get("label"), str):
            points = entry.get("points")
            if isinstance(points, bool) or not isinstance(points, int):
                continue
            items.append((entry["label"], points))
    return items


def breakdown_text(score_breakdown) -> str:
    """شکست فشرده: «نام: امتیاز · نام: امتیاز» (بخش ۳.۳)."""
    parts = [
        f"{label}: {to_persian_digits(points)}"
        for label, points in breakdown_items(score_breakdown)
    ]
    return " · ".join(parts)


def _price_explicitly_agreed(ad: dict) -> bool:
    raw = ad.get("raw_json")
    if not isinstance(raw, str) or not raw:
        return False
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return False
    return isinstance(payload, dict) and payload.get("price_agreed") is True


def build_field_lines(ad: dict, *, escape=lambda text: text) -> list:
    """فیلدهای «کلید: مقدار» به‌ترتیب بخش ۳.۲؛ فیلد غایب حذف.

    escape روی متن‌های متغیر (محله/شهر) اعمال می‌شود — تلگرام escape_html
    می‌دهد و ایمیل هیچ (بخش ۳.۴: متن ساده).
    """
    lines = []
    if ad.get("price") is not None:
        lines.append(f"قیمت: {format_number(ad['price'])} تومان")
    elif _price_explicitly_agreed(ad):
        lines.append("قیمت: توافقی")
    if ad.get("price_per_square") is not None:
        lines.append(
            f"قیمت هر متر: {format_number(ad['price_per_square'])} تومان"
        )
    if ad.get("size") is not None:
        lines.append(f"متراژ: {to_persian_digits(ad['size'])}")
    if ad.get("rooms") is not None:
        lines.append(f"اتاق: {to_persian_digits(ad['rooms'])}")
    year, age = ad.get("construction_year"), ad.get("building_age")
    if year is not None and age is not None:
        lines.append(
            f"ساخت: {to_persian_digits(year)} (عمر {to_persian_digits(age)} سال)"
        )
    elif year is not None:
        lines.append(f"ساخت: {to_persian_digits(year)}")
    elif age is not None:
        lines.append(f"عمر: {to_persian_digits(age)} سال")
    floor, total = ad.get("floor"), ad.get("total_floors")
    if floor is not None and total is not None:
        lines.append(
            f"طبقه: {to_persian_digits(floor)} از {to_persian_digits(total)}"
        )
    elif floor is not None:
        lines.append(f"طبقه: {to_persian_digits(floor)}")
    amenities = [label for name, label in _AMENITY_LABELS if ad.get(name) is True]
    if amenities:
        lines.append(f"امکانات: {' · '.join(amenities)}")
    if ad.get("district"):
        lines.append(f"محله: {escape(str(ad['district']))}")
    if ad.get("city"):
        lines.append(f"شهر: {escape(str(ad['city']))}")
    if ad.get("published_at"):
        try:
            lines.append(f"انتشار: {format_jalali_moment(ad['published_at'])}")
        except StorageError:
            pass  # تاریخ ناقص → همان خط حذف می‌شود (فیلد غایب)
    return lines


def ad_title(ad: dict) -> str:
    title = ad.get("title")
    return title if isinstance(title, str) and title.strip() else FALLBACK_TITLE


def post_link(ad: dict) -> str:
    return f"{POST_LINK_PREFIX}{ad.get('token')}"


def _score_display(score) -> str:
    return to_persian_digits(score if score is not None else 0)


def _score_line(score, breakdown: str) -> str:
    if breakdown:
        return f"امتیاز: {_score_display(score)} — {breakdown}"
    return f"امتیاز: {_score_display(score)}"


def _cut_middle(text: str, keep: int) -> str:
    """برش از میانه با نشانگر «…» در محل برش (بخش ۳.۲)."""
    keep = max(0, min(keep, len(text)))
    if keep >= len(text):
        return text
    head = keep // 2
    tail = keep - head
    return text[:head] + CUT_MARKER + (text[len(text) - tail:] if tail else "")


def build_telegram_message(
    ad: dict, search_label: str, *, limit: int = TELEGRAM_MAX_CHARS
) -> str:
    """پیام تک‌تکهٔ HTML تلگرام با نردبان برش بخش ۳.۲.

    ترتیب قربانی‌شدن: فیلدهای میانی (از قدیمی‌ترین اولویت نمایش)،
    بعد شکست امتیاز (برش از میانه)، آخر حذف کامل شکست.
    """
    label = search_label if isinstance(search_label, str) and search_label else None
    header_plain = ad_title(ad) if label is None else f"{ad_title(ad)} — {label}"
    link = post_link(ad)
    score = ad.get("score")
    breakdown = breakdown_text(ad.get("score_breakdown"))

    def message_with(fields: list, score_text: str) -> str:
        header = f"<b>{escape_html(header_plain)}</b>"
        parts = [header, *fields, score_text, link]
        return "\n".join(part for part in parts if part)

    full_score_line = escape_html(_score_line(score, breakdown))

    # ۱) پیام کامل
    fields = build_field_lines(ad, escape=escape_html)
    message = message_with(fields, full_score_line)
    if len(message) <= limit:
        return message

    # ۲) حذف فیلدهای میانی از بالا (قدیمی‌ترین اولویت نمایش) به پایین
    for end in range(len(fields) - 1, -1, -1):
        message = message_with(fields[:end], full_score_line)
        if len(message) <= limit:
            return message

    # ۳) برش شکست امتیاز از میانه — بزرگترین برشی که جا می‌شود
    prefix = escape_html(f"امتیاز: {_score_display(score)} — ")
    if breakdown:
        best = None
        lo, hi = 0, len(breakdown) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            candidate = message_with(
                [], prefix + escape_html(_cut_middle(breakdown, mid))
            )
            if len(candidate) <= limit:
                best = candidate
                lo = mid + 1
            else:
                hi = mid - 1
        if best is not None:
            return best

    # ۴) حذف کامل شکست — فقط «امتیاز: N»
    score_only = escape_html(_score_line(score, ""))
    message = message_with([], score_only)
    if len(message) <= limit:
        return message

    # محافظ آخر: عنوان ضدالعقلی بلند — همان خط اول از میانه بریده می‌شود
    keep = limit - (len("<b></b>") + 1 + len("\n".join([score_only, link])) + len(CUT_MARKER))
    while True:
        cut_header = _cut_middle(header_plain, max(keep, 1))
        final = f"<b>{escape_html(cut_header)}</b>\n{score_only}\n{link}"
        if len(final) <= limit:
            return final
        if len(cut_header) >= len(header_plain):
            # escape کاراکترها را بزرگ کرد؛ یک گام محکم‌تر برش بزن
            keep -= 1
            if keep < 1:
                return final
        header_plain = cut_header


def build_email_subject(ad: dict) -> str:
    """موضوع مصوب ایمیل (بخش ۳.۴) — قالب ثابت، قابل فیلتر."""
    return f"Top Divar — {ad_title(ad)} (امتیاز {_score_display(ad.get('score'))})"


def build_email_body(ad: dict, search_label: str) -> str:
    """متن سادهٔ ایمیل با همان فیلدهای پیام تلگرام + لینک در آخر (بخش ۳.۴)."""
    label = search_label if isinstance(search_label, str) and search_label else None
    header = ad_title(ad) if label is None else f"{ad_title(ad)} — {label}"
    score_line = _score_line(ad.get("score"), breakdown_text(ad.get("score_breakdown")))
    parts = [header, *build_field_lines(ad), score_line, post_link(ad)]
    return "\n".join(part for part in parts if part)

"""نرمال‌سازی متن و مقادیر دیوار (divar-api.md بخش ۸).

- ارقام فارسی/عربی → لاتین، جداکننده‌ها و نشانه‌های نامرئی حذف
- قیمت نمایشی → تومان صحیح؛ «توافقی» → null صریح
- طبقه (هر دو شکل)، اتاق (رقم/کلمه)، سال ساخت → عمر
- تاریخ شمسی «روز ماه سال، ساعت» → UTC
- قاعدهٔ عنوانی امکانات (بخش ۸.۷)
"""

import datetime
import re

from top_divar.divar.jalali import (
    MONTH_NAME_TO_NUMBER,
    jalali_datetime_to_utc,
    jalali_year_of,
)
from top_divar.shared.logging import get_logger

_log = get_logger("divar.normalization")

_DIGIT_TRANSLATION = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")
_INVISIBLE_CHARS = "\u200e\u200f\u202a\u202b\u202c\u202d\u202e\ufeff"
_THOUSANDS_SEPARATORS = str.maketrans("", "", ",٬، ")

ROOM_WORD_TO_NUMBER = {
    "یک": 1,
    "دو": 2,
    "سه": 3,
    "چهار": 4,
    "پنج": 5,
}

AMENITY_FIELD_BY_BASE_TITLE = {
    "آسانسور": "has_elevator",
    "پارکینگ": "has_parking",
    "انباری": "has_warehouse",
    "انبار": "has_warehouse",
}

_FLOOR_PATTERN = re.compile(r"^(-?\d+)(?:\s*از\s*(\d+))?$")
_PRICE_NUMBER_PATTERN = re.compile(r"\d+(?:\.\d+)?")
_PERSIAN_DATE_PATTERN = re.compile(
    r"^(?P<day>\d{1,2})\s+(?P<month>[^\s\d]+)\s+(?P<year>\d{2,4})"
    r"[،,]?\s+(?P<hour>\d{1,2}):(?P<minute>\d{1,2})$"
)


def convert_digits(text: str) -> str:
    """ارقام فارسی/عربی → لاتین؛ ممیز فارسی → نقطه."""
    return text.translate(_DIGIT_TRANSLATION).replace("٫", ".")


def clean_number_text(text: str) -> str:
    """ارقام → لاتین؛ حذف نشانه‌های نامرئی، جداکننده‌های هزارگان و فاصله‌ها."""
    converted = convert_digits(text)
    return converted.translate(_THOUSANDS_SEPARATORS).translate(
        str.maketrans("", "", _INVISIBLE_CHARS + " \u200c")
    )


def normalize_text(text: str) -> str:
    """نرمال‌سازی برای تطبیق: ي/ك عربی → فارسی، نیم‌فاصله → فاصله، فاصله‌های تکراری → یکی."""
    return re.sub(r"\s+", " ", text.replace("\u200c", " ").replace("ي", "ی").replace("ك", "ک")).strip()


def parse_price_text(text):
    """متن قیمت نمایشی → (تومان، توافقی؟) — بخش ۸.۱/۸.۲.

    «توافقی» → (None, True) یعنی null صریح؛ متن بی‌عدد → (None, False) یعنی غایب.
    پسوندهای «میلیون»/«میلیارد» در متن خلاصه پشتیبانی می‌شوند (بخش ۸.۲).
    """
    if not isinstance(text, str) or not text.strip():
        return None, False
    if "توافقی" in text:
        return None, True
    cleaned = clean_number_text(convert_digits(text))
    match = _PRICE_NUMBER_PATTERN.search(cleaned)
    if match is None:
        return None, False
    number = float(match.group(0))
    if "میلیارد" in cleaned:
        number *= 1_000_000_000
    elif "میلیون" in cleaned:
        number *= 1_000_000
    return int(round(number)), False


def parse_floor_text(text):
    """متن طبقه → (floor, total_floors) — بخش ۸.۳؛ هر دو شکل «N» و «N از M»."""
    if not isinstance(text, str) or not text.strip():
        return None, None
    normalized = normalize_text(convert_digits(text))
    squashed = normalized.replace(" ", "")
    if "زیرهمکف" in squashed:
        return -1, None
    if "همکف" in squashed:
        return 0, None
    match = _FLOOR_PATTERN.match(normalized)
    if match is None:
        _log.warning(
            "متن طبقه شناسایی نشد: %r",
            text,
            extra={"fields": {"event": "floor_parse_failed"}},
        )
        return None, None
    floor = int(match.group(1))
    total = int(match.group(2)) if match.group(2) is not None else None
    return floor, total


def parse_rooms_value(value):
    """تعداد اتاق → عدد صحیح؛ رقم یا کلمهٔ فارسی (بخش ۸.۵)."""
    if not isinstance(value, str) or not value.strip():
        return None
    normalized = normalize_text(convert_digits(value))
    if re.fullmatch(r"\d+", normalized):
        return int(normalized)
    if normalized in ROOM_WORD_TO_NUMBER:
        return ROOM_WORD_TO_NUMBER[normalized]
    if normalized.startswith("پنج"):
        return 5
    _log.warning(
        "متن اتاق شناسایی نشد: %r",
        value,
        extra={"fields": {"event": "rooms_parse_failed"}},
    )
    return None


def parse_int_text(value):
    """متن عددی (متراژ/ساخت) → عدد صحیح."""
    if not isinstance(value, str) or not value.strip():
        return None
    cleaned = clean_number_text(convert_digits(value))
    if not re.fullmatch(r"\d+", cleaned):
        return None
    return int(cleaned)


def building_age_from_year(construction_year, *, now=None):
    """عمر بنا = سال شمسی جاری − سال ساخت (دقت سال — بخش ۸.۴)."""
    if construction_year is None:
        return None
    moment = now or datetime.datetime.now(datetime.timezone.utc)
    age = jalali_year_of(moment) - construction_year
    if age < 0:
        _log.warning(
            "سال ساخت (%s) از سال جاری بزرگ‌تر است — عمر صفر شد.",
            construction_year,
            extra={"fields": {"event": "building_age_negative"}},
        )
        return 0
    return age


def parse_persian_datetime(text):
    """«۲۲ شهریور ۱۴۰۵، ۱۷:۱۹» به وقت تهران → ISO UTC (بخش ۷.۴)."""
    if not isinstance(text, str) or not text.strip():
        return None
    normalized = normalize_text(convert_digits(text)).replace("،", " ")
    normalized = re.sub(r"\s+", " ", normalized).strip()
    match = _PERSIAN_DATE_PATTERN.match(normalized)
    if match is None:
        return None
    month = MONTH_NAME_TO_NUMBER.get(match.group("month"))
    if month is None:
        return None
    moment = jalali_datetime_to_utc(
        int(match.group("year")),
        month,
        int(match.group("day")),
        int(match.group("hour")),
        int(match.group("minute")),
    )
    return moment.isoformat()


def epoch_microseconds_to_iso(value):
    """sort_date فشردهٔ posts_metadata (epoch میکروثانیه به‌صورت رشته) → ISO UTC."""
    try:
        micros = int(value)
    except (TypeError, ValueError):
        return None
    seconds, remainder = divmod(micros, 1_000_000)
    moment = datetime.datetime.fromtimestamp(
        seconds, tz=datetime.timezone.utc
    ) + datetime.timedelta(microseconds=remainder)
    return moment.isoformat()


def amenity_from_title(title):
    """قاعدهٔ عنوانی امکانات (بخش ۸.۷) → (نام فیلد، مقدار) یا (None, None).

    عنوان «… ندارد» → False؛ «… دارد» → True؛ در غیر این صورت کلید available
    تعیین‌کننده است و این تابع (فیلد، None) برمی‌گرداند تا فراخوان تصمیم بگیرد.
    """
    normalized = normalize_text(title or "")
    if not normalized:
        return None, None
    if normalized.endswith("ندارد"):
        base = normalized[: -len("ندارد")].strip()
        return AMENITY_FIELD_BY_BASE_TITLE.get(base), False
    if normalized.endswith("دارد"):
        base = normalized[: -len("دارد")].strip()
        return AMENITY_FIELD_BY_BASE_TITLE.get(base), True
    return AMENITY_FIELD_BY_BASE_TITLE.get(normalized), None

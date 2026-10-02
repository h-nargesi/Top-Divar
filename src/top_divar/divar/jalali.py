"""تبدیل تقویم شمسی (جلالی) به میلادی و برعکس — بدون وابستگی بیرونی.

الگوریتم استاندارد ۳۳سالهٔ تقویم جلالی (همان الگوریتم شناخته‌شدهٔ
jalaali) با کف‌شکن‌های تاریخی؛ دقت آن برای بازهٔ ۱۳۰۰ تا ۱۵۰۰ کافی است.
کاربرد (divar-api.md بخش ۸.۴ و ۷.۴):
- «ساخت» شمسی → عمر بنا = سال شمسی جاری − سال ساخت
- تاریخ‌های «انتشار/نردبان/به‌روزرسانی» شمسی → UTC (به وقت تهران)
"""

import datetime

TEHRAN_UTC_OFFSET = datetime.timedelta(hours=3, minutes=30)

_MONTH_NAMES = (
    "فروردین",
    "اردیبهشت",
    "خرداد",
    "تیر",
    "مرداد",
    "شهریور",
    "مهر",
    "آبان",
    "آذر",
    "دی",
    "بهمن",
    "اسفند",
)

MONTH_NAME_TO_NUMBER = {name: number for number, name in enumerate(_MONTH_NAMES, start=1)}

_BREAKS = (
    -61, 9, 38, 199, 426, 686, 756, 818, 1111, 1181, 1210, 1635,
    2060, 2097, 2192, 2262, 2324, 2394, 2456, 3178,
)


def _jal_cal(jy: int):
    gy = jy + 621
    leap_j = -14
    jp = _BREAKS[0]
    jump = 0
    for jm in _BREAKS[1:]:
        jump = jm - jp
        if jy < jm:
            break
        leap_j += (jump // 33) * 8 + ((jump % 33) // 4)
        jp = jm
    n = jy - jp
    leap_j += (n // 33) * 8 + ((n % 33) + 3) // 4
    if jump % 33 == 4 and jump - n == 4:
        leap_j += 1
    leap_g = (gy // 4) - (((gy // 100) + 1) * 3) // 4 - 150
    march = 20 + leap_j - leap_g
    if jump - n < 6:
        n = n - jump + ((jump + 4) // 33) * 33
    leap = ((n + 1) % 33 - 1) % 4
    if leap == -1:
        leap = 4
    return leap, gy, march


def _div(a: int, b: int) -> int:
    """تقسیم صحیح رو به صفر (همان div الگوریتم مرجع)."""
    q = a // b
    if q < 0 and q * b != a:
        q += 1
    return q


def _g2d(gy: int, gm: int, gd: int) -> int:
    d = (
        _div((gy + _div(gm - 8, 6) + 100100) * 1461, 4)
        + _div((153 * ((gm + 9) % 12) + 2), 5)
        + gd
        - 34840408
    )
    return d - _div(_div(gy + 100100 + _div(gm - 8, 6), 100) * 3, 4) + 752


def _d2g(jdn: int):
    j = 4 * jdn + 139361631
    j = j + _div(_div(4 * jdn + 183187720, 146097) * 3, 4) * 4 - 3908
    i = _div(j % 1461, 4) * 5 + 308
    gd = _div(i % 153, 5) + 1
    gm = (i // 153) % 12 + 1
    gy = (j // 1461) - 100100 + _div(8 - gm, 6)
    return gy, gm, gd


def _j2d(jy: int, jm: int, jd: int) -> int:
    _, gy, march = _jal_cal(jy)
    return _g2d(gy, 3, march) + (jm - 1) * 31 - (jm // 7) * (jm - 7) + jd - 1


def _d2j(jdn: int):
    gy = _d2g(jdn)[0]
    jy = gy - 621
    leap, _, march = _jal_cal(jy)
    jdn1f = _g2d(gy, 3, march)
    k = jdn - jdn1f
    if k >= 0:
        if k <= 185:
            return jy, 1 + (k // 31), (k % 31) + 1
        k -= 186
    else:
        jy -= 1
        k += 179
        if leap == 1:
            k += 1
    return jy, 7 + (k // 30), (k % 30) + 1


def jalali_to_gregorian(jy: int, jm: int, jd: int):
    gy, gm, gd = _d2g(_j2d(jy, jm, jd))
    return gy, gm, gd


def gregorian_to_jalali(gy: int, gm: int, gd: int):
    jy, jm, jd = _d2j(_g2d(gy, gm, gd))
    return jy, jm, jd


def is_jalali_leap(jy: int) -> bool:
    return _jal_cal(jy)[0] == 0


def jalali_month_name(month: int) -> str:
    """نام ماه شمسی (۱ = فروردین)."""
    return _MONTH_NAMES[month - 1]


def jalali_year_of(moment: datetime.datetime) -> int:
    """سال شمسی یک تاریخ میلادی (مرز سال = ۱ فروردین)."""
    return gregorian_to_jalali(moment.year, moment.month, moment.day)[0]


def jalali_datetime_to_utc(jy: int, jm: int, jd: int, hour: int, minute: int) -> datetime.datetime:
    """تاریخ شمسی به وقت تهران → datetime آگاه UTC."""
    gy, gm, gd = jalali_to_gregorian(jy, jm, jd)
    local = datetime.datetime(gy, gm, gd, hour, minute, tzinfo=datetime.timezone(TEHRAN_UTC_OFFSET))
    return local.astimezone(datetime.timezone.utc)

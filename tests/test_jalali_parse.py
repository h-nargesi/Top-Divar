"""تست parse تاریخ شمسی و مرزهای روز — /resend (مرحلهٔ ۷)."""

import datetime

from top_divar.divar.jalali import (
    gregorian_to_jalali,
    jalali_days_in_month,
    jalali_start_of_day_utc,
    jalali_today,
    parse_jalali_date,
)


def test_parse_accepts_ascii_and_persian_digits_and_separators():
    assert parse_jalali_date("1405/06/01") == (1405, 6, 1)
    assert parse_jalali_date("۱۴۰۵/۰۶/۰۱") == (1405, 6, 1)
    assert parse_jalali_date("۱۴۰۵-۰۶-۰۱") == (1405, 6, 1)
    assert parse_jalali_date(" 1405.6.1 ") == (1405, 6, 1)


def test_parse_rejects_invalid_shapes():
    assert parse_jalali_date("1405/06") is None
    assert parse_jalali_date("1405/06/01/extra") is None
    assert parse_jalali_date("1405/ab/01") is None
    assert parse_jalali_date("") is None
    assert parse_jalali_date(None) is None
    assert parse_jalali_date("1200/01/01") is None  # بیرون دامنهٔ سال
    assert parse_jalali_date("1600/01/01") is None


def test_parse_rejects_invalid_calendar_dates():
    assert parse_jalali_date("1405/13/01") is None
    assert parse_jalali_date("1405/00/01") is None
    assert parse_jalali_date("1405/01/32") is None
    assert parse_jalali_date("1405/07/31") is None  # ماه‌های ۷–۱۱ سی روزند


def test_esfand_leap_day():
    # ۱۴۰۳ کبیسه است → اسفند ۳۰ روز؛ ۱۴۰۴ نیست
    assert jalali_days_in_month(1403, 12) == 30
    assert jalali_days_in_month(1404, 12) == 29
    assert parse_jalali_date("1403/12/30") == (1403, 12, 30)
    assert parse_jalali_date("1404/12/30") is None


def test_start_of_day_utc_is_tehran_midnight():
    moment = jalali_start_of_day_utc(1405, 6, 1)
    assert moment.tzinfo == datetime.timezone.utc
    # نیمه‌شب تهران = ۲۰:۳۰ روز قبل UTC
    assert moment == datetime.datetime(
        2026, 8, 22, 20, 30, tzinfo=datetime.timezone.utc
    )
    assert gregorian_to_jalali(2026, 8, 23) == (1405, 6, 1)
    back = moment + datetime.timedelta(hours=3, minutes=30)
    assert (back.year, back.month, back.day) == (2026, 8, 23)


def test_jalali_today_with_injectable_clock():
    fixed = datetime.datetime(2026, 8, 23, 10, 0, tzinfo=datetime.timezone.utc)
    assert jalali_today(clock=lambda: fixed) == (1405, 6, 1)

import datetime

from top_divar.divar.jalali import (
    gregorian_to_jalali,
    is_jalali_leap,
    jalali_datetime_to_utc,
    jalali_to_gregorian,
    jalali_year_of,
)


def test_known_nowruz_anchors():
    assert jalali_to_gregorian(1403, 1, 1) == (2024, 3, 20)
    assert jalali_to_gregorian(1404, 1, 1) == (2025, 3, 21)
    assert jalali_to_gregorian(1405, 1, 1) == (2026, 3, 21)


def test_leap_years():
    # ۱۴۰۳ کبیسه است (اسفند ۳۰ روزه)؛ ۱۴۰۴ نیست
    assert is_jalali_leap(1403) is True
    assert is_jalali_leap(1404) is False
    assert jalali_to_gregorian(1403, 12, 30) == (2025, 3, 20)


def test_sample_dates_from_fetch_samples():
    # نمونه‌های gammaxvi: «۲۲ شهریور ۱۴۰۵، ۱۷:۱۹» به وقت تهران
    assert jalali_to_gregorian(1405, 6, 22) == (2026, 9, 13)
    assert jalali_to_gregorian(1405, 6, 24) == (2026, 9, 15)


def test_jalali_datetime_to_utc():
    moment = jalali_datetime_to_utc(1405, 6, 22, 17, 19)
    assert moment == datetime.datetime(
        2026, 9, 13, 13, 49, tzinfo=datetime.timezone.utc
    )


def test_gregorian_to_jalali():
    assert gregorian_to_jalali(2026, 10, 2) == (1405, 7, 10)
    assert gregorian_to_jalali(2026, 3, 21) == (1405, 1, 1)


def test_jalali_year_of_uses_year_boundary():
    assert jalali_year_of(datetime.datetime(2026, 3, 20, tzinfo=datetime.timezone.utc)) == 1404
    assert jalali_year_of(datetime.datetime(2026, 3, 21, tzinfo=datetime.timezone.utc)) == 1405


def test_roundtrip_over_decades():
    day = datetime.date(2001, 3, 21)
    for _ in range(365 * 40):
        jy, jm, jd = gregorian_to_jalali(day.year, day.month, day.day)
        assert jalali_to_gregorian(jy, jm, jd) == (day.year, day.month, day.day)
        day += datetime.timedelta(days=1)

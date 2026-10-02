import datetime

from top_divar.divar.normalization import (
    amenity_from_title,
    building_age_from_year,
    clean_number_text,
    convert_digits,
    epoch_microseconds_to_iso,
    normalize_text,
    parse_floor_text,
    parse_int_text,
    parse_persian_datetime,
    parse_price_text,
    parse_rooms_value,
)


class TestDigitsAndText:
    def test_convert_digits(self):
        assert convert_digits("۰۱۲۳۴۵۶۷۸۹") == "0123456789"
        assert convert_digits("٤٥٦") == "456"
        assert convert_digits("۱٫۵") == "1.5"

    def test_clean_number_text_removes_separators_and_invisible(self):
        assert clean_number_text("\u200f۴۸,۵۰۰,۰۰۰,۰۰۰ تومان") == "48500000000تومان"
        assert clean_number_text("۳۵,۰۰۰٬۰۰۰") == "35000000"

    def test_normalize_text(self):
        assert normalize_text("يوسف\u200cآباد  كلان") == "یوسف آباد کلان"
        assert normalize_text("  چند   فاصله  ") == "چند فاصله"


class TestPrice:
    def test_absolute_price_with_persian_digits(self):
        assert parse_price_text("۳۵,۰۰۰,۰۰۰,۰۰۰ تومان") == (35000000000, False)

    def test_price_with_rlm_and_arabic_separator(self):
        assert parse_price_text("\u200f۲۰,۵۰۰,۰۰۰,۰۰۰ تومان") == (20500000000, False)

    def test_agreement_is_explicit_null(self):
        assert parse_price_text("توافقی") == (None, True)

    def test_missing_price(self):
        assert parse_price_text("") == (None, False)
        assert parse_price_text(None) == (None, False)

    def test_compact_million_billion_words(self):
        assert parse_price_text("۲.۵ میلیارد تومان") == (2500000000, False)
        assert parse_price_text("۱۲۰ میلیون تومان") == (120000000, False)


class TestFloor:
    def test_plain_number(self):
        assert parse_floor_text("۵") == (5, None)
        assert parse_floor_text("3") == (3, None)

    def test_n_of_m_variants(self):
        # شکل «N از M» با فیکسچر synthetic (نمونهٔ واقعی Captured نیست — بخش ۸.۳)
        assert parse_floor_text("۳ از ۸") == (3, 8)
        assert parse_floor_text("۳از۸") == (3, 8)
        assert parse_floor_text("3از 8") == (3, 8)

    def test_special_floors(self):
        assert parse_floor_text("همکف") == (0, None)
        assert parse_floor_text("زیرهمکف") == (-1, None)
        assert parse_floor_text("زیر همکف") == (-1, None)
        assert parse_floor_text("-1") == (-1, None)

    def test_unparseable(self):
        assert parse_floor_text("نامشخص") == (None, None)


class TestRooms:
    def test_digits(self):
        assert parse_rooms_value("۲") == 2

    def test_words(self):
        assert parse_rooms_value("یک") == 1
        assert parse_rooms_value("دو") == 2
        assert parse_rooms_value("سه") == 3
        assert parse_rooms_value("چهار") == 4
        assert parse_rooms_value("پنج یا بیشتر") == 5

    def test_invalid(self):
        assert parse_rooms_value("نامشخص") is None


class TestInt:
    def test_size_and_year(self):
        assert parse_int_text("۹۷") == 97
        assert parse_int_text("۱۴۰۳") == 1403
        assert parse_int_text("") is None
        assert parse_int_text("۴۰ متر") is None


class TestBuildingAge:
    def test_year_precision(self):
        now = datetime.datetime(2026, 9, 17, tzinfo=datetime.timezone.utc)  # شهریور ۱۴۰۵
        assert building_age_from_year(1403, now=now) == 2
        assert building_age_from_year(1384, now=now) == 21

    def test_year_boundary(self):
        before_nowruz = datetime.datetime(2026, 3, 20, tzinfo=datetime.timezone.utc)
        assert building_age_from_year(1404, now=before_nowruz) == 0
        after_nowruz = datetime.datetime(2026, 3, 22, tzinfo=datetime.timezone.utc)
        assert building_age_from_year(1404, now=after_nowruz) == 1

    def test_negative_clamped_to_zero(self):
        now = datetime.datetime(2026, 9, 17, tzinfo=datetime.timezone.utc)
        assert building_age_from_year(1410, now=now) == 0

    def test_missing_year(self):
        assert building_age_from_year(None) is None


class TestPersianDatetime:
    def test_sample_format(self):
        assert parse_persian_datetime("۲۲ شهریور ۱۴۰۵، ۱۷:۱۹") == "2026-09-13T13:49:00+00:00"

    def test_invalid(self):
        assert parse_persian_datetime("") is None
        assert parse_persian_datetime("دیشب") is None


class TestEpochMicros:
    def test_posts_metadata_sort_date(self):
        # مقدار نمونهٔ gapa1FMk از posts_metadata
        assert (
            epoch_microseconds_to_iso("1789482557323148")
            == "2026-09-15T14:29:17.323148+00:00"
        )

    def test_invalid(self):
        assert epoch_microseconds_to_iso("nan") is None


class TestAmenityTitleRule:
    def test_positive_item_without_suffix_uses_available(self):
        assert amenity_from_title("آسانسور") == ("has_elevator", None)
        assert amenity_from_title("انباری") == ("has_warehouse", None)
        assert amenity_from_title("انبار") == ("has_warehouse", None)

    def test_negative_title(self):
        assert amenity_from_title("آسانسور ندارد") == ("has_elevator", False)
        assert amenity_from_title("پارکینگ ندارد") == ("has_parking", False)

    def test_modal_pattern(self):
        assert amenity_from_title("بالکن دارد") == (None, True)  # خارج از سه امکان
        assert amenity_from_title("آسانسور دارد") == ("has_elevator", True)

    def test_normalized_titles(self):
        assert amenity_from_title("آسانسور  ندارد") == ("has_elevator", False)

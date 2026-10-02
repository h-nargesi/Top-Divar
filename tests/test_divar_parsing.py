"""تست‌های snapshot پارسر روی نمونه‌های Captured (fetch-sample.md).

فیکسچرها عیناً از docs/fetch-sample.md استخراج شده‌اند (اسکراب REDACTED)
و ساختارشان دست‌نخورده است — اگر دیوار اسکیما را عوض کند این تست‌ها
فوراً فاش می‌کنند (divar-api.md بخش ۱۰).
"""

import json

import pytest

from top_divar.divar.errors import DivarSchemaError
from top_divar.divar.parsing import (
    extract_preloaded_state,
    parse_post_detail,
    parse_post_detail_html,
    parse_search_page,
)

def _load(name):
    import pathlib

    return json.loads(
        (pathlib.Path(__file__).parent / "fixtures" / name).read_text(encoding="utf-8")
    )


def _read(name):
    import pathlib

    return (pathlib.Path(__file__).parent / "fixtures" / name).read_text(encoding="utf-8")


class TestSearchPageSnapshot:
    def test_page1_cards(self):
        page = parse_search_page(_load("search_page1_response.json"))
        assert len(page.cards) == 8
        first = page.cards[0]
        assert first.token == "gapa1FMk"
        assert first.title == "۸۰ متر/۲ خواب/بازسازی شده/صرافهای شمالی"
        assert first.price == 35000000000
        assert first.price_agreed is False
        assert first.is_promoted is False
        assert first.district == "سعادت آباد"
        assert first.city == "تهران"
        assert first.image_count == 8
        assert first.sort_date == "2026-09-15T14:29:17.323148Z"

    def test_page1_pagination(self):
        page = parse_search_page(_load("search_page1_response.json"))
        assert page.has_next_page is True
        assert page.pagination_data["page"] == 1
        assert page.pagination_data["search_uid"] == "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8"
        assert page.pagination_data["viewed_tokens"].startswith("H4sIAAAAAAAE")

    def test_page1_promoted_row(self):
        page = parse_search_page(_load("search_page1_response.json"))
        promoted = [card for card in page.cards if card.is_promoted]
        assert [card.token for card in promoted] == ["gafebEer"]

    def test_page2_ignores_non_post_rows_and_stops(self):
        page = parse_search_page(_load("search_page2_response.json"))
        post_rows = [
            widget
            for widget in page.raw["list_widgets"]
            if widget.get("widget_type") == "POST_ROW"
        ]
        other_rows = [
            widget
            for widget in page.raw["list_widgets"]
            if widget.get("widget_type") != "POST_ROW"
        ]
        assert other_rows  # DIVIDER_ROW و SELECTOR_ROW در صفحهٔ ۲ هست
        assert len(page.cards) == len(post_rows)
        assert page.has_next_page is False  # صفحهٔ آخر: has_next_page غایب است

    def test_empty_response_is_not_error(self):
        page = parse_search_page({"show_no_search_result_notice": True})
        assert page.cards == []
        assert page.no_result is True
        assert page.has_next_page is False

    def test_sort_date_fallback_from_posts_metadata(self):
        payload = _load("search_page1_response.json")
        for widget in payload["list_widgets"]:
            if widget.get("widget_type") == "POST_ROW":
                info = widget["action_log"]["server_side_info"]["info"]
                info.pop("sort_date", None)
                break
        page = parse_search_page(payload)
        assert page.cards[0].sort_date == "2026-09-15T14:29:17.323148+00:00"

    def test_non_dict_payload_raises(self):
        with pytest.raises(DivarSchemaError):
            parse_search_page([1, 2, 3])


class TestPostDetailSnapshot:
    def test_gap5_twe_fields(self):
        detail = parse_post_detail(_load("post_detail_gap5_twe.json"))
        assert detail.token == "gap5-Twe"
        assert detail.size == 97
        assert detail.construction_year == 1403
        assert detail.building_age == 2  # شهریور ۱۴۰۵ − ۱۴۰۳
        assert detail.rooms == 2
        assert detail.price == 48500000000
        assert detail.price_per_square == 500000000
        assert detail.floor == 5
        assert detail.total_floors is None
        assert detail.has_elevator is True
        assert detail.has_parking is True
        assert detail.has_warehouse is True
        assert detail.district == "یوسف آباد"
        assert detail.city == "تهران"

    def test_gap5_twe_dates(self):
        detail = parse_post_detail(_load("post_detail_gap5_twe.json"))
        assert detail.published_at == "2026-07-29T12:13:00+00:00"
        assert detail.last_bumped_at == "2026-09-12T06:57:00+00:00"
        assert detail.last_updated_at == "2026-09-16T07:37:00+00:00"

    def test_gammaxvi_negative_amenities(self):
        detail = parse_post_detail(_load("post_detail_gammaxvi.json"))
        # عنوان «… ندارد» بدون کلید available → False (بخش ۸.۷)
        assert detail.has_elevator is False
        assert detail.has_parking is False
        assert detail.has_warehouse is True

    def test_gammaxvi_price_and_fields(self):
        detail = parse_post_detail(_load("post_detail_gammaxvi.json"))
        assert detail.token == "gammaxvi"
        assert detail.size == 98
        assert detail.construction_year == 1384
        assert detail.price == 20500000000
        assert detail.price_per_square == 209183000
        # 209,183,000 × 98 = 20,499,934,000؛ اختلاف ۶۶هزار ≤ ۱م → سازگار
        assert detail.floor == 3
        assert detail.district == "هروی"

    def test_gammaxvi_dates(self):
        detail = parse_post_detail(_load("post_detail_gammaxvi.json"))
        assert detail.published_at == "2026-09-13T13:49:00+00:00"
        assert detail.last_bumped_at == "2026-09-15T02:31:00+00:00"
        assert detail.last_updated_at == "2026-09-15T02:32:00+00:00"

    def test_webengage_price_not_used_when_text_exists(self):
        # webengage.price = 48499998720 ضرب ممیزی است؛ متن نمایشی ماند (بخش ۸.۶)
        detail = parse_post_detail(_load("post_detail_gap5_twe.json"))
        assert detail.price == 48500000000


class TestHtmlFallbackSnapshot:
    def test_preloaded_state_extraction(self):
        state = extract_preloaded_state(_read("post_page_gap5_twe.html"))
        post = state["currentPost"]["post"]
        assert post["token"] == "gap5-Twe"

    def test_html_detail_fields_match_json_parser(self):
        detail = parse_post_detail_html(_read("post_page_gap5_twe.html"))
        assert detail.token == "gap5-Twe"
        assert detail.size == 97
        assert detail.rooms == 2
        assert detail.price == 48500000000
        assert detail.price_per_square == 500000000
        assert detail.floor == 5
        assert detail.has_elevator is True
        assert detail.has_parking is True
        assert detail.has_warehouse is True
        assert detail.district == "یوسف آباد"
        assert detail.city == "تهران"

    def test_html_without_state_raises(self):
        with pytest.raises(DivarSchemaError):
            parse_post_detail_html("<html><body>خالی</body></html>")


class TestSyntheticFixtures:
    """فیکسچرهای فرضی — صریحاً synthetic و خارج از نمونه‌های Captured."""

    def _detail(self, widgets_extra=None, *, items=None, price="۱۰,۰۰۰,۰۰۰,۰۰۰ تومان"):
        info_items = items or [
            {"title": "متراژ", "value": "۵۰"},
            {"title": "ساخت", "value": "۱۴۰۰"},
            {"title": "اتاق", "value": "۲"},
        ]
        widgets = [
            {"widget_type": "GROUP_INFO_ROW", "data": {"items": info_items}},
            {"widget_type": "UNEXPANDABLE_ROW", "data": {"title": "قیمت کل", "value": price}},
            {"widget_type": "UNEXPANDABLE_ROW", "data": {"title": "قیمت هر متر", "value": "۲۰۰,۰۰۰,۰۰۰ تومان"}},
        ]
        widgets.extend(widgets_extra or [])
        return {"sections": [{"section_name": "LIST_DATA", "widgets": widgets}]}

    def test_floor_n_of_m_synthetic(self):
        payload = self._detail(
            [{"widget_type": "UNEXPANDABLE_ROW", "data": {"title": "طبقه", "value": "۳ از ۸"}}]
        )
        detail = parse_post_detail(payload)
        assert detail.floor == 3
        assert detail.total_floors == 8

    def test_agreement_price(self):
        payload = self._detail(price="توافقی")
        detail = parse_post_detail(payload)
        assert detail.price is None
        assert detail.price_agreed is True

    def test_price_derived_from_pps_times_size(self):
        # قیمت کل غایب، متری و متراژ هست → price = pps × size (بخش ۸.۶ بند ۴)
        payload = {
            "sections": [
                {
                    "section_name": "LIST_DATA",
                    "widgets": [
                        {
                            "widget_type": "GROUP_INFO_ROW",
                            "data": {"items": [{"title": "متراژ", "value": "۵۰"}]},
                        },
                        {
                            "widget_type": "UNEXPANDABLE_ROW",
                            "data": {"title": "قیمت هر متر", "value": "۲۰۰,۰۰۰,۰۰۰ تومان"},
                        },
                    ],
                }
            ]
        }
        detail = parse_post_detail(payload)
        assert detail.price == 10000000000

    def test_pps_derived_from_price_over_size(self):
        payload = {
            "sections": [
                {
                    "section_name": "LIST_DATA",
                    "widgets": [
                        {
                            "widget_type": "GROUP_INFO_ROW",
                            "data": {"items": [{"title": "متراژ", "value": "۹۷"}]},
                        },
                        {
                            "widget_type": "UNEXPANDABLE_ROW",
                            "data": {"title": "قیمت کل", "value": "۴۸,۵۰۰,۰۰۰,۰۰۰ تومان"},
                        },
                    ],
                }
            ]
        }
        detail = parse_post_detail(payload)
        assert detail.price_per_square == 500000000

    def test_webengage_price_used_only_as_last_resort(self):
        payload = self._detail()
        payload["webengage"] = {"token": "synthetic1", "price": 9876543210}
        # هر دو متن موجودند → webengage نادیده
        detail = parse_post_detail(payload)
        assert detail.price == 10000000000

        no_texts = {
            "sections": [{"section_name": "LIST_DATA", "widgets": []}],
            "webengage": {"token": "synthetic1", "price": 9876543210},
        }
        detail = parse_post_detail(no_texts)
        assert detail.price == 9877000000  # گرد شده به نزدیک‌ترین میلیون

    def test_rooms_word_and_seo_fallback(self):
        payload = {
            "sections": [
                {
                    "section_name": "LIST_DATA",
                    "widgets": [
                        {
                            "widget_type": "GROUP_INFO_ROW",
                            "data": {"items": [{"title": "متراژ", "value": "۸۰"}]},
                        }
                    ],
                }
            ],
            "seo": {
                "web_info": {"district_persian": "پونک", "city_persian": "تهران"},
                "post_seo_schema": {"numberOfRooms": "دو", "floorSize": {"value": "81"}},
            },
        }
        detail = parse_post_detail(payload)
        assert detail.rooms == 2
        assert detail.size == 80  # آیتم متراژ ارجح است؛ floorSize فقط fallback است

    def test_amenity_modal_secondary(self):
        # GROUP_FEATURERow فقط آسانسور دارد؛ پارکینگ از مودال ثانویه می‌آید
        payload = self._detail(
            [
                {
                    "widget_type": "GROUP_FEATURE_ROW",
                    "data": {"items": [{"title": "آسانسور", "available": True}]},
                },
                {
                    "widget_type": "SELECTOR_ROW",
                    "data": {
                        "action": {
                            "payload": {
                                "modal_page": {
                                    "widget_list": [
                                        {"widget_type": "FEATURE_ROW", "data": {"title": "آسانسور دارد"}},
                                        {"widget_type": "FEATURE_ROW", "data": {"title": "پارکینگ دارد"}},
                                        {"widget_type": "FEATURE_ROW", "data": {"title": "انباری"}},
                                    ]
                                }
                            }
                        }
                    },
                },
            ]
        )
        detail = parse_post_detail(payload)
        assert detail.has_elevator is True
        assert detail.has_parking is True
        assert detail.has_warehouse is True

    def test_missing_construction_year_means_missing_age(self):
        payload = self._detail(
            items=[{"title": "متراژ", "value": "۵۰"}, {"title": "اتاق", "value": "۱"}]
        )
        detail = parse_post_detail(payload)
        assert detail.construction_year is None
        assert detail.building_age is None

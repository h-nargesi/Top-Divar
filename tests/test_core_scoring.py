"""تست موتور امتیاز مطلق (مرحلهٔ ۵) — configuration.md بخش ۲ و ADR-0005."""

import json

from top_divar.core.scoring import (
    ScoringBlock,
    fields_from_ad_row,
    format_breakdown,
    load_scoring_blocks,
)

# همان قواعد نمونهٔ config.yaml — روی آگهی نمونه، امتیاز ۶۵ می‌دهد
SAMPLE_RULES = [
    {"field": "price", "tiers": [
        {"op": "<=", "value": 12_000_000_000, "points": 30},
        {"op": "<=", "value": 13_500_000_000, "points": 15},
        {"op": "<=", "value": 15_000_000_000, "points": 5},
    ]},
    {"field": "price_per_square", "tiers": [
        {"op": "<=", "value": 280_000_000, "points": 20},
        {"op": "<=", "value": 350_000_000, "points": 10},
    ]},
    {"field": "building_age", "tiers": [
        {"op": "<=", "value": 5, "points": 15},
        {"op": "<=", "value": 15, "points": 5},
    ]},
    {"field": "has_parking", "op": "==", "value": True, "points": 5},
    {"field": "has_elevator", "op": "==", "value": True, "points": 5},
    {"field": "rooms", "op": ">=", "value": 2, "points": 5},
]


def block(rules=None, min_score=60):
    return ScoringBlock.from_config(
        "default",
        {"min_score": min_score, "rules": SAMPLE_RULES if rules is None else rules},
    )


def good_ad():
    # مثل نمونهٔ پیام configuration.md بخش ۳.۲ → امتیاز ۶۵
    return {
        "price": 12_900_000_000,
        "price_per_square": 234_500_000,
        "size": 55,
        "rooms": 2,
        "building_age": 2,
        "floor": 3,
        "has_parking": True,
        "has_elevator": True,
        "has_warehouse": True,
        "district": "پونک",
        "city": "تهران",
        "title": "آپارتمان ۵۵ متری پونک",
        "is_promoted": False,
    }


def test_sample_rules_good_ad_scores_65_and_is_notable():
    result = block().evaluate(good_ad())
    assert result.total == 65
    assert result.notable is True
    labels = {match.field: match.points for match in result.matched}
    assert labels == {
        "price": 15,
        "price_per_square": 20,
        "building_age": 15,
        "has_parking": 5,
        "has_elevator": 5,
        "rooms": 5,
    }


def test_weak_ad_below_threshold_is_not_notable():
    fields = good_ad() | {
        "price": 15_000_000_000,
        "price_per_square": 290_000_000,
        "building_age": 12,
        "district": "مرزگان‌آباد",
    }
    result = block().evaluate(fields)
    # ۵ + ۱۰ + ۵ + ۵ + ۵ + ۵ = ۳۵ < ۶۰
    assert result.total == 35
    assert result.notable is False


def test_tiers_only_first_match_counts():
    result = block().evaluate(good_ad() | {"price": 11_000_000_000})
    prices = [m.points for m in result.matched if m.field == "price"]
    assert prices == [30]  # فقط پلهٔ اول، نه جمع همهٔ پله‌ها


def test_missing_field_skips_whole_rule():
    fields = good_ad()
    del fields["has_elevator"]
    result = block().evaluate(fields)
    assert result.total == 60  # ۵ امتیاز آسانسور نیامد
    assert all(match.field != "has_elevator" for match in result.matched)


def test_explicit_null_price_only_null_rules_evaluate():
    fields = good_ad() | {"price": None}
    result = block().evaluate(fields)
    by_field = {match.field: match.points for match in result.matched}
    # قواعد عددی قیمت skip شدند؛ جریمهٔ == null آمد
    assert by_field.get("price") == -10 or "price" not in by_field
    # ۶۵ − ۱۵ (پلهٔ قیمت) = ۵۰ بدون جریمه
    rules = SAMPLE_RULES + [{"field": "price", "op": "==", "value": None, "points": -10}]
    result = block(rules).evaluate(fields)
    assert result.total == 40  # ۶۵ − ۱۵ − ۱۰
    by_field = {match.field: match.points for match in result.matched}
    assert by_field.get("price") == -10
    assert by_field.get("price_per_square") == 20


def test_not_null_rule_matches_present_value_and_skips_on_null():
    rules = [{"field": "price", "op": "!=", "value": None, "points": 7}]
    result = block(rules, min_score=0).evaluate(good_ad())
    assert result.total == 7
    result = block(rules, min_score=0).evaluate(good_ad() | {"price": None})
    assert result.total == 0
    assert result.matched == ()


def test_absent_price_is_not_explicit_null():
    # قیمت غایب: نه قواعد عددی نه جریمهٔ توافقی
    fields = good_ad()
    del fields["price"]
    result = block(
        SAMPLE_RULES + [{"field": "price", "op": "==", "value": None, "points": -10}]
    ).evaluate(fields)
    assert all(match.field != "price" for match in result.matched)
    assert result.total == 50  # ۶۵ − ۱۵


def test_promoted_penalty_applies():
    result = block(
        SAMPLE_RULES + [{"field": "is_promoted", "op": "==", "value": True, "points": -5}]
    ).evaluate(good_ad() | {"is_promoted": True})
    assert result.total == 60  # ۶۵ − ۵
    promoted = [m for m in result.matched if m.field == "is_promoted"]
    assert len(promoted) == 1 and promoted[0].points == -5


def test_title_penalty_contains_any():
    result = block(
        SAMPLE_RULES
        + [{"field": "title", "op": "contains_any", "value": ["سرمایه‌گذاری", "کلید نخورده"], "points": -10}]
    ).evaluate(good_ad() | {"title": "کلید نخورده، سرمایه‌گذاری"})
    assert result.total == 55  # ۶۵ − ۱۰ (یک بار جریمه)


def test_district_contains_any_rule():
    rules = SAMPLE_RULES + [
        {"field": "district", "op": "contains_any", "value": ["نارمک", "پونک", "شهران"], "points": 10}
    ]
    assert block(rules).evaluate(good_ad()).total == 75  # پونک مچ
    assert block(rules).evaluate(good_ad() | {"district": "مرزگان‌آباد"}).total == 65


def test_contains_any_matches_normalized_text():
    rules = [{"field": "district", "op": "contains_any", "value": ["كردستان"], "points": 10}]
    # ك عربی در مقدار قاعده، ک فارسی در آگهی → نرمال می‌شوند
    assert block(rules, min_score=0).evaluate({"district": "کردستان"}).total == 10
    rules_exact = [{"field": "district", "op": "contains_any", "value": ["پونک"], "points": 10}]
    assert block(rules_exact, min_score=0).evaluate({"district": "پونک شمالی"}).total == 10


def test_in_operator_exact_membership():
    rules = [{"field": "rooms", "op": "in", "value": [1, 2], "points": 4}]
    assert block(rules, min_score=0).evaluate({"rooms": 2}).total == 4
    assert block(rules, min_score=0).evaluate({"rooms": 3}).total == 0


def test_bool_equality_does_not_confuse_with_int():
    rules = [{"field": "has_parking", "op": "==", "value": True, "points": 5}]
    assert block(rules, min_score=0).evaluate({"has_parking": True}).total == 5
    assert block(rules, min_score=0).evaluate({"has_parking": False}).total == 0


def test_numeric_op_on_non_numeric_value_skips():
    rules = [{"field": "district", "op": "<=", "value": 5, "points": 1}]
    assert block(rules, min_score=0).evaluate({"district": "پونک"}).total == 0


def test_min_score_boundary_is_inclusive():
    rules = [{"field": "rooms", "op": ">=", "value": 2, "points": 60}]
    result = block(rules, min_score=60).evaluate({"rooms": 2})
    assert result.total == 60 and result.notable is True


def test_breakdown_format_is_compact_persian():
    result = block().evaluate(good_ad())
    assert format_breakdown(result) == (
        "قیمت≤۱۳.۵B: ۱۵ · قیمت‌متری≤۲۸۰M: ۲۰ · عمر≤۵: ۱۵ · "
        "پارکینگ: ۵ · آسانسور: ۵ · اتاق≥۲: ۵"
    )


def test_breakdown_json_roundtrip():
    result = block().evaluate(good_ad())
    payload = json.loads(result.breakdown_json())
    assert {"label": "پارکینگ", "points": 5} in payload
    assert len(payload) == len(result.matched)


def test_load_scoring_blocks_from_config_shape():
    raw = {
        "scoring": {
            "default": {"min_score": 60, "rules": SAMPLE_RULES},
            "strict": {"min_score": 80, "rules": []},
        }
    }
    blocks = load_scoring_blocks(raw["scoring"])
    assert set(blocks) == {"default", "strict"}
    assert blocks["default"].min_score == 60
    assert len(blocks["default"].rules) == len(SAMPLE_RULES)
    assert blocks["strict"].evaluate(good_ad()).notable is False
    assert load_scoring_blocks(None) == {}


def test_fields_from_ad_row_distinguishes_absent_and_explicit_null():
    row = {
        "price": None,
        "size": 55,
        "has_parking": 1,
        "is_promoted": 0,
        "district": None,
        "raw_json": json.dumps({"search_card": {}, "price_agreed": True}),
    }
    fields = fields_from_ad_row(row)
    assert fields["price"] is None          # null صریح (توافقی)
    assert fields["size"] == 55
    assert fields["has_parking"] is True    # ۰/۱ پایگاه → بولی
    assert fields["is_promoted"] is False
    assert "district" not in fields         # غایب → کلید نیست

    row_absent = {"price": None, "raw_json": json.dumps({"search_card": {}})}
    assert "price" not in fields_from_ad_row(row_absent)


def test_fields_from_ad_row_legacy_card_fallback():
    row = {
        "price": None,
        "raw_json": json.dumps(
            {"search_card": {"data": {"middle_description_text": "توافقی"}}}
        ),
    }
    assert fields_from_ad_row(row).get("price") is None
    row_numeric = {
        "price": None,
        "raw_json": json.dumps(
            {"search_card": {"data": {"middle_description_text": "۱۲ میلیون"}}}
        ),
    }
    assert "price" not in fields_from_ad_row(row_numeric)


def test_fields_from_ad_row_broken_raw_json_is_not_agreed():
    row = {"price": None, "raw_json": "not-json{"}
    assert "price" not in fields_from_ad_row(row)

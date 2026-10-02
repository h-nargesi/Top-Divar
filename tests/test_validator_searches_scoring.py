import copy

import pytest

from top_divar.config import validate_config


def base_config():
    return {
        "searches": [
            {
                "id": "s1",
                "city_ids": ["1"],
                "interval": "5m",
                "form_data": {
                    "category": {"str": {"value": "apartment-sell"}},
                    "price": {
                        "number_range": {"minimum": "10", "maximum": "20"}
                    },
                },
                "scoring_ref": "default",
            }
        ],
        "scoring": {
            "default": {
                "min_score": 60,
                "on_missing_field": "skip",
                "rules": [
                    {
                        "field": "price",
                        "tiers": [
                            {"op": "<=", "value": 100, "points": 30}
                        ],
                    }
                ],
            }
        },
        "polling": {
            "min_interval": "5m",
            "default_interval": "5m",
        },
        "notify": {"channels": []},
        "history": {"purge_margin_days": 7},
    }


def base_env():
    return {
        "TELEGRAM_BOT_TOKEN": "t",
        "TELEGRAM_BOT_PASSWORD": "p",
        "TELEGRAM_OPS_CHAT_ID": "1",
        "SMTP_PASSWORD": "s",
    }


@pytest.fixture
def cfg():
    return base_config()


def codes(report, level):
    return [issue.code for issue in getattr(report, level)]


def test_valid_config_passes(cfg):
    report = validate_config(cfg, base_env())
    assert report.ok, [e.message for e in report.errors]


def test_missing_searches_is_error():
    report = validate_config({}, base_env())
    assert not report.ok
    assert "schema_error" in codes(report, "errors")


def test_duplicate_search_id_is_error(cfg):
    cfg["searches"].append(copy.deepcopy(cfg["searches"][0]))
    report = validate_config(cfg, base_env())
    assert "duplicate_search_id" in codes(report, "errors")


def test_interval_below_min_interval_is_error(cfg):
    cfg["searches"][0]["interval"] = "1m"
    report = validate_config(cfg, base_env())
    assert "interval_below_min" in codes(report, "errors")


def test_default_interval_below_min_interval_is_error(cfg):
    cfg["polling"]["default_interval"] = "1m"
    report = validate_config(cfg, base_env())
    assert "default_interval_below_min" in codes(report, "errors")


def test_deprecated_districts_name_key_is_error(cfg):
    cfg["searches"][0]["districts"] = ["نارمک"]
    report = validate_config(cfg, base_env())
    assert "deprecated_search_key" in codes(report, "errors")


def test_deprecated_allow_unknown_district_is_error(cfg):
    cfg["searches"][0]["allow_unknown_district"] = True
    report = validate_config(cfg, base_env())
    assert "deprecated_search_key" in codes(report, "errors")
    assert "unknown_search_key" not in codes(report, "warnings")


def test_form_data_districts_with_numeric_ids_is_allowed(cfg):
    cfg["searches"][0]["form_data"]["districts"] = {
        "repeated_string": {"value": ["198", "399"]}
    }
    report = validate_config(cfg, base_env())
    assert report.ok, [e.message for e in report.errors]


def test_unknown_form_data_key_is_warning_not_error(cfg):
    cfg["searches"][0]["form_data"]["some_new_divar_filter"] = {
        "str": {"value": "x"}
    }
    report = validate_config(cfg, base_env())
    assert report.ok
    assert "unknown_form_data_key" in codes(report, "warnings")


def test_number_range_without_bounds_is_error(cfg):
    cfg["searches"][0]["form_data"]["price"] = {"number_range": {}}
    report = validate_config(cfg, base_env())
    assert "form_data_bad_value" in codes(report, "errors")


def test_number_range_accepts_string_or_number(cfg):
    cfg["searches"][0]["form_data"]["price"] = {
        "number_range": {"minimum": 10, "maximum": "20"}
    }
    report = validate_config(cfg, base_env())
    assert report.ok, [e.message for e in report.errors]


def test_missing_form_data_is_error(cfg):
    del cfg["searches"][0]["form_data"]
    report = validate_config(cfg, base_env())
    assert not report.ok


def test_scoring_ref_to_missing_block_is_error(cfg):
    cfg["searches"][0]["scoring_ref"] = "typo"
    report = validate_config(cfg, base_env())
    assert "scoring_ref_not_found" in codes(report, "errors")


def test_default_scoring_ref_missing_block_is_error(cfg):
    del cfg["searches"][0]["scoring_ref"]
    cfg["scoring"] = {"other": {"min_score": 10, "rules": []}}
    report = validate_config(cfg, base_env())
    assert "scoring_ref_not_found" in codes(report, "errors")


def test_unknown_scoring_field_is_error(cfg):
    cfg["scoring"]["default"]["rules"].append(
        {"field": "below_neighborhood_avg", "op": "==", "value": True, "points": 5}
    )
    report = validate_config(cfg, base_env())
    assert "unknown_scoring_field" in codes(report, "errors")


def test_on_missing_field_zero_is_error(cfg):
    cfg["scoring"]["default"]["on_missing_field"] = "zero"
    report = validate_config(cfg, base_env())
    assert "on_missing_field_invalid" in codes(report, "errors")


def test_invalid_operator_is_error(cfg):
    cfg["scoring"]["default"]["rules"].append(
        {"field": "price", "op": "~=", "value": 1, "points": 5}
    )
    report = validate_config(cfg, base_env())
    assert "invalid_operator" in codes(report, "errors")


def test_missing_points_is_error(cfg):
    cfg["scoring"]["default"]["rules"].append(
        {"field": "price", "op": "<=", "value": 1}
    )
    report = validate_config(cfg, base_env())
    assert "schema_error" in codes(report, "errors")


def test_missing_value_is_error(cfg):
    cfg["scoring"]["default"]["rules"].append(
        {"field": "price", "op": "<=", "points": 5}
    )
    report = validate_config(cfg, base_env())
    assert "schema_error" in codes(report, "errors")


def test_explicit_null_value_is_allowed(cfg):
    cfg["scoring"]["default"]["rules"].append(
        {"field": "price", "op": "==", "value": None, "points": -10}
    )
    report = validate_config(cfg, base_env())
    assert report.ok, [e.message for e in report.errors]

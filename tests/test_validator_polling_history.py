import pytest

from top_divar.config import validate_config

from test_validator_searches_scoring import base_config, base_env, codes


@pytest.fixture
def cfg():
    return base_config()


def test_search_min_interval_below_5s_is_warning(cfg):
    cfg["polling"]["search_min_interval"] = "2s"
    report = validate_config(cfg, base_env())
    assert report.ok
    assert "polling_min_interval_too_small" in codes(report, "warnings")


def test_detail_min_interval_below_5s_is_warning(cfg):
    cfg["polling"]["detail_min_interval"] = "1s"
    report = validate_config(cfg, base_env())
    assert report.ok
    assert "polling_min_interval_too_small" in codes(report, "warnings")


def test_bad_duration_format_is_error(cfg):
    cfg["polling"]["min_interval"] = "fast"
    report = validate_config(cfg, base_env())
    assert "invalid_duration" in codes(report, "errors")


def test_negative_purge_margin_is_error(cfg):
    cfg["history"]["purge_margin_days"] = -1
    report = validate_config(cfg, base_env())
    assert "purge_margin_negative" in codes(report, "errors")


def test_zero_purge_margin_is_allowed(cfg):
    cfg["history"]["purge_margin_days"] = 0
    report = validate_config(cfg, base_env())
    assert report.ok, [e.message for e in report.errors]


def test_history_defaults_are_ok_when_absent(cfg):
    del cfg["history"]
    report = validate_config(cfg, base_env())
    assert report.ok, [e.message for e in report.errors]


def test_polling_defaults_are_ok_when_absent(cfg):
    del cfg["polling"]
    report = validate_config(cfg, base_env())
    assert report.ok, [e.message for e in report.errors]


def test_unknown_top_level_key_is_warning(cfg):
    cfg["futures"] = {}
    report = validate_config(cfg, base_env())
    assert report.ok
    assert "unknown_top_level_key" in codes(report, "warnings")

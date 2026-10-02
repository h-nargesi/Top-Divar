import pytest

from top_divar.config import validate_config

from test_validator_searches_scoring import base_config, base_env, codes


@pytest.fixture
def cfg():
    return base_config()


def test_telegram_channel_without_token_is_error(cfg):
    env = base_env()
    del env["TELEGRAM_BOT_TOKEN"]
    cfg["notify"]["channels"] = ["telegram"]
    report = validate_config(cfg, env)
    error_messages = [e.message for e in report.errors]
    assert any("TELEGRAM_BOT_TOKEN" in m for m in error_messages)


def test_telegram_channel_without_password_is_error(cfg):
    env = base_env()
    del env["TELEGRAM_BOT_PASSWORD"]
    cfg["notify"]["channels"] = ["telegram"]
    report = validate_config(cfg, env)
    error_messages = [e.message for e in report.errors]
    assert any("TELEGRAM_BOT_PASSWORD" in m for m in error_messages)


def test_email_channel_without_smtp_password_is_error(cfg):
    env = base_env()
    del env["SMTP_PASSWORD"]
    cfg["notify"]["channels"] = ["email"]
    cfg["notify"]["email"] = {
        "smtp": {"host": "smtp.example.com", "port": 587},
        "to": ["user@example.com"],
    }
    report = validate_config(cfg, env)
    assert not report.ok
    assert any("SMTP_PASSWORD" in e.message for e in report.errors)


def test_email_channel_with_empty_to_is_error(cfg):
    cfg["notify"]["channels"] = ["email"]
    cfg["notify"]["email"] = {
        "smtp": {"host": "smtp.example.com", "port": 587},
        "to": [],
    }
    report = validate_config(cfg, base_env())
    assert not report.ok


def test_email_password_env_name_is_respected(cfg):
    env = base_env()
    del env["SMTP_PASSWORD"]
    cfg["notify"]["channels"] = ["email"]
    cfg["notify"]["email"] = {
        "smtp": {
            "host": "smtp.example.com",
            "port": 587,
            "password_env": "MAIL_PASS",
        },
        "to": ["user@example.com"],
    }
    report = validate_config(cfg, env)
    assert any("MAIL_PASS" in e.message for e in report.errors)
    env["MAIL_PASS"] = "x"
    report = validate_config(cfg, env)
    assert report.ok, [e.message for e in report.errors]


def test_missing_ops_env_vars_warn_even_without_channels(cfg):
    env = {"TELEGRAM_BOT_PASSWORD": "p", "SMTP_PASSWORD": "s"}
    report = validate_config(cfg, env)
    assert report.ok
    warning_messages = [w.message for w in report.warnings]
    assert any("TELEGRAM_BOT_TOKEN" in m for m in warning_messages)
    assert any("TELEGRAM_OPS_CHAT_ID" in m for m in warning_messages)


def test_unknown_channel_is_error(cfg):
    cfg["notify"]["channels"] = ["sms"]
    report = validate_config(cfg, base_env())
    assert "unknown_channel" in codes(report, "errors")


def test_backfill_days_above_default_window_is_error(cfg):
    cfg["notify"]["channels"] = ["telegram"]
    cfg["notify"]["telegram"] = {"backfill_days": 45}
    report = validate_config(cfg, base_env())
    assert "backfill_exceeds_window" in codes(report, "errors")


def test_backfill_days_with_active_relative_window(cfg):
    cfg["notify"]["channels"] = ["telegram"]
    cfg["notify"]["telegram"] = {"backfill_days": 20}
    cfg["scoring"]["default"]["relative"] = {
        "enabled": True,
        "window_days_max": 15,
    }
    report = validate_config(cfg, base_env())
    assert "backfill_exceeds_window" in codes(report, "errors")
    cfg["scoring"]["default"]["relative"]["window_days_max"] = 30
    report = validate_config(cfg, base_env())
    assert report.ok, [e.message for e in report.errors]


def test_inactive_relative_block_keeps_system_window(cfg):
    cfg["notify"]["channels"] = ["telegram"]
    cfg["notify"]["telegram"] = {"backfill_days": 20}
    cfg["scoring"]["default"]["relative"] = {
        "enabled": False,
        "window_days_max": 15,
    }
    report = validate_config(cfg, base_env())
    assert report.ok, [e.message for e in report.errors]


def test_smtp_encryption_none_is_warning(cfg):
    cfg["notify"]["channels"] = ["email"]
    cfg["notify"]["email"] = {
        "smtp": {
            "host": "smtp.example.com",
            "port": 587,
            "encryption": "none",
        },
        "to": ["user@example.com"],
    }
    report = validate_config(cfg, base_env())
    assert report.ok
    assert "smtp_encryption_none" in codes(report, "warnings")


def test_smtp_encryption_invalid_is_error(cfg):
    cfg["notify"]["email"] = {
        "smtp": {
            "host": "smtp.example.com",
            "port": 587,
            "encryption": "ssl",
        },
        "to": ["user@example.com"],
    }
    report = validate_config(cfg, base_env())
    assert "schema_error" in codes(report, "errors")

import pytest

from top_divar.cli import main


VALID_YAML = """
searches:
  - id: s1
    city_ids: ["1"]
    form_data:
      category: {str: {value: apartment-sell}}
    scoring_ref: default
scoring:
  default:
    min_score: 60
    on_missing_field: skip
    rules:
      - {field: price, op: "<=", value: 100, points: 5}
"""

BROKEN_YAML = "searches:\n  - id: s1\n   bad: [unclosed\n"

INVALID_YAML = """
searches:
  - id: s1
    city_ids: ["1"]
    districts: [نارمک]
    form_data:
      category: {str: {value: apartment-sell}}
"""


def test_validate_green_on_correct_sample(tmp_path, capsys):
    config = tmp_path / "config.yaml"
    config.write_text(VALID_YAML, encoding="utf-8")
    code = main(["validate", "--config", str(config), "--env", str(tmp_path / ".env")])
    assert code == 0
    out = capsys.readouterr().out
    assert "کانفیگ معتبر است" in out


def test_validate_fails_on_broken_yaml_with_clear_message(tmp_path, capsys):
    config = tmp_path / "config.yaml"
    config.write_text(BROKEN_YAML, encoding="utf-8")
    code = main(["validate", "--config", str(config), "--env", str(tmp_path / ".env")])
    assert code == 1
    err = capsys.readouterr().err
    assert "خطای YAML" in err


def test_validate_fails_on_missing_config_file(tmp_path, capsys):
    code = main(
        ["validate", "--config", str(tmp_path / "nope.yaml"), "--env", str(tmp_path / ".env")]
    )
    assert code == 1
    err = capsys.readouterr().err
    assert "پیدا نشد" in err


def test_validate_reports_deprecated_district_key_as_error(tmp_path, capsys):
    config = tmp_path / "config.yaml"
    config.write_text(INVALID_YAML, encoding="utf-8")
    code = main(["validate", "--config", str(config), "--env", str(tmp_path / ".env")])
    assert code == 1
    captured = capsys.readouterr()
    assert "منسوخ" in captured.err
    assert "کانفیگ نامعتبر است" in captured.err


def test_validate_prints_env_warnings_but_stays_green(tmp_path, capsys):
    config = tmp_path / "config.yaml"
    config.write_text(VALID_YAML, encoding="utf-8")
    code = main(
        [
            "validate",
            "--config",
            str(config),
            "--env",
            str(tmp_path / ".env"),
            "--log-level",
            "ERROR",
        ]
    )
    assert code == 0
    out = capsys.readouterr().out
    assert "هشدار" in out


def test_no_command_prints_help(capsys):
    assert main([]) == 2
    assert "usage" in capsys.readouterr().out

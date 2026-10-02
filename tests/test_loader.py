import pytest

from top_divar.config import ConfigFileError, load_env, load_yaml_file


def test_missing_file_raises_clear_error(tmp_path):
    with pytest.raises(ConfigFileError) as excinfo:
        load_yaml_file(tmp_path / "nope.yaml")
    assert "پیدا نشد" in str(excinfo.value)


def test_broken_yaml_raises_clear_error(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text(
        "searches:\n  - id: s1\n   bad_indent: [unclosed\n", encoding="utf-8"
    )
    with pytest.raises(ConfigFileError) as excinfo:
        load_yaml_file(path)
    message = str(excinfo.value)
    assert "YAML" in message
    assert "خط" in message


def test_duplicate_keys_raise_error(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text(
        "polling:\n  min_interval: 5m\n  min_interval: 1m\n", encoding="utf-8"
    )
    with pytest.raises(ConfigFileError) as excinfo:
        load_yaml_file(path)
    assert "کلید تکراری" in str(excinfo.value)


def test_non_mapping_top_level_raises(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text("- just\n- a list\n", encoding="utf-8")
    with pytest.raises(ConfigFileError) as excinfo:
        load_yaml_file(path)
    assert "mapping" in str(excinfo.value)


def test_valid_yaml_loads(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text("polling:\n  min_interval: 5m\n", encoding="utf-8")
    data = load_yaml_file(path)
    assert data == {"polling": {"min_interval": "5m"}}


def test_load_env_reads_dotenv_and_prefers_real_environ(tmp_path, monkeypatch):
    env_path = tmp_path / ".env"
    env_path.write_text(
        "TELEGRAM_BOT_TOKEN=from-file\nSMTP_PASSWORD=from-file\n", encoding="utf-8"
    )
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "from-environ")
    effective = load_env(env_path)
    assert effective["TELEGRAM_BOT_TOKEN"] == "from-environ"
    assert effective["SMTP_PASSWORD"] == "from-file"


def test_load_env_without_file_still_returns_environ(tmp_path, monkeypatch):
    monkeypatch.setenv("SOME_VAR", "1")
    effective = load_env(tmp_path / ".env")
    assert effective["SOME_VAR"] == "1"

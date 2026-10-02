"""تست دستورهای خط فرمان مرحلهٔ ۷: user، reset-watermark، backup."""

import asyncio

import pytest

from top_divar.cli import main
from top_divar.storage import SqliteRepository


@pytest.fixture(autouse=True)
def isolated_db(tmp_path, monkeypatch):
    """پایگاه دادهٔ CLI (مسیر پیش‌فرض data/) را به tmp می‌برد."""
    db_path = tmp_path / "db.sqlite3"
    monkeypatch.setattr("top_divar.cli.DEFAULT_DB_PATH", db_path)
    yield db_path


def _seed(db_path):
    repo = SqliteRepository(db_path)
    asyncio.run(repo.add_user("alice", 100))
    asyncio.run(repo.add_user("bob", 200))
    ad_id = asyncio.run(
        repo.insert_ad("tok1", "2026-09-20T10:00:00Z", title="آگهی")
    )
    asyncio.run(repo.store_score("tok1", 70, "[]"))
    asyncio.run(
        repo.create_delivery_rows(ad_id, [("telegram", "100")])
    )
    asyncio.run(repo.update_watermark("s1", "2026-09-20T10:00:00Z"))
    repo.close()


def test_user_list_shows_pending_counts(isolated_db, capsys):
    _seed(isolated_db)
    assert main(["user", "list"]) == 0
    out = capsys.readouterr().out
    assert "alice (chat 100) — در انتظار: 1" in out
    assert "bob (chat 200) — در انتظار: 0" in out


def test_user_list_empty(isolated_db, capsys):
    assert main(["user", "list"]) == 0
    assert "هیچ کاربری ثبت‌نام نکرده است" in capsys.readouterr().out


def test_user_remove_marks_pending_dead(isolated_db, capsys):
    _seed(isolated_db)
    assert main(["user", "remove", "alice"]) == 0
    out = capsys.readouterr().out
    assert "حذف شد" in out
    repo = SqliteRepository(isolated_db)
    try:
        assert asyncio.run(repo.get_user("alice")) is None
        deliveries = asyncio.run(repo.get_deliveries(1))
        assert deliveries[0]["status"] == "dead"
    finally:
        repo.close()


def test_user_remove_unknown_fails(isolated_db, capsys):
    _seed(isolated_db)
    assert main(["user", "remove", "ghost"]) == 1
    assert "پیدا نشد" in capsys.readouterr().err


def test_user_without_subcommand_prints_help(capsys):
    assert main(["user"]) == 2
    assert "user list" in capsys.readouterr().out


def test_reset_watermark(isolated_db, capsys):
    _seed(isolated_db)
    assert main(["reset-watermark", "s1"]) == 0
    assert "baseline" in capsys.readouterr().out
    repo = SqliteRepository(isolated_db)
    try:
        assert asyncio.run(repo.get_watermark("s1")) is None
    finally:
        repo.close()
    assert main(["reset-watermark", "s1"]) == 1
    assert "نبود" in capsys.readouterr().err


def test_backup_creates_rotating_snapshot(isolated_db, tmp_path, capsys):
    _seed(isolated_db)
    backups_dir = tmp_path / "backups"
    assert main(["backup", "--output", str(backups_dir), "--keep", "2"]) == 0
    assert main(["backup", "--output", str(backups_dir), "--keep", "2"]) == 0
    assert main(["backup", "--output", str(backups_dir), "--keep", "2"]) == 0
    out = capsys.readouterr().out
    assert out.count("پشتیبان ساخته شد") == 3
    files = list(backups_dir.iterdir())
    assert len(files) == 2  # چرخش: فقط ۲ نسخه ماند
    import sqlite3

    conn = sqlite3.connect(sorted(files)[-1])
    try:
        assert conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 2
    finally:
        conn.close()


def test_backup_default_directory_under_data(isolated_db, tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    _seed(isolated_db)
    assert main(["backup"]) == 0
    files = list((tmp_path / "data" / "backups").iterdir())
    assert len(files) == 1
    assert files[0].name.startswith("top_divar_")

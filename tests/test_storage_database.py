import sqlite3

import pytest

from top_divar.storage import database
from top_divar.storage.errors import StorageError


def test_connect_creates_file_and_parent_directories(tmp_path):
    db_path = tmp_path / "nested" / "data" / "db.sqlite3"
    conn = database.connect(db_path)
    try:
        assert db_path.is_file()
    finally:
        conn.close()


def test_connect_enables_wal_and_busy_timeout(tmp_path):
    conn = database.connect(tmp_path / "db.sqlite3")
    try:
        journal_mode = conn.execute("PRAGMA journal_mode").fetchone()[0]
        busy_timeout = conn.execute("PRAGMA busy_timeout").fetchone()[0]
        foreign_keys = conn.execute("PRAGMA foreign_keys").fetchone()[0]
        assert journal_mode.lower() == "wal"
        assert busy_timeout == database.BUSY_TIMEOUT_MS
        assert foreign_keys == 1
    finally:
        conn.close()


def test_migrate_applies_schema_and_sets_version(tmp_path):
    conn = database.connect(tmp_path / "db.sqlite3")
    try:
        version = database.migrate(conn)
        assert version == database.latest_version()
        tables = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            )
        }
        assert {"ads", "tombstones", "watermarks", "users", "delivery"} <= tables
    finally:
        conn.close()


def test_migrate_is_idempotent_and_keeps_data(tmp_path):
    db_path = tmp_path / "db.sqlite3"
    conn = database.connect(db_path)
    try:
        database.migrate(conn)
        with conn:
            conn.execute(
                """
                INSERT INTO ads (token, sort_date, created_at, updated_at)
                VALUES ('tok1', '2026-09-01T00:00:00+00:00', 'x', 'x')
                """
            )
    finally:
        conn.close()
    conn = database.connect(db_path)
    try:
        version = database.migrate(conn)
        assert version == database.latest_version()
        row = conn.execute("SELECT token FROM ads").fetchone()
        assert row["token"] == "tok1"
    finally:
        conn.close()


def test_migrate_rejects_future_schema_version(tmp_path):
    conn = database.connect(tmp_path / "db.sqlite3")
    try:
        with conn:
            conn.execute("PRAGMA user_version = 99")
        with pytest.raises(StorageError) as excinfo:
            database.migrate(conn)
        assert "جدیدتر" in str(excinfo.value)
    finally:
        conn.close()


def test_unique_index_on_token_rejects_duplicates(tmp_path):
    conn = database.connect(tmp_path / "db.sqlite3")
    try:
        database.migrate(conn)
        with conn:
            conn.execute(
                """
                INSERT INTO ads (token, sort_date, created_at, updated_at)
                VALUES ('tok1', '2026-09-01T00:00:00+00:00', 'x', 'x')
                """
            )
        with pytest.raises(sqlite3.IntegrityError):
            with conn:
                conn.execute(
                    """
                    INSERT INTO ads (token, sort_date, created_at, updated_at)
                    VALUES ('tok1', '2026-09-02T00:00:00+00:00', 'x', 'x')
                    """
                )
    finally:
        conn.close()

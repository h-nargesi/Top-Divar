"""تست ذخیره — متدهای مرحلهٔ ۷ (بات و پایداری)."""

import asyncio
import datetime
import sqlite3

import pytest

from top_divar.storage import (
    DEFAULT_BACKUP_KEEP,
    SqliteRepository,
    StorageError,
    backup_database,
    rotate_backups,
)
from top_divar.storage.timestamps import utc_now


@pytest.fixture()
def repo(tmp_path):
    repository = SqliteRepository(tmp_path / "db.sqlite3")
    yield repository
    repository.close()


def _insert(repo, token, sort_date="2026-09-20T10:00:00Z", **overrides):
    fields = {
        "title": "آپارتمان آزمایش",
        "price": 1_000_000_000,
        "district": "پونک",
        "raw_json": '{"v": 1}',
    }
    fields.update(overrides)
    return asyncio.run(repo.insert_ad(token, sort_date, **fields))


def _delivery(repo, ad_id, recipient, *, status="pending", **overrides):
    count = asyncio.run(
        repo.create_delivery_rows(ad_id, [("telegram", recipient)])
    )
    assert count == 1
    if status != "pending" or overrides:
        row = asyncio.run(repo.get_deliveries(ad_id))[0]
        asyncio.run(repo.mark_delivery(row["id"], status, **overrides))
    return asyncio.run(repo.get_deliveries(ad_id))[0]


def test_get_pending_deliveries_ignores_backoff_for_backfill(repo):
    """G5: جبران تعاملی بی‌تاب به next_attempt_at است — برخلاف سویپ."""
    ad_id = _insert(repo, "a")
    _delivery(
        repo,
        ad_id,
        "100",
        next_attempt_at=utc_now() + datetime.timedelta(hours=12),
    )
    due = asyncio.run(repo.get_due_deliveries(channel="telegram"))
    assert due == []
    pending = asyncio.run(
        repo.get_pending_deliveries(channel="telegram", recipient="100")
    )
    assert [row["ad"]["token"] for row in pending] == ["a"]


def test_get_pending_deliveries_filters_and_window(repo):
    ad_a = _insert(repo, "a")
    ad_b = _insert(repo, "b")
    ad_c = _insert(repo, "c")
    _delivery(repo, ad_a, "100")
    _delivery(repo, ad_b, "200")
    _delivery(repo, ad_c, "100", status="dead")
    rows = asyncio.run(repo.get_pending_deliveries(recipient="100"))
    assert [row["ad"]["token"] for row in rows] == ["a"]
    rows = asyncio.run(
        repo.get_pending_deliveries(
            recipient="100",
            since=utc_now() + datetime.timedelta(days=1),
        )
    )
    assert rows == []
    rows = asyncio.run(
        repo.get_pending_deliveries(
            recipient="100",
            since=utc_now() - datetime.timedelta(days=7),
        )
    )
    assert [row["ad"]["token"] for row in rows] == ["a"]


def test_count_pending_deliveries(repo):
    ad_id = _insert(repo, "a")
    _delivery(repo, ad_id, "100")
    _delivery(repo, _insert(repo, "b"), "100")
    _delivery(repo, _insert(repo, "c"), "200")
    _delivery(repo, _insert(repo, "d"), "100", status="sent")
    assert asyncio.run(repo.count_pending_deliveries(recipient="100")) == 2
    assert asyncio.run(repo.count_pending_deliveries(recipient="200")) == 1
    assert asyncio.run(repo.count_pending_deliveries(recipient="999")) == 0


def test_list_users_with_pending_counts(repo):
    asyncio.run(repo.add_user("alice", 100))
    asyncio.run(repo.add_user("bob", 200))
    _delivery(repo, _insert(repo, "a"), "100")
    _delivery(repo, _insert(repo, "b"), "100")
    _delivery(repo, _insert(repo, "c"), "300")
    users = asyncio.run(repo.list_users_with_pending())
    by_name = {user["username"]: user for user in users}
    assert by_name["alice"]["pending"] == 2
    assert by_name["bob"]["pending"] == 0


def test_delete_user_marks_pending_dead_and_keeps_sent(repo):
    """G3: حذف کاربر pendingهای او را dead می‌کند؛ sent تاریخچه می‌ماند."""
    asyncio.run(repo.add_user("alice", 100))
    pending = _delivery(repo, _insert(repo, "a"), "100")
    sent = _delivery(repo, _insert(repo, "b"), "100", status="sent")
    other = _delivery(repo, _insert(repo, "c"), "200")

    removed = asyncio.run(repo.delete_user("alice"))
    assert removed["username"] == "alice"
    assert removed["pending_dead"] == 1
    assert asyncio.run(repo.get_user("alice")) is None
    assert asyncio.run(repo.get_user_by_chat_id(100)) is None

    statuses = {
        row["ad_id"]: row["status"] for row in asyncio.run(repo.get_deliveries(pending["ad_id"]))
    }
    assert statuses[pending["ad_id"]] == "dead"
    assert asyncio.run(repo.get_deliveries(sent["ad_id"]))[0]["status"] == "sent"
    assert asyncio.run(repo.get_deliveries(other["ad_id"]))[0]["status"] == "pending"

    assert asyncio.run(repo.delete_user("ghost")) is None


def test_get_notable_ads_since_requires_delivery_row(repo):
    """«ممتاز» = وجود ردیف delivery — آگهی زیر min_score ردیف ندارد."""
    _insert(repo, "plain", "2026-09-10T10:00:00Z")
    notable_old = _insert(repo, "old", "2026-09-10T10:00:00Z")
    notable_new = _insert(repo, "new", "2026-09-20T10:00:00Z")
    dead_notable = _insert(repo, "dead", "2026-09-15T10:00:00Z")
    _delivery(repo, notable_old, "100")
    _delivery(repo, notable_new, "100")
    _delivery(repo, dead_notable, "100", status="dead")

    rows = asyncio.run(
        repo.get_notable_ads_since("2026-09-12T00:00:00Z")
    )
    # قدیمی‌ترین اول؛ وضعیت ردیف (حتی dead) مهم نیست
    assert [row["token"] for row in rows] == ["dead", "new"]
    rows = asyncio.run(repo.get_notable_ads_since("2026-09-01T00:00:00Z"))
    assert [row["token"] for row in rows] == ["old", "dead", "new"]


def test_vacuum_into_creates_consistent_snapshot(repo, tmp_path):
    ad_id = _insert(repo, "a")
    _delivery(repo, ad_id, "100")
    asyncio.run(repo.store_score("a", 70, "[]"))
    snapshot = tmp_path / "snapshot.sqlite3"
    asyncio.run(repo.vacuum_into(snapshot))
    assert snapshot.is_file()
    conn = sqlite3.connect(snapshot)
    try:
        assert conn.execute("SELECT COUNT(*) FROM ads").fetchone()[0] == 1
        assert conn.execute("SELECT COUNT(*) FROM delivery").fetchone()[0] == 1
        assert (
            conn.execute("SELECT scoring_state FROM ads").fetchone()[0]
            == "scored"
        )
    finally:
        conn.close()
    with pytest.raises(StorageError):
        asyncio.run(repo.vacuum_into(" "))


def test_backup_database_rotates_old_versions(repo, tmp_path):
    backups_dir = tmp_path / "backups"
    base = datetime.datetime(2026, 10, 1, tzinfo=datetime.timezone.utc)
    for index in range(DEFAULT_BACKUP_KEEP + 2):
        moment = base + datetime.timedelta(minutes=index)
        asyncio.run(
            backup_database(repo, backups_dir, keep=DEFAULT_BACKUP_KEEP, now=moment)
        )
    files = sorted(path.name for path in backups_dir.iterdir())
    assert len(files) == DEFAULT_BACKUP_KEEP
    # دو نسخهٔ قدیمی‌تر (00:00 و 00:01) حذف شده‌اند؛ جدیدترین مانده
    assert files[0] == "top_divar_20261001_000200.sqlite3"
    assert files[-1] == "top_divar_20261001_000800.sqlite3"
    (backups_dir / "unrelated.txt").write_text("x")
    removed = rotate_backups(backups_dir, keep=DEFAULT_BACKUP_KEEP)
    assert removed == []
    assert (backups_dir / "unrelated.txt").is_file()


def test_delete_watermark_only_target(repo):
    asyncio.run(repo.update_watermark("s1", "2026-09-20T10:00:00Z"))
    asyncio.run(repo.update_watermark("s2", "2026-09-21T10:00:00Z"))
    assert asyncio.run(repo.delete_watermark("s1")) is True
    assert asyncio.run(repo.get_watermark("s1")) is None
    assert asyncio.run(repo.get_watermark("s2")) == "2026-09-21T10:00:00+00:00"
    assert asyncio.run(repo.delete_watermark("s1")) is False
    watermarks = asyncio.run(repo.list_watermarks())
    assert [row["search_id"] for row in watermarks] == ["s2"]

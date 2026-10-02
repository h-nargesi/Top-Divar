import asyncio
import datetime

import pytest

from top_divar.storage import (
    SqliteRepository,
    StorageError,
    derive_purge_after_days,
)

NOW = datetime.datetime(2026, 10, 2, 12, 0, 0, tzinfo=datetime.timezone.utc)


def days_ago(days: int) -> str:
    return (NOW - datetime.timedelta(days=days)).isoformat()


@pytest.fixture()
def repo(tmp_path):
    repository = SqliteRepository(tmp_path / "db.sqlite3")
    yield repository
    repository.close()


def test_derive_purge_after_days_defaults_to_37():
    assert derive_purge_after_days({}) == 37
    assert derive_purge_after_days(None) == 37


def test_derive_purge_after_days_uses_active_relative_window():
    config = {
        "scoring": {
            "default": {
                "relative": {"enabled": True, "window_days_max": 21},
            }
        }
    }
    assert derive_purge_after_days(config) == 28


def test_derive_purge_after_days_ignores_inactive_relative_block():
    config = {
        "scoring": {
            "default": {
                "relative": {"enabled": False, "window_days_max": 21},
            }
        }
    }
    assert derive_purge_after_days(config) == 37


def test_derive_purge_after_days_uses_configured_margin():
    config = {"history": {"purge_margin_days": 14}}
    assert derive_purge_after_days(config) == 44


def test_purge_removes_old_ads_and_deliveries_but_keeps_tombstone(repo):
    old_id = asyncio.run(repo.insert_ad("old-token", days_ago(40)))
    asyncio.run(repo.insert_ad("fresh-token", days_ago(1)))
    asyncio.run(
        repo.create_delivery_rows(
            old_id, [("telegram", "12345"), ("email", "user@example.com")]
        )
    )

    result = asyncio.run(repo.purge_expired(37, now=NOW))

    assert result["ads"] == 1
    assert result["deliveries"] == 2
    assert asyncio.run(repo.get_ad_by_token("old-token")) is None
    assert asyncio.run(repo.get_deliveries(old_id)) == []
    fresh = asyncio.run(repo.get_ad_by_token("fresh-token"))
    assert fresh is not None
    assert asyncio.run(repo.get_tombstone("fresh-token")) is None

    tombstone = asyncio.run(repo.get_tombstone("old-token"))
    assert tombstone is not None
    assert tombstone["last_sort_date"] == days_ago(40)


def test_purge_boundary_is_exclusive(repo):
    asyncio.run(repo.insert_ad("edge-token", days_ago(37)))
    result = asyncio.run(repo.purge_expired(37, now=NOW))
    assert result["ads"] == 0
    assert asyncio.run(repo.get_ad_by_token("edge-token")) is not None


def test_tombstone_survives_later_purges_forever(repo):
    old_id = asyncio.run(repo.insert_ad("old-token", days_ago(40)))
    asyncio.run(repo.purge_expired(37, now=NOW))
    later = NOW + datetime.timedelta(days=10)
    asyncio.run(repo.purge_expired(37, now=later))
    tombstone = asyncio.run(repo.get_tombstone("old-token"))
    assert tombstone is not None
    assert tombstone["last_sort_date"] == days_ago(40)


def test_republished_token_after_purge_updates_tombstone_to_newer_date(repo):
    asyncio.run(repo.insert_ad("tok", days_ago(40)))
    asyncio.run(repo.purge_expired(37, now=NOW))
    asyncio.run(repo.insert_ad("tok", days_ago(2)))
    result = asyncio.run(repo.purge_expired(1, now=NOW))
    assert result["ads"] == 1
    tombstone = asyncio.run(repo.get_tombstone("tok"))
    assert tombstone["last_sort_date"] == days_ago(2)


def test_purge_rejects_invalid_days(repo):
    with pytest.raises(StorageError):
        asyncio.run(repo.purge_expired(-1, now=NOW))
    with pytest.raises(StorageError):
        asyncio.run(repo.purge_expired("37", now=NOW))

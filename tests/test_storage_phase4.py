import asyncio

import pytest

from top_divar.storage import SqliteRepository, StorageError


@pytest.fixture()
def repo(tmp_path):
    repository = SqliteRepository(tmp_path / "db.sqlite3")
    yield repository
    repository.close()


def _insert(repo, token, sort_date, **overrides):
    fields = {
        "title": "آپارتمان آزمایش",
        "price": 1_000_000_000,
        "size": 50,
        "district": "پونک",
        "raw_json": '{"v": 1}',
    }
    fields.update(overrides)
    return asyncio.run(repo.insert_ad(token, sort_date, **fields))


def test_schema_version_2(repo):
    assert repo.schema_version == 2


def test_record_search_match_is_idempotent(repo):
    ad_id = _insert(repo, "tok1", "2026-09-20T10:00:00Z")
    assert asyncio.run(repo.record_search_match(ad_id, "s1")) is True
    assert asyncio.run(repo.record_search_match(ad_id, "s1")) is False
    assert asyncio.run(repo.record_search_match(ad_id, "s2")) is True
    assert asyncio.run(repo.get_matched_searches(ad_id)) == ["s1", "s2"]


def test_record_search_match_rejects_unknown_ad(repo):
    with pytest.raises(StorageError):
        asyncio.run(repo.record_search_match(9999, "s1"))


def test_refresh_ad_updates_fields_and_sort_date(repo):
    _insert(repo, "tok1", "2026-09-20T10:00:00Z", size=50, price=1_000)
    asyncio.run(repo.set_scoring_state("tok1", "scored"))
    updated = asyncio.run(
        repo.refresh_ad(
            "tok1",
            {
                "sort_date": "2026-09-25T08:00:00Z",
                "title": "عنوان تازه",
                "price": 2_000,
                "size": 60,
                "raw_json": '{"v": 2}',
            },
        )
    )
    assert updated is True
    row = asyncio.run(repo.get_ad_by_token("tok1"))
    assert row["sort_date"] == "2026-09-25T08:00:00+00:00"
    assert row["title"] == "عنوان تازه"
    assert row["price"] == 2_000
    assert row["size"] == 60
    assert row["scoring_state"] == "pending"


def test_refresh_ad_missing_token_returns_false(repo):
    updated = asyncio.run(
        repo.refresh_ad("ghost", {"sort_date": "2026-09-25T08:00:00Z"})
    )
    assert updated is False


def test_refresh_ad_requires_sort_date(repo):
    _insert(repo, "tok1", "2026-09-20T10:00:00Z")
    with pytest.raises(StorageError):
        asyncio.run(repo.refresh_ad("tok1", {"title": "بدون تاریخ"}))


def test_refresh_ad_from_card_keeps_detail_fields(repo):
    _insert(repo, "tok1", "2026-09-20T10:00:00Z", size=97, price_per_square=500_000_000)
    updated = asyncio.run(
        repo.refresh_ad_from_card(
            "tok1",
            "2026-09-26T09:30:00Z",
            title="عنوان کارت",
            is_promoted=True,
            image_count=3,
        )
    )
    assert updated is True
    row = asyncio.run(repo.get_ad_by_token("tok1"))
    assert row["sort_date"] == "2026-09-26T09:30:00+00:00"
    assert row["title"] == "عنوان کارت"
    assert row["is_promoted"] == 1
    assert row["image_count"] == 3
    # فیلدهای وابسته به جزئیات باید دست‌نخورده بمانند
    assert row["size"] == 97
    assert row["price_per_square"] == 500_000_000


def test_touch_tombstone_returns_none_when_absent(repo):
    assert asyncio.run(repo.touch_tombstone("tok1", "2026-09-20T10:00:00Z")) is None


def test_touch_tombstone_only_moves_forward(repo):
    _insert(repo, "old1", "2026-08-01T00:00:00Z")
    asyncio.run(repo.purge_expired(30))
    # purge سنگ قبر ساخت
    assert asyncio.run(repo.get_tombstone("old1")) is not None
    # زمان قدیمی‌تر تغییری نمی‌کند
    assert (
        asyncio.run(repo.touch_tombstone("old1", "2026-07-01T00:00:00Z"))
        == "2026-08-01T00:00:00+00:00"
    )
    # زمان تازه‌تر جایگزین می‌شود
    assert (
        asyncio.run(repo.touch_tombstone("old1", "2026-09-01T00:00:00Z"))
        == "2026-09-01T00:00:00+00:00"
    )
    tomb = asyncio.run(repo.get_tombstone("old1"))
    assert tomb["last_sort_date"] == "2026-09-01T00:00:00+00:00"


def test_matched_searches_purged_with_ad(repo):
    ad_id = _insert(repo, "old1", "2026-01-01T00:00:00Z")
    asyncio.run(repo.record_search_match(ad_id, "s1"))
    asyncio.run(repo.purge_expired(30))
    assert asyncio.run(repo.get_ad_by_token("old1")) is None
    assert asyncio.run(repo.get_matched_searches(ad_id)) == []

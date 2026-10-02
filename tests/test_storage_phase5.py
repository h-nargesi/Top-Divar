"""تست ذخیرهٔ نتیجهٔ امتیاز (مرحلهٔ ۵) — ستون‌های score/score_breakdown."""

import asyncio
import json

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


def test_get_pending_ads_oldest_first(repo):
    id_a = _insert(repo, "a", "2026-09-20T10:00:00Z")
    id_b = _insert(repo, "b", "2026-09-21T10:00:00Z")
    _insert(repo, "c", "2026-09-22T10:00:00Z")
    asyncio.run(repo.set_scoring_state("b", "scored"))
    pending = asyncio.run(repo.get_pending_ads())
    assert [row["token"] for row in pending] == ["a", "c"]
    asyncio.run(repo.store_score("c", 10, "[]"))
    pending = asyncio.run(repo.get_pending_ads())
    assert [row["token"] for row in pending] == ["a"]


def test_store_score_sets_state_and_columns(repo):
    _insert(repo, "x", "2026-09-20T10:00:00Z")
    breakdown = json.dumps([{"label": "پارکینگ", "points": 5}], ensure_ascii=False)
    assert asyncio.run(repo.store_score("x", 65, breakdown)) is True
    row = asyncio.run(repo.get_ad_by_token("x"))
    assert row["scoring_state"] == "scored"
    assert row["score"] == 65
    assert json.loads(row["score_breakdown"]) == [{"label": "پارکینگ", "points": 5}]


def test_store_score_rejects_bad_values(repo):
    _insert(repo, "x", "2026-09-20T10:00:00Z")
    with pytest.raises(StorageError):
        asyncio.run(repo.store_score("x", 1.5))
    with pytest.raises(StorageError):
        asyncio.run(repo.store_score("x", 10, {"not": "str"}))


def test_store_score_missing_token_returns_false(repo):
    assert asyncio.run(repo.store_score("ghost", 10, "[]")) is False


def test_new_ad_has_no_score_until_scored(repo):
    _insert(repo, "x", "2026-09-20T10:00:00Z")
    row = asyncio.run(repo.get_ad_by_token("x"))
    assert row["scoring_state"] == "pending"
    assert row["score"] is None
    assert row["score_breakdown"] is None


def test_refresh_ad_clears_stale_score(repo):
    _insert(repo, "x", "2026-09-20T10:00:00Z")
    asyncio.run(repo.store_score("x", 65, '[{"label":"پارکینگ","points":5}]'))
    asyncio.run(
        repo.refresh_ad("x", {"sort_date": "2026-09-25T08:00:00Z", "price": 2_000})
    )
    row = asyncio.run(repo.get_ad_by_token("x"))
    assert row["scoring_state"] == "pending"
    assert row["score"] is None
    assert row["score_breakdown"] is None

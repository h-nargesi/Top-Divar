import asyncio

import pytest

from top_divar.storage import (
    DuplicateTokenError,
    DuplicateUsernameError,
    SqliteRepository,
    StorageError,
)


@pytest.fixture()
def repo(tmp_path):
    repository = SqliteRepository(tmp_path / "db.sqlite3")
    yield repository
    repository.close()


def test_insert_and_get_ad_roundtrip(repo):
    ad_id = asyncio.run(
        repo.insert_ad(
            "gapa1FMk",
            "2026-09-22T17:19:00Z",
            title="آپارتمان ۵۵ متری پونک",
            price=12_900_000_000,
            price_per_square=234_500_000,
            size=55,
            rooms=2,
            construction_year=1403,
            building_age=2,
            floor=3,
            total_floors=8,
            has_parking=True,
            has_elevator=True,
            has_warehouse=False,
            district="پونک",
            city="تهران",
            is_promoted=False,
            image_count=6,
            raw_json='{"widget": 1}',
        )
    )
    assert isinstance(ad_id, int)
    ad = asyncio.run(repo.get_ad_by_token("gapa1FMk"))
    assert ad["id"] == ad_id
    assert ad["title"] == "آپارتمان ۵۵ متری پونک"
    assert ad["price"] == 12_900_000_000
    assert ad["has_parking"] == 1
    assert ad["has_warehouse"] == 0
    assert ad["scoring_state"] == "pending"
    assert ad["sort_date"] == "2026-09-22T17:19:00+00:00"


def test_get_missing_ad_returns_none(repo):
    assert asyncio.run(repo.get_ad_by_token("nope")) is None


def test_duplicate_token_is_rejected_and_original_untouched(repo):
    asyncio.run(
        repo.insert_ad("tok1", "2026-09-01T00:00:00+00:00", title="اول")
    )
    with pytest.raises(DuplicateTokenError) as excinfo:
        asyncio.run(
            repo.insert_ad("tok1", "2026-09-02T00:00:00+00:00", title="دوم")
        )
    assert "توکن" in str(excinfo.value)
    ad = asyncio.run(repo.get_ad_by_token("tok1"))
    assert ad["title"] == "اول"
    assert ad["sort_date"] == "2026-09-01T00:00:00+00:00"


def test_insert_ad_rejects_invalid_values(repo):
    with pytest.raises(StorageError):
        asyncio.run(repo.insert_ad("", "2026-09-01T00:00:00+00:00"))
    with pytest.raises(StorageError):
        asyncio.run(
            repo.insert_ad("tok1", "2026-09-01T00:00:00+00:00", scoring_state="bogus")
        )
    with pytest.raises(StorageError):
        asyncio.run(repo.insert_ad("tok1", "not-a-date"))
    with pytest.raises(StorageError):
        asyncio.run(repo.insert_ad("tok1", "2026-09-01T00:00:00+00:00", price="cheap"))


def test_scoring_state_transitions(repo):
    asyncio.run(repo.insert_ad("tok1", "2026-09-01T00:00:00+00:00"))
    assert asyncio.run(repo.set_scoring_state("tok1", "scored")) is True
    ad = asyncio.run(repo.get_ad_by_token("tok1"))
    assert ad["scoring_state"] == "scored"
    assert asyncio.run(repo.set_scoring_state("missing", "scored")) is False
    with pytest.raises(StorageError):
        asyncio.run(repo.set_scoring_state("tok1", "bogus"))


def test_watermark_missing_then_set_and_monotonic_update(repo):
    assert asyncio.run(repo.get_watermark("s1")) is None
    effective = asyncio.run(
        repo.update_watermark("s1", "2026-09-22T17:19:00Z")
    )
    assert effective == "2026-09-22T17:19:00+00:00"
    assert asyncio.run(repo.get_watermark("s1")) == "2026-09-22T17:19:00+00:00"

    newer = asyncio.run(
        repo.update_watermark("s1", "2026-09-23T09:00:00+00:00")
    )
    assert newer == "2026-09-23T09:00:00+00:00"

    older = asyncio.run(
        repo.update_watermark("s1", "2026-09-20T00:00:00+00:00")
    )
    assert older == "2026-09-23T09:00:00+00:00"
    assert asyncio.run(repo.get_watermark("s1")) == "2026-09-23T09:00:00+00:00"


def test_watermarks_are_per_search(repo):
    asyncio.run(repo.update_watermark("s1", "2026-09-22T00:00:00+00:00"))
    asyncio.run(repo.update_watermark("s2", "2026-09-23T00:00:00+00:00"))
    assert asyncio.run(repo.get_watermark("s1")) == "2026-09-22T00:00:00+00:00"
    assert asyncio.run(repo.get_watermark("s2")) == "2026-09-23T00:00:00+00:00"


def test_users_crud_and_case_insensitive_uniqueness(repo):
    user_id = asyncio.run(repo.add_user("ryan", 12345))
    assert isinstance(user_id, int)
    user = asyncio.run(repo.get_user("ryan"))
    assert user["chat_id"] == 12345
    assert asyncio.run(repo.get_user("RYAN"))["id"] == user_id
    by_chat = asyncio.run(repo.get_user_by_chat_id(12345))
    assert by_chat["username"] == "ryan"
    with pytest.raises(DuplicateUsernameError):
        asyncio.run(repo.add_user("Ryan", 67890))
    assert asyncio.run(repo.remove_user("RYAN")) is True
    assert asyncio.run(repo.get_user("ryan")) is None
    assert asyncio.run(repo.remove_user("ryan")) is False
    with pytest.raises(StorageError):
        asyncio.run(repo.add_user("bob", "not-an-int"))


def test_delivery_rows_statuses_and_tracking(repo):
    ad_id = asyncio.run(repo.insert_ad("tok1", "2026-09-01T00:00:00+00:00"))
    created = asyncio.run(
        repo.create_delivery_rows(
            ad_id, [("telegram", "12345"), ("email", "user@example.com")]
        )
    )
    assert created == 2
    rows = asyncio.run(repo.get_deliveries(ad_id))
    assert [row["status"] for row in rows] == ["pending", "pending"]
    assert all(row["attempts"] == 0 for row in rows)

    telegram_row = rows[0]
    assert asyncio.run(repo.mark_delivery(telegram_row["id"], "sent")) is True
    rows = asyncio.run(repo.get_deliveries(ad_id))
    assert rows[0]["status"] == "sent"
    assert rows[0]["attempts"] == 1

    long_error = "x" * 2000
    assert asyncio.run(
        repo.mark_delivery(
            rows[1]["id"],
            "dead",
            error=long_error,
        )
    )
    rows = asyncio.run(repo.get_deliveries(ad_id))
    assert rows[1]["status"] == "dead"
    assert rows[1]["last_error"] == "x" * 500

    assert asyncio.run(repo.mark_delivery(999999, "sent")) is False
    with pytest.raises(StorageError):
        asyncio.run(repo.mark_delivery(rows[0]["id"], "bogus"))


def test_duplicate_delivery_row_is_rejected(repo):
    ad_id = asyncio.run(repo.insert_ad("tok1", "2026-09-01T00:00:00+00:00"))
    asyncio.run(repo.create_delivery_rows(ad_id, [("telegram", "12345")]))
    with pytest.raises(StorageError) as excinfo:
        asyncio.run(repo.create_delivery_rows(ad_id, [("telegram", "12345")])
        )
    assert "تحویل" in str(excinfo.value)


def test_delivery_requires_existing_ad(repo):
    with pytest.raises(StorageError):
        asyncio.run(repo.create_delivery_rows(999, [("telegram", "12345")]))


def test_concurrent_distinct_inserts_all_succeed(repo):
    async def scenario():
        tasks = [
            repo.insert_ad(f"tok{i}", f"2026-09-01T00:00:{i:02d}+00:00")
            for i in range(30)
        ]
        return await asyncio.gather(*tasks)

    ids = asyncio.run(scenario())
    assert len(set(ids)) == 30


def test_concurrent_duplicate_inserts_exactly_one_wins(repo):
    async def scenario():
        tasks = [
            repo.insert_ad("same-token", "2026-09-01T00:00:00+00:00")
            for _ in range(10)
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

    results = asyncio.run(scenario())
    successes = [result for result in results if not isinstance(result, Exception)]
    failures = [result for result in results if isinstance(result, Exception)]
    assert len(successes) == 1
    assert len(failures) == 9
    assert all(isinstance(failure, DuplicateTokenError) for failure in failures)

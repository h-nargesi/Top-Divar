import asyncio
import logging

import pytest

from top_divar.core.detector import poll_search
from top_divar.core.settings import PollingSettings
from top_divar.divar.errors import DivarUnavailableError
from top_divar.divar.models import AdCard, PostDetail, SearchPage
from top_divar.storage import SqliteRepository


class FakeFetcher:
    """صفحه‌ها را به‌ترتیب تحویل می‌دهد و درخواست‌ها را ثبت می‌کند."""

    def __init__(self, pages, details=None):
        self.pages = list(pages)
        self.details = details or {}
        self.search_calls = []      # (pagination_data)
        self.detail_calls = []

    async def search(self, search, *, pagination_data=None):
        self.search_calls.append(pagination_data)
        if not self.pages:
            raise AssertionError("صفحهٔ بیشتری از فیکسچر خواسته شد")
        return self.pages.pop(0)

    async def get_post(self, token):
        self.detail_calls.append(token)
        detail = self.details.get(token)
        if detail is None:
            raise DivarUnavailableError(f"جزئیات {token} در دسترس نیست")
        return detail


def card(token, sort_date, **overrides):
    fields = {
        "token": token,
        "title": f"آگهی {token}",
        "price": 1_000_000_000,
        "district": "پونک",
        "city": "تهران",
        "sort_date": sort_date,
    }
    fields.update(overrides)
    return AdCard(**fields)


def detail_for(token, **overrides):
    fields = {"token": token, "size": 70, "price": 2_000_000_000}
    fields.update(overrides)
    return PostDetail(**fields)


def page(cards, *, has_next_page=False, pagination_data=None):
    return SearchPage(
        cards=list(cards),
        has_next_page=has_next_page,
        pagination_data=pagination_data or {"page": 2},
    )


@pytest.fixture()
def repo(tmp_path):
    repository = SqliteRepository(tmp_path / "db.sqlite3")
    yield repository
    repository.close()


def _ad_count(repo):
    return asyncio.run(
        repo._call(lambda conn: conn.execute("SELECT COUNT(*) FROM ads").fetchone()[0])
    )


def test_first_poll_processes_only_first_page(repo):
    page1 = page(
        [
            card("a1", "2026-09-20T10:30:00Z"),
            card("a2", "2026-09-20T10:00:00Z"),
        ],
        has_next_page=True,
    )
    page2 = page([card("a3", "2026-09-19T09:00:00Z")])
    fetcher = FakeFetcher([page1, page2], details={"a1": detail_for("a1")})
    outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}))
    assert outcome.first_poll is True
    assert fetcher.search_calls == [None]  # صفحهٔ دوم هرگز خواسته نشد
    assert outcome.pages_fetched == 1
    assert outcome.new_ads == 2
    assert outcome.details_failed == 1  # جزئیات a2 در دسترس نبود
    assert asyncio.run(repo.get_watermark("s1")) == "2026-09-20T10:30:00+00:00"
    assert asyncio.run(repo.get_ad_by_token("a3")) is None


def test_subsequent_poll_paginates_until_watermark(repo):
    asyncio.run(repo.update_watermark("s1", "2026-09-20T10:00:00Z"))
    asyncio.run(
        repo.insert_ad("old1", "2026-09-20T10:00:00Z", title="قدیمی")
    )
    page1 = page(
        [
            card("n1", "2026-09-20T10:30:00Z"),
            card("old1", "2026-09-20T10:00:00Z"),  # هم‌زمان با خط مرز → پردازش می‌شود
        ],
        has_next_page=True,
    )
    page2 = page([card("old2", "2026-09-20T09:00:00Z")], has_next_page=True)
    fetcher = FakeFetcher([page1, page2], details={"n1": detail_for("n1")})
    outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}))
    assert outcome.first_poll is False
    assert fetcher.search_calls == [None, {"page": 2}]
    assert outcome.pages_fetched == 2
    assert outcome.watermark_reached is True
    # n1 تازه است؛ old1 تکراری؛ old2 زیر خط مرز است ولی توکنش دیده نشده
    # و تشخیص تکراری همیشه با token است → جدید ثبت می‌شود (بخش ۹.۳)
    assert outcome.new_ads == 2
    assert outcome.duplicates == 1
    assert asyncio.run(repo.get_watermark("s1")) == "2026-09-20T10:30:00+00:00"


def test_pagination_stops_at_page_cap_with_warning(repo, caplog):
    asyncio.run(repo.update_watermark("s1", "2026-09-01T00:00:00Z"))
    pages = [
        page([card(f"n{i}", f"2026-09-20T10:{i:02d}:00Z")], has_next_page=True)
        for i in range(5)
    ]
    fetcher = FakeFetcher(pages)
    settings = PollingSettings(max_pages_per_poll=2)
    with caplog.at_level(logging.WARNING, logger="top_divar"):
        outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}, settings))
    assert outcome.pages_fetched == 2
    assert outcome.page_cap_hit is True
    assert outcome.watermark_reached is False
    assert any("سقف" in record.message for record in caplog.records)


def test_stops_when_no_next_page(repo):
    asyncio.run(repo.update_watermark("s1", "2026-09-01T00:00:00Z"))
    single = page([card("n1", "2026-09-20T10:00:00Z")], has_next_page=False)
    fetcher = FakeFetcher([single, single], details={"n1": detail_for("n1")})
    outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}))
    assert outcome.last_page_reached is True
    assert outcome.pages_fetched == 1
    assert outcome.new_ads == 1


def test_duplicate_ad_is_not_stored_again(repo):
    asyncio.run(repo.update_watermark("s1", "2026-09-20T10:00:00Z"))
    asyncio.run(
        repo.insert_ad(
            "dup1",
            "2026-09-20T10:00:00Z",
            title="اصل",
            district="پونک",
        )
    )
    before = _ad_count(repo)
    fetcher = FakeFetcher(
        [page([card("dup1", "2026-09-20T10:00:00Z")])],
        details={"dup1": detail_for("dup1")},
    )
    outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}))
    assert _ad_count(repo) == before
    assert outcome.duplicates == 1
    assert outcome.new_ads == 0
    assert fetcher.detail_calls == []  # تکراری جزئیات نمی‌گیرد


def test_bump_seen_as_duplicate_with_newer_time(repo):
    asyncio.run(repo.update_watermark("s1", "2026-09-20T10:00:00Z"))
    ad_id = asyncio.run(
        repo.insert_ad(
            "bump1",
            "2026-09-20T10:00:00Z",
            title="قبل از نردبان",
            price=1_000,
            size=50,
        )
    )
    fetcher = FakeFetcher(
        [page([card("bump1", "2026-09-22T06:00:00Z", is_promoted=True)])],
        details={"bump1": detail_for("bump1", size=80, price=5_000)},
    )
    outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}))
    # نردبان = همان ردیف، با زمان تازه‌تر — نه ردیف جدید
    assert _ad_count(repo) == 1
    row = asyncio.run(repo.get_ad_by_token("bump1"))
    assert row["id"] == ad_id
    assert row["sort_date"] == "2026-09-22T06:00:00+00:00"
    assert row["size"] == 80
    assert row["price"] == 5_000
    assert row["is_promoted"] == 1
    assert row["scoring_state"] == "pending"
    assert fetcher.detail_calls == ["bump1"]
    assert [event.token for event in outcome.bumps] == ["bump1"]
    assert outcome.new_ads == 0
    assert outcome.duplicates == 0
    assert asyncio.run(repo.get_watermark("s1")) == "2026-09-22T06:00:00+00:00"


def test_bump_without_details_keeps_old_detail_fields(repo):
    asyncio.run(repo.update_watermark("s1", "2026-09-20T10:00:00Z"))
    asyncio.run(
        repo.insert_ad(
            "bump2",
            "2026-09-20T10:00:00Z",
            title="قبل",
            size=97,
            price_per_square=500_000_000,
        )
    )
    fetcher = FakeFetcher([page([card("bump2", "2026-09-21T10:00:00Z")])])
    outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}))
    row = asyncio.run(repo.get_ad_by_token("bump2"))
    assert row["sort_date"] == "2026-09-21T10:00:00+00:00"
    assert row["size"] == 97
    assert row["price_per_square"] == 500_000_000
    assert outcome.details_failed == 1
    assert len(outcome.bumps) == 1


def test_new_ad_records_search_match(repo):
    fetcher = FakeFetcher(
        [page([card("m1", "2026-09-20T10:00:00Z")])],
        details={"m1": detail_for("m1")},
    )
    asyncio.run(poll_search(fetcher, repo, {"id": "sA"}))
    ad = asyncio.run(repo.get_ad_by_token("m1"))
    assert asyncio.run(repo.get_matched_searches(ad["id"])) == ["sA"]


def test_second_search_only_completes_match_list(repo):
    fetcher = FakeFetcher(
        [page([card("m1", "2026-09-20T10:00:00Z")])],
        details={"m1": detail_for("m1")},
    )
    asyncio.run(poll_search(fetcher, repo, {"id": "sA"}))
    ad = asyncio.run(repo.get_ad_by_token("m1"))
    fetcher_b = FakeFetcher(
        [page([card("m1", "2026-09-20T10:00:00Z")])],
        details={"m1": detail_for("m1")},
    )
    outcome = asyncio.run(poll_search(fetcher_b, repo, {"id": "sB"}))
    assert _ad_count(repo) == 1
    assert fetcher_b.detail_calls == []  # جزئیات دوباره گرفته نمی‌شود (بخش ۹.۱۰)
    assert outcome.matches_added == 1
    assert outcome.new_ads == 0
    assert outcome.duplicates == 1
    assert asyncio.run(repo.get_matched_searches(ad["id"])) == ["sA", "sB"]


def test_tombstoned_token_is_never_new_again(repo):
    # آگهی قدیمی را purge می‌کنیم تا سنگ قبر بماند (ADR-0001)
    asyncio.run(repo.insert_ad("gone1", "2026-01-01T00:00:00Z"))
    asyncio.run(repo.purge_expired(30))
    assert asyncio.run(repo.get_tombstone("gone1")) is not None
    fetcher = FakeFetcher(
        [page([card("gone1", "2026-09-20T10:00:00Z")])],
        details={"gone1": detail_for("gone1")},
    )
    outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}))
    assert outcome.new_ads == 0
    assert outcome.duplicates == 1
    assert asyncio.run(repo.get_ad_by_token("gone1")) is None
    assert fetcher.detail_calls == []


def test_fetch_post_detail_disabled_stores_card_only(repo):
    fetcher = FakeFetcher(
        [page([card("d1", "2026-09-20T10:00:00Z")])],
        details={"d1": detail_for("d1")},
    )
    settings = PollingSettings(fetch_post_detail=False)
    outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}, settings))
    assert fetcher.detail_calls == []
    row = asyncio.run(repo.get_ad_by_token("d1"))
    assert row is not None
    assert row["size"] is None
    assert row["price"] == 1_000_000_000  # قیمت کارت search


def test_watermark_never_moves_backwards(repo):
    asyncio.run(repo.update_watermark("s1", "2026-09-25T00:00:00Z"))
    fetcher = FakeFetcher([page([card("o1", "2026-09-20T10:00:00Z")])])
    outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}))
    assert outcome.watermark == "2026-09-20T10:00:00+00:00"
    assert asyncio.run(repo.get_watermark("s1")) == "2026-09-25T00:00:00+00:00"


def test_card_without_sort_date_is_skipped(repo):
    fetcher = FakeFetcher(
        [page([card("nosort", None), card("ok1", "2026-09-20T10:00:00Z")])]
    )
    outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}))
    assert asyncio.run(repo.get_ad_by_token("nosort")) is None
    assert outcome.new_ads == 1
    assert asyncio.run(repo.get_watermark("s1")) == "2026-09-20T10:00:00+00:00"


def test_empty_first_page_keeps_no_watermark(repo):
    fetcher = FakeFetcher([SearchPage(cards=[], no_result=True)])
    outcome = asyncio.run(poll_search(fetcher, repo, {"id": "s1"}))
    assert outcome.first_poll is True
    assert outcome.watermark is None
    assert asyncio.run(repo.get_watermark("s1")) is None

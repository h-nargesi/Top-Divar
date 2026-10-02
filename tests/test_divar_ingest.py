import asyncio
import json
import pathlib

import pytest

from top_divar.divar.errors import DivarUnavailableError
from top_divar.divar.ingest import build_ad_record, ingest_search_page
from top_divar.divar.models import AdCard, PostDetail, SearchPage
from top_divar.storage import SqliteRepository

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


class FakeFetcher:
    def __init__(self, page, details):
        self.page = page
        self.details = details
        self.detail_calls = []

    async def search(self, search, *, pagination_data=None):
        return self.page

    async def get_post(self, token):
        self.detail_calls.append(token)
        detail = self.details.get(token)
        if detail is None:
            raise DivarUnavailableError(f"جزئیات {token} در دسترس نیست")
        if isinstance(detail, Exception):
            raise detail
        return detail


@pytest.fixture()
def repo(tmp_path):
    repository = SqliteRepository(tmp_path / "db.sqlite3")
    yield repository
    repository.close()


def _load_page():
    payload = json.loads((FIXTURES / "search_page1_response.json").read_text(encoding="utf-8"))
    from top_divar.divar.parsing import parse_search_page

    return parse_search_page(payload)


def _load_detail(token):
    name = {"gap5-Twe": "post_detail_gap5_twe.json", "gammaxvi": "post_detail_gammaxvi.json"}[token]
    payload = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
    from top_divar.divar.parsing import parse_post_detail

    return parse_post_detail(payload)


def _detail_for(token):
    detail = _load_detail("gammaxvi" if token == "gammaxvi" else "gap5-Twe")
    detail.token = token
    return detail


class TestIngestSearchPage:
    def test_stores_all_cards_with_details(self, repo):
        page = _load_page()
        details = {card.token: _detail_for(card.token) for card in page.cards[:2]}
        fetcher = FakeFetcher(page, details)
        result = asyncio.run(ingest_search_page(fetcher, repo, {"id": "s1"}))
        assert result.cards == 8
        assert result.stored == 8
        assert result.duplicates == 0
        assert result.details_failed == 6
        first = asyncio.run(repo.get_ad_by_token(page.cards[0].token))
        assert first is not None
        assert first["scoring_state"] == "pending"

    def test_merged_fields_prefer_detail(self, repo):
        page = _load_page()
        target = page.cards[0]
        fetcher = FakeFetcher(page, {target.token: _detail_for(target.token)})
        asyncio.run(ingest_search_page(fetcher, repo, {"id": "s1"}))
        row = asyncio.run(repo.get_ad_by_token(target.token))
        detail = _detail_for(target.token)
        # محله از جزئیات ارجح است (بخش ۷.۴)
        assert row["district"] == detail.district
        assert row["size"] == detail.size
        assert row["price"] == detail.price
        assert row["price_per_square"] == detail.price_per_square
        assert row["building_age"] == detail.building_age
        assert row["published_at"] == detail.published_at
        assert row["title"] == target.title
        assert row["is_promoted"] == 0
        raw = json.loads(row["raw_json"])
        assert "search_card" in raw and "post_detail" in raw

    def test_detail_failure_stores_card_only(self, repo):
        page = _load_page()
        target = page.cards[0]
        fetcher = FakeFetcher(page, {})  # همهٔ جزئیات شکست می‌خورند
        result = asyncio.run(ingest_search_page(fetcher, repo, {"id": "s1"}))
        row = asyncio.run(repo.get_ad_by_token(target.token))
        assert row["size"] is None
        assert row["district"] == target.district  # از کارت
        assert row["price"] == target.price
        raw = json.loads(row["raw_json"])
        assert "post_detail" not in raw
        assert result.details_failed == 8

    def test_duplicate_tokens_are_skipped(self, repo):
        page = _load_page()
        fetcher = FakeFetcher(page, {})
        first = asyncio.run(ingest_search_page(fetcher, repo, {"id": "s1"}))
        second = asyncio.run(ingest_search_page(fetcher, repo, {"id": "s1"}))
        assert first.stored == 8
        assert second.stored == 0
        assert second.duplicates == 8

    def test_card_without_sort_date_is_skipped(self, repo):
        card = AdCard(token="nosort", title="بدون تاریخ", price=1, district="پونک", city="تهران")
        page = SearchPage(cards=[card])
        fetcher = FakeFetcher(page, {})
        result = asyncio.run(ingest_search_page(fetcher, repo, {"id": "s1"}))
        assert result.stored == 0
        assert asyncio.run(repo.get_ad_by_token("nosort")) is None

    def test_empty_page(self, repo):
        fetcher = FakeFetcher(SearchPage(cards=[], no_result=True), {})
        result = asyncio.run(ingest_search_page(fetcher, repo, {"id": "s1"}))
        assert result.cards == 0
        assert result.stored == 0


class TestBuildAdRecord:
    def test_explicit_null_price_from_detail(self):
        card = AdCard(token="t", price=1000, sort_date="2026-09-15T00:00:00Z")
        detail = PostDetail(token="t", price=None, price_agreed=True)
        record = build_ad_record(card, detail)
        assert record["price"] is None

    def test_card_price_used_when_detail_silent(self):
        card = AdCard(token="t", price=1000, sort_date="2026-09-15T00:00:00Z")
        record = build_ad_record(card, None)
        assert record["price"] == 1000
        assert record["building_age"] is None

    def test_district_falls_back_to_card(self):
        card = AdCard(token="t", district="پونک", city="تهران", sort_date="2026-09-15T00:00:00Z")
        detail = PostDetail(token="t", district=None, city=None)
        record = build_ad_record(card, detail)
        assert record["district"] == "پونک"

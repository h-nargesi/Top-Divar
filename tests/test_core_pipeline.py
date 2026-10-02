"""تست خط لولهٔ امتیازدهی دسته (مرحلهٔ ۵) — architecture.md «جریان داده»."""

import asyncio
import json

import pytest

from top_divar.core.detector import poll_search
from top_divar.core.pipeline import resolve_block_name, score_pending_ads
from top_divar.divar.models import AdCard, PostDetail, SearchPage
from top_divar.storage import SqliteRepository

RULES = [
    {"field": "price", "tiers": [
        {"op": "<=", "value": 12_000_000_000, "points": 30},
        {"op": "<=", "value": 13_500_000_000, "points": 15},
    ]},
    {"field": "has_elevator", "op": "==", "value": True, "points": 30},
    {"field": "price", "op": "==", "value": None, "points": -10},
]

CONFIG = {
    "searches": [
        {"id": "s1", "scoring_ref": "default"},
        {"id": "s2", "scoring_ref": "strict"},
    ],
    "scoring": {
        "default": {"min_score": 60, "rules": RULES},
        "strict": {"min_score": 90, "rules": RULES},
    },
}


@pytest.fixture()
def repo(tmp_path):
    repository = SqliteRepository(tmp_path / "db.sqlite3")
    yield repository
    repository.close()


def _insert(repo, token, *, sort_date="2026-09-20T10:00:00Z", **overrides):
    fields = {
        "price": 12_000_000_000,
        "has_elevator": True,
        "raw_json": json.dumps({"search_card": {}}),
    }
    fields.update(overrides)
    ad_id = asyncio.run(repo.insert_ad(token, sort_date, **fields))
    for search_id in ("s1",):
        asyncio.run(repo.record_search_match(ad_id, search_id))
    return ad_id


def test_batch_scores_fake_ads_pass_and_fail(repo):
    # ممتاز: ۳۰ (قیمت) + ۳۰ (آسانسور) = ۶۰ >= حد ۶۰
    _insert(repo, "good", price=11_500_000_000)
    # زیر حد: ۱۵ + ۳۰ = ۴۵ < ۶۰
    _insert(repo, "weak", price=13_000_000_000)
    outcome = asyncio.run(score_pending_ads(repo, CONFIG))
    assert outcome.scored == 2
    assert outcome.tokens_notable == ["good"]

    good = asyncio.run(repo.get_ad_by_token("good"))
    weak = asyncio.run(repo.get_ad_by_token("weak"))
    assert good["scoring_state"] == "scored" and good["score"] == 60
    assert weak["scoring_state"] == "scored" and weak["score"] == 45
    breakdown = json.loads(good["score_breakdown"])
    assert {"label": "آسانسور", "points": 30} in breakdown
    assert {"label": "قیمت≤۱۲B", "points": 30} in breakdown


def test_below_threshold_creates_no_delivery_rows(repo):
    _insert(repo, "weak", price=13_000_000_000)
    asyncio.run(score_pending_ads(repo, CONFIG))
    ad_id = asyncio.run(repo.get_ad_by_token("weak"))["id"]
    assert asyncio.run(repo.get_deliveries(ad_id)) == []


def test_block_resolved_from_first_matched_search(repo):
    # آگهی مشترک: اولین جستجوی مچ (s1 → default) تعیین‌کننده است (ADR-0007)
    ad_id = _insert(repo, "shared", price=11_500_000_000)
    asyncio.run(repo.record_search_match(ad_id, "s2"))
    asyncio.run(score_pending_ads(repo, CONFIG))
    row = asyncio.run(repo.get_ad_by_token("shared"))
    assert row["score"] == 60  # با بلوک default ممتاز است

    # فقط s2 (strict، حد ۹۰): ۶۰ < ۹۰ → ممتاز نیست
    _insert(repo, "only-s2", price=11_500_000_000)
    ad2 = asyncio.run(repo.get_ad_by_token("only-s2"))
    asyncio.run(
        repo._call(
            lambda conn: conn.execute(
                "DELETE FROM matched_searches WHERE ad_id = ?", (ad2["id"],)
            )
        )
    )
    asyncio.run(repo.record_search_match(ad2["id"], "s2"))
    asyncio.run(score_pending_ads(repo, CONFIG))
    row2 = asyncio.run(repo.get_ad_by_token("only-s2"))
    assert row2["score"] == 60
    outcome = asyncio.run(score_pending_ads(repo, CONFIG))
    # دوباره اجرا شود چیزی عوض نمی‌شود؛ notable فقط از نتیجهٔ تازه می‌آید
    assert outcome.scored == 0


def test_startup_reconcile_scores_leftover_pending(repo):
    _insert(repo, "leftover", price=11_500_000_000)
    # شبیه اجرای قبل از کرش: آگهی pending مانده؛ startup همان‌جا امتیاز می‌دهد
    outcome = asyncio.run(score_pending_ads(repo, CONFIG))
    assert outcome.scored == 1
    row = asyncio.run(repo.get_ad_by_token("leftover"))
    assert row["scoring_state"] == "scored"


def test_agreed_price_penalty_applies_in_batch(repo):
    _insert(
        repo,
        "agreed",
        price=None,
        raw_json=json.dumps({"search_card": {}, "price_agreed": True}),
    )
    asyncio.run(score_pending_ads(repo, CONFIG))
    row = asyncio.run(repo.get_ad_by_token("agreed"))
    # ۳۰ (آسانسور) − ۱۰ (توافقی) = ۲۰
    assert row["score"] == 20
    assert {"label": "قیمت توافقی", "points": -10} in json.loads(
        row["score_breakdown"]
    )


def test_missing_block_leaves_ad_pending(repo):
    _insert(repo, "orphan")
    broken = {
        "searches": [{"id": "s1", "scoring_ref": "ghost"}],
        "scoring": {"default": {"min_score": 60, "rules": RULES}},
    }
    outcome = asyncio.run(score_pending_ads(repo, broken))
    assert outcome.scored == 0
    assert outcome.unresolved == 1
    row = asyncio.run(repo.get_ad_by_token("orphan"))
    assert row["scoring_state"] == "pending"


def test_bump_resets_and_rescores(repo):
    _insert(repo, "bump", price=11_500_000_000)
    asyncio.run(score_pending_ads(repo, CONFIG))
    assert asyncio.run(repo.get_ad_by_token("bump"))["score"] == 60
    asyncio.run(
        repo.refresh_ad(
            "bump",
            {
                "sort_date": "2026-09-25T08:00:00Z",
                "price": 20_000_000_000,
                "has_elevator": True,
                "raw_json": json.dumps({"search_card": {}}),
            },
        )
    )
    row = asyncio.run(repo.get_ad_by_token("bump"))
    assert row["scoring_state"] == "pending" and row["score"] is None
    asyncio.run(score_pending_ads(repo, CONFIG))
    assert asyncio.run(repo.get_ad_by_token("bump"))["score"] == 30  # فقط آسانسور


def test_resolve_block_name_defaults():
    assert resolve_block_name([], {}) == "default"
    assert resolve_block_name(["ghost"], {}) == "default"
    assert resolve_block_name(["s1"], {"s1": {"id": "s1"}}) == "default"
    assert resolve_block_name(["s1"], {"s1": {"id": "s1", "scoring_ref": "strict"}}) == "strict"
    assert resolve_block_name(["a", "b"], {"a": {}, "b": {"scoring_ref": "strict"}}) == "default"


class FakeFetcher:
    async def search(self, search, *, pagination_data=None):
        return SearchPage(
            cards=[
                AdCard(
                    token="live1",
                    title="آپارتمان ۵۵ متری پونک",
                    price=None,
                    price_agreed=True,
                    district="پونک",
                    city="تهران",
                    sort_date="2026-09-20T10:30:00Z",
                )
            ]
        )

    async def get_post(self, token):
        return PostDetail(
            token=token,
            size=55,
            rooms=2,
            price_per_square=234_500_000,
            has_elevator=True,
            has_parking=True,
        )


def test_two_phase_pipeline_from_poll_to_score(repo):
    """poll ذخیره می‌کند (pending) → دسته امتیاز می‌دهد؛ توافقی جریمه می‌گیرد."""
    config = {
        "searches": [{"id": "s1"}],
        "scoring": {
            "default": {
                "min_score": 40,
                "rules": RULES
                + [
                    {"field": "price_per_square", "op": "<=", "value": 280_000_000, "points": 20},
                    {"field": "has_parking", "op": "==", "value": True, "points": 5},
                ],
            }
        },
    }
    outcome = asyncio.run(poll_search(FakeFetcher(), repo, {"id": "s1"}))
    assert outcome.new_ads == 1
    row = asyncio.run(repo.get_ad_by_token("live1"))
    assert row["scoring_state"] == "pending"  # مرحلهٔ اول: فقط ذخیره

    batch = asyncio.run(score_pending_ads(repo, config))
    assert batch.scored == 1 and batch.tokens_notable == ["live1"]
    row = asyncio.run(repo.get_ad_by_token("live1"))
    # قیمت null صریح ماند (کارت توافقی بود و جزئیات قیمت کل نداشت):
    # ۳۰ (آسانسور) + ۲۰ (قیمت‌متری) + ۵ (پارکینگ) − ۱۰ (توافقی) = ۴۵
    assert row["score"] == 45
    labels = [item["label"] for item in json.loads(row["score_breakdown"])]
    assert "قیمت توافقی" in labels

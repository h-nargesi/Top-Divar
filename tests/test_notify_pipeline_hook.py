"""تست اتصال امتیاز → ردیف تحویل (مرحلهٔ ۶) و اعتبارسنجی notify."""

import asyncio
import json

from top_divar.config import validate_config
from top_divar.core.pipeline import score_pending_ads
from top_divar.notify import NotifySettings, plan_delivery_rows
from top_divar.storage import SqliteRepository

RULES = [
    {"field": "price", "tiers": [{"op": "<=", "value": 12_000_000_000, "points": 30}]},
    {"field": "has_elevator", "op": "==", "value": True, "points": 30},
]


def _config():
    return {
        "searches": [{"id": "s1", "label": "آپارتمان تهران"}],
        "scoring": {"default": {"min_score": 60, "rules": RULES}},
        "notify": {
            "channels": ["email"],
            "email": {"to": ["user@example.com"]},
        },
    }


def test_score_pending_ads_invokes_on_notable_only_for_notable(tmp_path):
    repo = SqliteRepository(tmp_path / "db.sqlite3")
    try:
        good = asyncio.run(
            repo.insert_ad(
                "good",
                "2026-09-20T10:00:00Z",
                price=11_000_000_000,
                has_elevator=True,
                raw_json=json.dumps({"search_card": {}}),
            )
        )
        asyncio.run(repo.record_search_match(good, "s1"))
        weak = asyncio.run(
            repo.insert_ad(
                "weak",
                "2026-09-20T10:00:00Z",
                price=20_000_000_000,
                has_elevator=True,
                raw_json=json.dumps({"search_card": {}}),
            )
        )
        asyncio.run(repo.record_search_match(weak, "s1"))

        seen = []

        async def on_notable(row):
            seen.append(row["token"])
            settings = NotifySettings.from_config(_config())
            await plan_delivery_rows(repo, settings, row["id"])

        outcome = asyncio.run(score_pending_ads(repo, _config(), on_notable=on_notable))
        assert outcome.tokens_notable == ["good"]
        assert seen == ["good"]  # زیر حد صدا زده نمی‌شود
        rows = asyncio.run(repo.get_deliveries(good))
        assert [row["recipient"] for row in rows] == ["user@example.com"]
        assert asyncio.run(repo.get_deliveries(weak)) == []
    finally:
        repo.close()


def test_validator_accepts_and_rejects_sweep_max_sends():
    base = {
        "searches": [
            {
                "id": "s",
                "city_ids": ["1"],
                "form_data": {"category": {"str": {"value": "apartment-sell"}}},
            }
        ],
        "scoring": {"default": {"min_score": 60}},
    }

    def with_notify(notify):
        config = json.loads(json.dumps(base))
        config["notify"] = {
            "channels": ["email"],
            "email": {
                "smtp": {"host": "smtp.example.com"},
                "to": ["user@example.com"],
            },
            **notify,
        }
        return config

    env = {"SMTP_PASSWORD": "x"}

    report = validate_config(
        with_notify({"sweep_max_sends": 25}),
        env,
    )
    assert report.ok

    report = validate_config(
        with_notify({"sweep_max_sends": 0}),
        env,
    )
    assert not report.ok
    assert any("sweep_max_sends" in error.message for error in report.errors)

    report = validate_config(
        with_notify({"sweep_max_sends": "many"}),
        env,
    )
    assert not report.ok

    report = validate_config(
        with_notify({"unknown_key": 1}),
        env,
    )
    assert report.ok  # کلید ناشناخته فقط هشدار است
    assert any("unknown_key" in warning.message for warning in report.warnings)

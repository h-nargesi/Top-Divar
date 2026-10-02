"""تست جاروی تحویل و برنامه‌ریز ردیف‌ها (مرحلهٔ ۶) — ADR-0010."""

import asyncio
import dataclasses
import datetime
import json

import pytest

from top_divar.notify import (
    BACKOFF_CAP_SECONDS,
    ETERNAL,
    RESURRECTABLE,
    TRANSIENT,
    DeliverySweeper,
    NotifySettings,
    SendError,
    compute_backoff_seconds,
    email_sender,
    plan_delivery_rows,
    resolve_recipients,
    telegram_sender,
)
from top_divar.notify.email import EmailNotifier
from top_divar.notify.settings import EmailSettings, SMTPSettings
from top_divar.notify.telegram import TelegramNotifier
from top_divar.storage import SqliteRepository
from top_divar.storage.timestamps import utc_now

# --- fixture مشترک ---------------------------------------------------------

RECIPIENTS_CONFIG = {
    "notify": {
        "channels": ["telegram", "email"],
        "retry_interval": "30m",
        "sweep_max_sends": 2,
        "email": {
            "smtp": {
                "host": "smtp.example.com",
                "port": 587,
                "encryption": "starttls",
                "username": "bot@example.com",
                "password_env": "SMTP_PASSWORD",
                "from": "Top Divar <bot@example.com>",
            },
            "to": ["user1@example.com", "user2@example.com"],
        },
    }
}


@pytest.fixture()
def repo(tmp_path):
    repository = SqliteRepository(tmp_path / "db.sqlite3")
    yield repository
    repository.close()


def _insert(repo, token, *, sort_date="2026-09-20T10:00:00Z", **overrides):
    fields = {
        "title": "آپارتمان ۵۵ متری پونک",
        "price": 12_000_000_000,
        "price_per_square": 234_500_000,
        "size": 55,
        "rooms": 2,
        "construction_year": 1403,
        "building_age": 2,
        "floor": 3,
        "total_floors": 8,
        "has_parking": True,
        "has_elevator": True,
        "has_warehouse": True,
        "district": "پونک",
        "city": "تهران",
        "published_at": "2026-09-13T13:49:00+00:00",
        "raw_json": json.dumps({"search_card": {}}, ensure_ascii=False),
    }
    fields.update(overrides)
    ad_id = asyncio.run(repo.insert_ad(token, sort_date, **fields))
    asyncio.run(
        repo.store_score(token, 65, '[{"label": "قیمت≤۱۳.۵B", "points": 15}]')
    )
    return ad_id


def _settings(**overrides):
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    return dataclasses.replace(settings, **overrides)


class FakeSender:
    """ارسال‌کنندهٔ ضبط‌شده با خطای قابل‌تنظیم به‌ازای گیرنده."""

    def __init__(self, failures=None):
        self.sent = []
        self.failures = dict(failures or {})

    async def __call__(self, ad, recipient, label):
        failure = self.failures.get(recipient)
        if failure is not None:
            raise failure
        self.sent.append((recipient, label, ad["token"]))


def _sweeper(repo, senders, settings=None):
    return DeliverySweeper(
        repo,
        senders,
        settings or NotifySettings.from_config(RECIPIENTS_CONFIG),
        searches_by_id={
            "s1": {"id": "s1", "label": "آپارتمان تهران"},
            "s2": {"id": "s2"},
        },
        pauses={"telegram": 0, "email": 0},
        sleeper=_no_sleep,
    )


async def _no_sleep(seconds):
    return None


# --- برنامه‌ریز -------------------------------------------------------------


def test_resolve_recipients_telegram_users_and_email_config(repo):
    asyncio.run(repo.add_user("ali", 111))
    asyncio.run(repo.add_user("sara", 222))
    recipients = asyncio.run(
        resolve_recipients(repo, NotifySettings.from_config(RECIPIENTS_CONFIG))
    )
    assert sorted(recipients["telegram"]) == ["111", "222"]
    assert recipients["email"] == ["user1@example.com", "user2@example.com"]


def test_plan_delivery_rows_before_sending(repo):
    asyncio.run(repo.add_user("ali", 111))
    ad_id = _insert(repo, "tok1")
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    result = asyncio.run(plan_delivery_rows(repo, settings, ad_id))
    assert result.created == 3  # یک تلگرام + دو ایمیل
    rows = asyncio.run(repo.get_deliveries(ad_id))
    assert {(row["channel"], row["recipient"]) for row in rows} == {
        ("telegram", "111"),
        ("email", "user1@example.com"),
        ("email", "user2@example.com"),
    }
    assert all(row["status"] == "pending" for row in rows)


def test_plan_delivery_rows_is_idempotent(repo):
    asyncio.run(repo.add_user("ali", 111))
    ad_id = _insert(repo, "tok1")
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    asyncio.run(plan_delivery_rows(repo, settings, ad_id))
    result = asyncio.run(plan_delivery_rows(repo, settings, ad_id))
    assert result.created == 0


def test_plan_delivery_rows_no_users_no_telegram_rows(repo):
    ad_id = _insert(repo, "tok1")
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    result = asyncio.run(plan_delivery_rows(repo, settings, ad_id))
    assert result.created == 2  # فقط ایمیل


# --- جارو -------------------------------------------------------------------


def _pending_rows(repo, ad_id):
    return [
        row
        for row in asyncio.run(repo.get_deliveries(ad_id))
        if row["status"] == "pending"
    ]


def test_sweep_marks_sent_only_after_success(repo):
    asyncio.run(repo.add_user("ali", 111))
    ad_id = _insert(repo, "tok1")
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    asyncio.run(plan_delivery_rows(repo, settings, ad_id))
    sender = FakeSender()
    outcome = asyncio.run(_sweeper(repo, {"telegram": sender}).sweep_once())
    assert outcome.channels[0].sent == 1
    rows = asyncio.run(repo.get_deliveries(ad_id))
    telegram_row = next(row for row in rows if row["channel"] == "telegram")
    assert telegram_row["status"] == "sent"
    assert telegram_row["attempts"] == 1
    assert telegram_row["last_error"] is None


def test_sweep_transient_error_stays_pending_without_backoff(repo):
    asyncio.run(repo.add_user("ali", 111))
    ad_id = _insert(repo, "tok1")
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    asyncio.run(plan_delivery_rows(repo, settings, ad_id))
    sender = FakeSender(failures={"111": SendError(TRANSIENT, "قطع موقت شبکه")})
    outcome = asyncio.run(_sweeper(repo, {"telegram": sender}).sweep_once())
    assert outcome.channels[0].transient == 1
    row = _pending_rows(repo, ad_id)[0]
    assert row["next_attempt_at"] is None  # سویپ بعدی بدون backoff
    assert "قطع موقت" in row["last_error"]
    assert row["attempts"] == 1


def test_sweep_resurrectable_error_sets_backoff(repo):
    asyncio.run(repo.add_user("ali", 111))
    ad_id = _insert(repo, "tok1")
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    asyncio.run(plan_delivery_rows(repo, settings, ad_id))
    sender = FakeSender(
        failures={"111": SendError(RESURRECTABLE, "429 تکراری", retry_after=5)}
    )
    before = utc_now()
    outcome = asyncio.run(_sweeper(repo, {"telegram": sender}).sweep_once())
    assert outcome.channels[0].resurrectable == 1
    row = _pending_rows(repo, ad_id)[0]
    # base = retry_interval = 30m → تلاش اول: 1800 ثانیه (سرنخ 5s کمتر است)
    assert row["next_attempt_at"] is not None
    due = datetime.datetime.fromisoformat(row["next_attempt_at"])
    assert (due - before) >= datetime.timedelta(seconds=1790)
    # ردیف سررسیدنشده در سویپ بعدی برنمی‌گردد
    sender2 = FakeSender()
    outcome2 = asyncio.run(_sweeper(repo, {"telegram": sender2}).sweep_once())
    assert outcome2.channels[0].attempted == 0
    assert sender2.sent == []


def test_sweep_eternal_error_marks_dead(repo):
    asyncio.run(repo.add_user("ali", 111))
    ad_id = _insert(repo, "tok1")
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    asyncio.run(plan_delivery_rows(repo, settings, ad_id))
    sender = FakeSender(failures={"111": SendError(ETERNAL, "403 بلاک")})
    outcome = asyncio.run(_sweeper(repo, {"telegram": sender}).sweep_once())
    assert outcome.channels[0].dead == 1
    rows = asyncio.run(repo.get_deliveries(ad_id))
    telegram_row = next(row for row in rows if row["channel"] == "telegram")
    assert telegram_row["status"] == "dead"
    # dead برنمی‌گردد
    outcome2 = asyncio.run(
        _sweeper(repo, {"telegram": FakeSender()}).sweep_once()
    )
    assert outcome2.channels[0].attempted == 0


def test_sweep_cap_limits_sends_per_channel(repo):
    for index in range(3):
        ad_id = _insert(repo, f"tok{index}")
        asyncio.run(repo.record_search_match(ad_id, "s1"))
    asyncio.run(repo.add_user("ali", 111))
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    for index in range(3):
        row = asyncio.run(repo.get_ad_by_token(f"tok{index}"))
        asyncio.run(plan_delivery_rows(repo, settings, row["id"]))
    sender = FakeSender()
    outcome = asyncio.run(_sweeper(repo, {"telegram": sender}).sweep_once())
    assert outcome.channels[0].attempted == 2  # sweep_max_sends = 2
    assert len(sender.sent) == 2
    # مازاد به سویپ بعدی می‌رود
    outcome2 = asyncio.run(_sweeper(repo, {"telegram": sender}).sweep_once())
    assert outcome2.channels[0].sent == 1


def test_sweep_oldest_first(repo):
    for index in range(3):
        ad_id = _insert(repo, f"tok{index}", sort_date=f"2026-09-1{index}T10:00:00Z")
        asyncio.run(repo.record_search_match(ad_id, "s1"))
    asyncio.run(repo.add_user("ali", 111))
    settings = _settings(sweep_max_sends=10)
    for index in range(3):
        row = asyncio.run(repo.get_ad_by_token(f"tok{index}"))
        asyncio.run(plan_delivery_rows(repo, settings, row["id"]))
    sender = FakeSender()
    asyncio.run(_sweeper(repo, {"telegram": sender}, settings).sweep_once())
    assert [token for _, _, token in sender.sent] == ["tok0", "tok1", "tok2"]


def test_sweep_channels_are_independent(repo):
    ad_id = _insert(repo, "tok1")
    asyncio.run(repo.add_user("ali", 111))
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    asyncio.run(plan_delivery_rows(repo, settings, ad_id))
    telegram = FakeSender(
        failures={"111": SendError(TRANSIENT, "خطای تلگرام")}
    )
    email = FakeSender()
    outcome = asyncio.run(
        _sweeper(repo, {"telegram": telegram, "email": email}).sweep_once()
    )
    by_channel = {result.channel: result for result in outcome.channels}
    assert by_channel["telegram"].transient == 1
    assert by_channel["email"].sent == 2  # خطای تلگرام مانع ایمیل نشد


def test_sweep_label_from_first_matched_search(repo):
    ad_id = _insert(repo, "tok1")
    asyncio.run(repo.record_search_match(ad_id, "s1"))  # label: آپارتمان تهران
    asyncio.run(repo.record_search_match(ad_id, "s2"))
    asyncio.run(repo.add_user("ali", 111))
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    asyncio.run(plan_delivery_rows(repo, settings, ad_id))
    sender = FakeSender()
    asyncio.run(_sweeper(repo, {"telegram": sender}).sweep_once())
    assert sender.sent[0][1] == "آپارتمان تهران"


def test_backoff_growth_and_cap():
    assert compute_backoff_seconds(1, 1800) == 1800
    assert compute_backoff_seconds(2, 1800) == 3600
    assert compute_backoff_seconds(3, 1800) == 7200
    assert compute_backoff_seconds(20, 1800) == BACKOFF_CAP_SECONDS
    assert compute_backoff_seconds(1, 100000) == BACKOFF_CAP_SECONDS


# --- ارسال آزمایشی ضبطشده: notifier واقعی + پایگاه واقعی --------------------


def test_recorded_telegram_send_moves_row_to_sent(repo):
    """ارسال آزمایشی به مقصد تست (ضبط‌شده): ردیف pending → sent."""

    class RecordedTransport:
        def __init__(self, responses):
            self.responses = list(responses)
            self.calls = []

        async def __call__(self, method, url, headers, body=None):
            self.calls.append(
                (method, url, headers, json.loads(body.decode("utf-8")))
            )
            status, payload = self.responses.pop(0)
            return status, {}, json.dumps(payload).encode("utf-8")

    ad_id = _insert(repo, "tok1")
    asyncio.run(repo.record_search_match(ad_id, "s1"))
    asyncio.run(repo.add_user("ali", 111))
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    asyncio.run(plan_delivery_rows(repo, settings, ad_id))

    transport = RecordedTransport([(200, {"ok": True, "result": {"message_id": 7}})])

    async def no_sleep(seconds):
        return None

    notifier = TelegramNotifier("TOK", transport=transport, sleeper=no_sleep)
    sweeper = DeliverySweeper(
        repo,
        {"telegram": telegram_sender(notifier)},
        settings,
        searches_by_id={"s1": {"id": "s1", "label": "آپارتمان تهران"}},
        pauses={"telegram": 0},
        sleeper=_no_sleep,
    )
    outcome = asyncio.run(sweeper.sweep_once())
    assert outcome.channels[0].sent == 1
    method, url, headers, payload = transport.calls[0]
    assert payload["chat_id"] == "111"
    assert payload["parse_mode"] == "HTML"
    assert payload["disable_web_page_preview"] is True
    assert payload["text"].split("\n")[0] == "<b>آپارتمان ۵۵ متری پونک — آپارتمان تهران</b>"
    assert payload["text"].endswith("https://divar.ir/v/tok1")
    rows = asyncio.run(repo.get_deliveries(ad_id))
    assert rows[0]["status"] == "sent"


def test_recorded_email_send_via_local_smtp(monkeypatch, repo):
    """ارسال ضبط‌شدهٔ SMTP: ایمیل متن ساده + موضوع مصوب؛ 250 → sent."""

    class RecordedSMTP:
        instances = []

        def __init__(self, host, port, timeout=None):
            self.host, self.port = host, port
            self.calls = []
            self.sent = []
            RecordedSMTP.instances.append(self)

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def starttls(self, context=None):
            self.calls.append(("starttls", context))

        def login(self, username, password):
            self.calls.append(("login", username, password))

        def send_message(self, message):
            self.calls.append(("send_message", message))
            return {}

    monkeypatch.setattr("top_divar.notify.email.smtplib.SMTP", RecordedSMTP)
    ad_id = _insert(repo, "tok1")
    asyncio.run(repo.record_search_match(ad_id, "s1"))
    settings = NotifySettings.from_config(RECIPIENTS_CONFIG)
    asyncio.run(plan_delivery_rows(repo, settings, ad_id))

    notifier = EmailNotifier(settings.email.smtp, "secret")
    sweeper = DeliverySweeper(
        repo,
        {"email": email_sender(notifier)},
        settings,
        searches_by_id={"s1": {"id": "s1", "label": "آپارتمان تهران"}},
        pauses={"email": 0},
        sleeper=_no_sleep,
    )
    outcome = asyncio.run(sweeper.sweep_once())
    assert outcome.channels[0].sent == 2
    assert len(RecordedSMTP.instances) == 2  # هر گیرنده یک اتصال
    smtp = RecordedSMTP.instances[0]
    kinds = [call[0] for call in smtp.calls]
    assert kinds == ["starttls", "login", "send_message"]
    assert smtp.calls[0][1] is not None  # context گواهی الزامی
    assert smtp.calls[1][2] == "secret"
    first_message = smtp.calls[2][1]
    assert first_message["Subject"] == "Top Divar — آپارتمان ۵۵ متری پونک (امتیاز ۶۵)"
    assert first_message["To"] == "user1@example.com"
    body = first_message.get_content()
    assert "<b>" not in body
    assert body.rstrip("\n").endswith("https://divar.ir/v/tok1")
    rows = asyncio.run(repo.get_deliveries(ad_id))
    assert all(row["status"] == "sent" for row in rows)


def test_email_tls_mode_uses_smtp_ssl(monkeypatch):
    import smtplib

    created = []

    class FakeSSL:
        def __init__(self, host, port, timeout=None, context=None):
            created.append(("ssl", host, port, context))

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def send_message(self, message):
            return {}

    monkeypatch.setattr(smtplib, "SMTP_SSL", FakeSSL)
    smtp_settings = SMTPSettings(
        host="smtp.example.com", port=465, encryption="tls", username=None
    )
    notifier = EmailNotifier(smtp_settings, None)
    asyncio.run(notifier.send_message("x@y.z", "موضوع", "متن"))
    assert created[0][0] == "ssl"
    assert created[0][2] == 465
    assert created[0][3] is not None


def test_email_recipients_refused_is_eternal(monkeypatch):
    import smtplib

    class RefusingSMTP:
        def __init__(self, *args, **kwargs):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def send_message(self, message):
            raise smtplib.SMTPRecipientsRefused({"x@y.z": (550, "No such user")})

    monkeypatch.setattr(smtplib, "SMTP", RefusingSMTP)
    notifier = EmailNotifier(
        SMTPSettings(host="h", encryption="none", username=None), None
    )
    with pytest.raises(SendError) as excinfo:
        asyncio.run(notifier.send_message("x@y.z", "s", "b"))
    assert excinfo.value.category == ETERNAL


def test_email_smtp_4xx_is_resurrectable(monkeypatch):
    import smtplib

    class TemporarySMTP:
        def __init__(self, *args, **kwargs):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def send_message(self, message):
            raise smtplib.SMTPResponseException(421, "Service not available")

    monkeypatch.setattr(smtplib, "SMTP", TemporarySMTP)
    notifier = EmailNotifier(
        SMTPSettings(host="h", encryption="none", username=None), None
    )
    with pytest.raises(SendError) as excinfo:
        asyncio.run(notifier.send_message("x@y.z", "s", "b"))
    assert excinfo.value.category == RESURRECTABLE


def test_email_network_error_is_transient(monkeypatch):
    import smtplib

    class BrokenSMTP:
        def __init__(self, host, port, timeout=None):
            raise OSError("connection refused")

    monkeypatch.setattr(smtplib, "SMTP", BrokenSMTP)
    notifier = EmailNotifier(
        SMTPSettings(host="h", encryption="none", username=None), None
    )
    with pytest.raises(SendError) as excinfo:
        asyncio.run(notifier.send_message("x@y.z", "s", "b"))
    assert excinfo.value.category == TRANSIENT


def test_email_settings_from_config_defaults():
    settings = NotifySettings.from_config({})
    assert settings.channels == ()
    assert settings.retry_interval == 1800.0
    assert settings.sweep_max_sends == 50
    assert settings.email.to == ()
    assert not settings.telegram_enabled and not settings.email_enabled

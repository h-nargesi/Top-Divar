"""تست درگاه بات (مرحلهٔ ۷) — ثبت‌نام، جبران G5، /resend، /status، /help."""

import asyncio
import datetime

import pytest

from top_divar.bot import BotGateway
from top_divar.bot.gateway import (
    MSG_ASK_PASSWORD,
    MSG_ASK_USERNAME,
    MSG_BLOCKED,
    MSG_REGISTERED,
    MSG_RESEND_COOLDOWN,
    MSG_RESEND_EMPTY,
    MSG_RESEND_TOO_OLD,
    MSG_RESEND_USAGE,
    MSG_WRONG_PASSWORD,
    poll_error_delay,
)
from top_divar.bot.guards import (
    GlobalPasswordCounter,
    PasswordThrottle,
    RegistrationSessions,
    ResendCooldowns,
)
from top_divar.notify.errors import SendError
from top_divar.storage import SqliteRepository
from top_divar.storage.timestamps import utc_now

PASSWORD = "s3cret"


class FakeClient:
    """کلاینت ضبط‌شده — getUpdates اسکریپتی و sendMessage فقط ثبت می‌کند."""

    def __init__(self, batches=None, failures=None):
        self.sent = []  # (chat_id, text)
        self.failures = dict(failures or {})  # chat_id → SendError
        self._batches = list(batches or [])
        self.get_updates_calls = 0

    async def get_updates(self, *, offset=None, timeout=0, allowed_updates=None):
        self.get_updates_calls += 1
        if self._batches:
            return self._batches.pop(0)
        return []

    async def send_message(self, chat_id, text, *, parse_mode=None):
        failure = self.failures.get(chat_id)
        if failure is not None:
            raise failure
        self.sent.append((chat_id, text))

    def replies_to(self, chat_id):
        return [text for target, text in self.sent if target == chat_id]


class FakeAdSender:
    def __init__(self, failures=None):
        self.sent = []
        self.failures = dict(failures or {})

    async def __call__(self, chat_id, text):
        failure = self.failures.get(chat_id)
        if failure is not None:
            raise failure
        self.sent.append((chat_id, text))


def _update(chat_id, text, update_id=1):
    return {
        "update_id": update_id,
        "message": {"chat": {"id": chat_id}, "text": text},
    }


@pytest.fixture()
def repo(tmp_path):
    repository = SqliteRepository(tmp_path / "db.sqlite3")
    yield repository
    repository.close()


def _gateway(repo, client, *, ad_sender=None, sweeper=None, ops_chat_id=None,
             today=None, backfill_days=7, **guard_overrides):
    guards = {
        "sessions": RegistrationSessions(),
        "throttle": PasswordThrottle(),
        "global_counter": GlobalPasswordCounter(),
        "resend_cooldowns": ResendCooldowns(),
    }
    guards.update(guard_overrides)
    kwargs = {}
    if today is not None:
        kwargs["today_provider"] = lambda: today
    return BotGateway(
        repo,
        client,
        password=PASSWORD,
        ad_sender=ad_sender,
        sweeper=sweeper,
        ops_chat_id=ops_chat_id,
        backfill_days=backfill_days,
        **guards,
        **kwargs,
    )


def _insert(repo, token, sort_date="2026-09-20T10:00:00Z", **overrides):
    fields = {
        "title": "آپارتمان آزمایش",
        "price": 1_000_000_000,
        "district": "پونک",
        "raw_json": '{"v": 1}',
    }
    fields.update(overrides)
    return asyncio.run(repo.insert_ad(token, sort_date, **fields))


def _notable(repo, token, recipients=("100",), sort_date="2026-09-20T10:00:00Z"):
    ad_id = _insert(repo, token, sort_date)
    asyncio.run(repo.store_score(token, 75, "[]"))
    asyncio.run(
        repo.create_delivery_rows(ad_id, [("telegram", r) for r in recipients])
    )
    return ad_id


# --- ثبت‌نام ----------------------------------------------------------------

def test_registration_flow_puts_user_in_db(repo):
    client = FakeClient()
    gateway = _gateway(repo, client)
    asyncio.run(gateway.handle_update(_update(100, "/start")))
    assert client.replies_to(100)[-1] == MSG_ASK_PASSWORD
    asyncio.run(gateway.handle_update(_update(100, "wrong")))
    assert MSG_WRONG_PASSWORD.split(".")[0] in client.replies_to(100)[-1]
    asyncio.run(gateway.handle_update(_update(100, PASSWORD)))
    assert client.replies_to(100)[-1] == MSG_ASK_USERNAME
    asyncio.run(gateway.handle_update(_update(100, "Ali!")))
    assert "معتبر نیست" in client.replies_to(100)[-1]
    asyncio.run(gateway.handle_update(_update(100, "alice")))
    assert MSG_REGISTERED.format(username="alice") in client.replies_to(100)[-1]
    user = asyncio.run(repo.get_user("alice"))
    assert user["chat_id"] == 100


def test_duplicate_username_case_insensitive(repo):
    asyncio.run(repo.add_user("alice", 100))
    client = FakeClient()
    gateway = _gateway(repo, client)
    asyncio.run(gateway.handle_update(_update(200, "/start")))
    asyncio.run(gateway.handle_update(_update(200, PASSWORD)))
    asyncio.run(gateway.handle_update(_update(200, "alice")))
    assert "قبلاً گرفته شده" in client.replies_to(200)[-1]
    assert asyncio.run(repo.get_user_by_chat_id(200)) is None


def test_wrong_password_blocks_after_five_failures(repo):
    client = FakeClient()
    gateway = _gateway(repo, client)
    asyncio.run(gateway.handle_update(_update(100, "/start")))
    for _ in range(5):
        asyncio.run(gateway.handle_update(_update(100, "wrong")))
    assert MSG_BLOCKED.split("؛")[0] in client.replies_to(100)[-1]
    # بعد از بلاک، /start هم راه نمی‌دهد و گفتگو انداخته شده است
    asyncio.run(gateway.handle_update(_update(100, "/start")))
    assert MSG_BLOCKED.split("؛")[0] in client.replies_to(100)[-1]


def test_global_bruteforce_alerts_ops_once(repo):
    client = FakeClient()
    gateway = _gateway(repo, client, ops_chat_id=999)
    for chat_id in range(1, 21):
        asyncio.run(gateway.handle_update(_update(chat_id, "/start")))
        asyncio.run(gateway.handle_update(_update(chat_id, "wrong")))
    ops_messages = client.replies_to(999)
    assert len(ops_messages) == 1
    assert "بروت‌فورس" in ops_messages[0]
    # چرخهٔ بعدی (پنجرهٔ نو) دوباره هشدار می‌دهد — اینجا فقط تعداد می‌سنجیم
    for chat_id in range(21, 41):
        asyncio.run(gateway.handle_update(_update(chat_id, "/start")))
        asyncio.run(gateway.handle_update(_update(chat_id, "wrong")))
    assert len(client.replies_to(999)) == 1  # هنوز داخل پنجرهٔ هشدار


def test_restart_drops_half_finished_conversation(repo):
    """ری‌استارت گفتگوی نیمه‌کاره را می‌اندازد — state فقط در حافظه است."""
    client = FakeClient()
    gateway = _gateway(repo, client)
    asyncio.run(gateway.handle_update(_update(100, "/start")))
    asyncio.run(gateway.handle_update(_update(100, PASSWORD)))
    # ری‌استارت: درگاه تازه هیچ stateای ندارد
    client2 = FakeClient()
    gateway2 = _gateway(repo, client2)
    asyncio.run(gateway2.handle_update(_update(100, "alice")))
    assert "/start" in client2.replies_to(100)[-1]
    assert asyncio.run(repo.get_user("alice")) is None


# --- دستورها -----------------------------------------------------------------

def test_help_and_status(repo):
    asyncio.run(repo.add_user("alice", 100))
    client = FakeClient()
    gateway = _gateway(repo, client)
    asyncio.run(gateway.handle_update(_update(100, "/help")))
    assert "/resend" in client.replies_to(100)[-1]
    asyncio.run(gateway.handle_update(_update(100, "/status")))
    assert "alice" in client.replies_to(100)[-1]
    assert "۰" in client.replies_to(100)[-1]
    asyncio.run(gateway.handle_update(_update(200, "/status")))
    assert "/start" in client.replies_to(200)[-1]


def test_status_counts_pending(repo):
    asyncio.run(repo.add_user("alice", 100))
    _notable(repo, "a", recipients=("100",))
    _notable(repo, "b", recipients=("100",))
    client = FakeClient()
    gateway = _gateway(repo, client)
    asyncio.run(gateway.handle_update(_update(100, "/status")))
    assert "۲" in client.replies_to(100)[-1]


def test_start_from_registered_user_triggers_backfill(repo):
    """هر update کاربر ثبت‌شده — حتی /start تکراری — محرک جبران است."""
    asyncio.run(repo.add_user("alice", 100))
    _notable(repo, "a", recipients=("100",))
    client = FakeClient()
    ad_sender = FakeAdSender()
    sweeper = _sweeper(repo, ad_sender)
    gateway = _gateway(repo, client, ad_sender=ad_sender, sweeper=sweeper)
    asyncio.run(gateway.handle_update(_update(100, "/start")))
    assert "alice" in client.replies_to(100)[-1]
    assert [chat for chat, _ in ad_sender.sent] == ["100"]
    # پیام جبران به‌عنوان delivery علامت خورد
    deliveries = asyncio.run(repo.get_deliveries(_insert_id(repo, "a")))
    assert deliveries[0]["status"] == "sent"


def _insert_id(repo, token):
    row = asyncio.run(repo.get_ad_by_token(token))
    return row["id"]


def _sweeper(repo, ad_sender):
    from top_divar.notify import DeliverySweeper, NotifySettings
    from top_divar.notify.sweep import telegram_sender

    return DeliverySweeper(
        repo,
        {"telegram": telegram_sender(_NotifierShim(ad_sender))},
        NotifySettings(),
        pauses={"telegram": 0, "email": 0},
        sleeper=_no_sleep,
    )


class _NotifierShim:
    """ادغام ارسال‌کنندهٔ جعلی در شکل TelegramNotifier."""

    def __init__(self, ad_sender):
        self._ad_sender = ad_sender

    async def send_message(self, chat_id, text):
        await self._ad_sender(chat_id, text)


async def _no_sleep(seconds):
    # باید واقعاً به حلقهٔ رویداد کنترل بدهیم تا تسک توقف‌دهنده اجرا شود
    await asyncio.sleep(0)


def test_backfill_ignores_backoff_and_skips_dead(repo):
    """G5: تعامل کاربر = ارسال فوری؛ dead برنمی‌گردد."""
    asyncio.run(repo.add_user("alice", 100))
    ad_a = _notable(repo, "a", recipients=("100",))
    ad_b = _notable(repo, "b", recipients=("100",))
    rows = asyncio.run(repo.get_deliveries(ad_b))
    asyncio.run(
        repo.mark_delivery(
            rows[0]["id"],
            "pending",
            next_attempt_at=utc_now() + datetime.timedelta(hours=12),
        )
    )
    ad_c = _notable(repo, "c", recipients=("100",))
    rows = asyncio.run(repo.get_deliveries(ad_c))
    asyncio.run(repo.mark_delivery(rows[0]["id"], "dead", error="403"))
    client = FakeClient()
    ad_sender = FakeAdSender()
    gateway = _gateway(
        repo, client, ad_sender=ad_sender, sweeper=_sweeper(repo, ad_sender)
    )
    asyncio.run(gateway.handle_update(_update(100, "سلام")))
    assert [token_of(text) for _, text in ad_sender.sent] == ["a", "b"]
    for ad_id in (ad_a, ad_b):
        assert asyncio.run(repo.get_deliveries(ad_id))[0]["status"] == "sent"
    assert asyncio.run(repo.get_deliveries(ad_c))[0]["status"] == "dead"


def token_of(ad_text):
    return ad_text.rsplit("/", 1)[-1]


def test_backfill_respects_window(repo):
    asyncio.run(repo.add_user("alice", 100))
    ad_id = _notable(repo, "a", recipients=("100",))
    conn_deliveries = asyncio.run(repo.get_deliveries(ad_id))
    old = "2020-01-01T00:00:00+00:00"
    # created_at را دستی عقب می‌بریم تا بیرون پنجرهٔ ۷ روزه بیفتد
    repo._conn.execute(
        "UPDATE delivery SET created_at = ? WHERE id = ?", (old, conn_deliveries[0]["id"])
    )
    repo._conn.commit()
    client = FakeClient()
    ad_sender = FakeAdSender()
    gateway = _gateway(
        repo, client, ad_sender=ad_sender, sweeper=_sweeper(repo, ad_sender)
    )
    asyncio.run(gateway.handle_update(_update(100, "سلام")))
    assert ad_sender.sent == []


# --- /resend ------------------------------------------------------------------

def test_resend_requires_registration_and_valid_date(repo):
    client = FakeClient()
    gateway = _gateway(repo, client)
    asyncio.run(gateway.handle_update(_update(100, "/resend 1405/06/01")))
    assert "/start" in client.replies_to(100)[-1]

    asyncio.run(repo.add_user("alice", 100))
    asyncio.run(gateway.handle_update(_update(100, "/resend 1405/13/01")))
    assert client.replies_to(100)[-1] == MSG_RESEND_USAGE
    asyncio.run(gateway.handle_update(_update(100, "/resend")))
    assert client.replies_to(100)[-1] == MSG_RESEND_USAGE


def test_resend_rejects_future_and_too_old_dates(repo):
    asyncio.run(repo.add_user("alice", 100))
    client = FakeClient()
    gateway = _gateway(repo, client, today=(1405, 7, 1))
    asyncio.run(gateway.handle_update(_update(100, "/resend 1405/07/02")))
    assert "آینده" in client.replies_to(100)[-1]
    asyncio.run(gateway.handle_update(_update(100, "/resend 1404/06/01")))
    assert client.replies_to(100)[-1] == MSG_RESEND_TOO_OLD
    # مرز ۳۰ روز دقیقاً مجاز است: ۱۴۰۵/۰۶/۰۱ تا ۱۴۰۵/۰۷/۰۱ = ۳۱ روز → رد؟
    # (۳۰ روز قبل از ۱۴۰۵/۰۷/۰۱ برابر ۱۴۰۵/۰۶/۰۲ است)
    asyncio.run(gateway.handle_update(_update(100, "/resend 1405/06/02")))
    assert client.replies_to(100)[-1] == MSG_RESEND_EMPTY  # پنجره مجاز، آگهی نیست


def test_resend_sends_notable_ads_only_to_requester(repo):
    asyncio.run(repo.add_user("alice", 100))
    asyncio.run(repo.add_user("bob", 200))
    _notable(repo, "old", sort_date="2026-09-15T10:00:00Z")
    _notable(repo, "new1", sort_date="2026-09-25T10:00:00Z")
    _notable(repo, "new2", sort_date="2026-09-26T10:00:00Z")
    _insert(repo, "plain", "2026-09-26T10:00:00Z")  # زیر حد؛ ردیف ندارد
    client = FakeClient()
    ad_sender = FakeAdSender()
    gateway = _gateway(repo, client, ad_sender=ad_sender, today=(1405, 7, 8))
    asyncio.run(gateway.handle_update(_update(100, "/resend 1405/06/25")))
    tokens = [token_of(text) for _, text in ad_sender.sent]
    assert tokens == ["new1", "new2"]  # قدیمی‌ترین اول؛ فقط ممتازها
    assert all(chat == 100 for chat, _ in ad_sender.sent)
    assert "۲ آگهی ارسال شد" in client.replies_to(100)[-1]
    # مستقل از جدول delivery — ردیفی علامت نمی‌خورد
    deliveries = asyncio.run(repo.get_deliveries(_insert_id(repo, "new1")))
    assert deliveries[0]["status"] == "pending"


def test_resend_cooldown_ten_minutes(repo):
    asyncio.run(repo.add_user("alice", 100))
    _notable(repo, "a")
    client = FakeClient()
    ad_sender = FakeAdSender()
    clock = _FakeMonotonic()
    gateway = _gateway(
        repo,
        client,
        ad_sender=ad_sender,
        today=_today_near_now(),
        resend_cooldowns=ResendCooldowns(clock=clock),
    )
    asyncio.run(gateway.handle_update(_update(100, "/resend 1405/06/25")))
    assert "۱ آگهی ارسال شد" in client.replies_to(100)[-1]
    asyncio.run(gateway.handle_update(_update(100, "/resend 1405/06/25")))
    assert MSG_RESEND_COOLDOWN.split("؛")[0] in client.replies_to(100)[-1]
    clock.advance(10 * 60 + 1)
    asyncio.run(gateway.handle_update(_update(100, "/resend 1405/06/25")))
    assert client.replies_to(100)[-1].count("آگهی ارسال شد") >= 1


class _FakeMonotonic:
    def __init__(self):
        self.now = 5.0

    def __call__(self):
        return self.now

    def advance(self, seconds):
        self.now += seconds


def _today_near_now():
    from top_divar.divar.jalali import gregorian_to_jalali

    now = utc_now()
    return gregorian_to_jalali(now.year, now.month, now.day)


def test_resend_send_failure_counted(repo):
    asyncio.run(repo.add_user("alice", 100))
    _notable(repo, "a")
    _notable(repo, "b")
    client = FakeClient()
    ad_sender = FakeAdSender(
        failures={100: SendError(category="transient", message="شبکه قطع است")}
    )
    gateway = _gateway(repo, client, ad_sender=ad_sender, today=_today_near_now())
    asyncio.run(gateway.handle_update(_update(100, "/resend 1405/06/25")))
    assert "خطا خورد" in client.replies_to(100)[-1]


# --- حلقهٔ polling ---------------------------------------------------------------

def test_run_loop_survives_409_and_processes_updates(repo):
    """409 تلگرام گذراست: backoff کوتاه و ادامهٔ polling (ADR-0010)."""
    asyncio.run(repo.add_user("alice", 100))
    conflict = SendError(category="transient", message="tel 409 conflict")
    client = _FailingOnceClient(
        [[_update(100, "/status")]], failure=conflict
    )
    gateway = _gateway(repo, client)
    stop = asyncio.Event()

    async def _stop_soon():
        await asyncio.sleep(0)
        while not client.sent:
            await asyncio.sleep(0)
        stop.set()

    gateway._sleeper = _no_sleep

    async def _main():
        await asyncio.gather(gateway.run(stop), _stop_soon())

    asyncio.run(_main())
    assert client.replies_to(100)  # بعد از 409، به‌روز پردازش شد
    assert client.get_updates_calls >= 2


class _FailingOnceClient(FakeClient):
    def __init__(self, batches, failure):
        super().__init__(batches)
        self._failure = failure
        self._failed_once = False

    async def get_updates(self, **kwargs):
        if not self._failed_once:
            self._failed_once = True
            raise self._failure
        return await super().get_updates(**kwargs)


def test_poll_error_delay_uses_retry_after_capped():
    assert poll_error_delay(
        SendError(category="resurrectable", message="x", retry_after=200)
    ) == 60.0
    assert poll_error_delay(
        SendError(category="transient", message="x", retry_after=3)
    ) == 3.0
    assert poll_error_delay(SendError(category="transient", message="x")) == 5.0

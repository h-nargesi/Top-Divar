"""تست سرویس (مرحلهٔ ۷): reload زنده، هشدار اپراتور، قفل تک‌نمونه."""

import asyncio
import datetime

import pytest

from top_divar.core.settings import PollingSettings
from top_divar.divar.errors import DivarError
from top_divar.notify.errors import SendError
from top_divar.service import OpsAlerter, Service
from top_divar.shared.locking import SingleInstanceLock
from top_divar.storage import SqliteRepository
from top_divar.storage.timestamps import utc_now

CONFIG = """
searches:
  - id: s1
    city_ids: ["1"]
    form_data:
      category: {str: {value: apartment-sell}}
    scoring_ref: default
  - id: s2
    label: جستجوی دوم
    city_ids: ["1"]
    form_data:
      category: {str: {value: apartment-sell}}
    scoring_ref: default
scoring:
  default:
    min_score: 60
    on_missing_field: skip
    rules:
      - {field: price, op: "<=", value: 100, points: 5}
"""

CONFIG_S2_DISABLED = CONFIG.replace(
    "- id: s2\n    label: جستجوی دوم",
    "- id: s2\n    enabled: false\n    label: جستجوی دوم",
)


@pytest.fixture()
def repo(tmp_path):
    repository = SqliteRepository(tmp_path / "db.sqlite3")
    yield repository
    repository.close()


def _service(repo, tmp_path, config_text=CONFIG, env=None):
    import yaml

    config_path = tmp_path / "config.yaml"
    config_path.write_text(config_text, encoding="utf-8")
    raw = yaml.safe_load(config_text)
    return Service(
        repo,
        raw,
        env or {},
        config_path=str(config_path),
        env_path=str(tmp_path / ".env"),
    )


# --- reload زندهٔ کانفیگ --------------------------------------------------------

def test_reload_bad_yaml_keeps_old_config(repo, tmp_path):
    service = _service(repo, tmp_path)
    assert service.scheduler.search_ids == ["s1", "s2"]
    (tmp_path / "config.yaml").write_text("searches: [unclosed", encoding="utf-8")
    service.reload_config()
    assert service.scheduler.search_ids == ["s1", "s2"]
    assert service.scheduler.schedules[0].search["id"] == "s1"


def test_reload_invalid_config_keeps_old_config(repo, tmp_path):
    service = _service(repo, tmp_path)
    invalid = CONFIG.replace("scoring_ref: default", "scoring_ref: nope")
    (tmp_path / "config.yaml").write_text(invalid, encoding="utf-8")
    service.reload_config()
    assert service.scheduler.search_ids == ["s1", "s2"]


def test_reload_applies_new_searches_live(repo, tmp_path):
    """enabled: false یا id غایب → poll نمی‌شود؛ برگشت همان id ادامه می‌دهد."""
    service = _service(repo, tmp_path)
    schedules = {s.search_id: s for s in service.scheduler.schedules}
    s1_schedule = schedules["s1"]
    s1_schedule.next_due += 12345.0  # علامت گذاشتن state برای اثبات حفظ شدن

    (tmp_path / "config.yaml").write_text(CONFIG_S2_DISABLED, encoding="utf-8")
    service.reload_config()
    assert service.scheduler.search_ids == ["s1"]
    kept = service.scheduler.schedules[0]
    assert kept is s1_schedule  # همان شیء — next_due و خطاهای قبلی حفظ شد
    assert kept.next_due > 12345.0

    # برگشت همان id: از watermark قبلی ادامه می‌دهد (تاریخچه مستقل است)
    asyncio.run(repo.update_watermark("s2", "2026-09-20T10:00:00Z"))
    (tmp_path / "config.yaml").write_text(CONFIG, encoding="utf-8")
    service.reload_config()
    assert service.scheduler.search_ids == ["s1", "s2"]


def test_reload_updates_polling_settings(repo, tmp_path):
    service = _service(repo, tmp_path)
    tuned = CONFIG + "\npolling:\n  default_interval: 10m\n"
    (tmp_path / "config.yaml").write_text(tuned, encoding="utf-8")
    service.reload_config()
    assert service.scheduler._settings.default_interval == 600.0


# --- هشدار اپراتور --------------------------------------------------------------

class _RecordingSender:
    def __init__(self, failures=None):
        self.sent = []
        self.failures = list(failures or [])

    async def __call__(self, chat_id, text):
        if self.failures:
            failure = self.failures.pop(0)
            raise failure
        self.sent.append((chat_id, text))


def test_ops_alerter_throttles_to_once_per_day():
    class Clock:
        def __init__(self):
            self.now = utc_now()

        def __call__(self):
            return self.now

    clock = Clock()
    sender = _RecordingSender()
    alerter = OpsAlerter(sender, "999", clock=clock)
    assert asyncio.run(alerter.send("اول")) is True
    assert asyncio.run(alerter.send("دوم")) is False  # داخل ۲۴ ساعت
    clock.now += datetime.timedelta(hours=25)
    assert asyncio.run(alerter.send("سوم")) is True
    assert [text for _, text in sender.sent] == ["اول", "سوم"]


def test_ops_alerter_swallows_send_errors():
    sender = _RecordingSender(
        failures=[SendError(category="transient", message="شبکه")]
    )
    alerter = OpsAlerter(sender, "999")
    assert asyncio.run(alerter.send("هشدار")) is False


def test_scheduler_pause_alerts_ops_with_throttle(repo, tmp_path):
    """بعد از max_consecutive_errors خطای متوالی، هشدار اپراتور می‌رود (ADR-0003)."""
    alerts = []

    async def _poll(search):
        raise DivarError("دیوار 502 داد")

    from top_divar.core.scheduler import PollScheduler

    async def _on_paused(schedule, exc):
        alerts.append(schedule.search_id)

    settings = PollingSettings(max_consecutive_errors=3)

    class SteadyClock:
        """ساعتی که بعد از هر دور به اندازهٔ backoff جلو می‌رود."""

        def __init__(self):
            self.now = 1000.0

        def __call__(self):
            return self.now

        def advance(self, seconds):
            self.now += seconds

    clock = SteadyClock()
    scheduler = PollScheduler(
        [{"id": "s1", "enabled": True, "city_ids": ["1"], "form_data": {}}],
        settings,
        _poll,
        on_paused=_on_paused,
        clock=clock,
    )
    for _ in range(3):
        asyncio.run(scheduler.run_once())
        clock.advance(10_000.0)  # از backoff جلوتر — خطای «متوالی» می‌ماند
    assert alerts == ["s1"]  # رسیدن به آستانه هشدار ساخت
    asyncio.run(scheduler.run_once())
    clock.advance(10_000.0)
    assert alerts == ["s1", "s1"]  # هر توقف دوباره هشدار می‌سازد؛ throttle سمت فرستنده است


# --- قفل تک‌نمونه ------------------------------------------------------------------

def test_single_instance_lock_blocks_second_holder(tmp_path):
    lock_path = tmp_path / "top_divar.lock"
    first = SingleInstanceLock(lock_path)
    assert first.acquire() is True
    second = SingleInstanceLock(lock_path)
    assert second.acquire() is False
    first.release()
    assert second.acquire() is True
    second.release()


def test_single_instance_lock_released_on_object_release(tmp_path):
    lock = SingleInstanceLock(tmp_path / "top_divar.lock")
    with lock as acquired:
        assert acquired is True
    other = SingleInstanceLock(tmp_path / "top_divar.lock")
    assert other.acquire() is True


# --- مونتاژ سرویس ------------------------------------------------------------------

def test_service_builds_gateway_without_channels(repo, tmp_path):
    env = {
        "TELEGRAM_BOT_TOKEN": "1:test",
        "TELEGRAM_BOT_PASSWORD": "pw",
        "TELEGRAM_OPS_CHAT_ID": "42",
    }
    service = _service(repo, tmp_path, env=env)
    assert service.gateway is not None
    assert service.sweeper is None  # کانالی فعال نیست
    assert service._ops_alerter is not None


def test_service_without_bot_env_disables_gateway(repo, tmp_path):
    service = _service(repo, tmp_path)
    assert service.gateway is None
    assert service._ops_alerter is None


def test_reload_enabling_channels_builds_sweeper(repo, tmp_path):
    """روشن‌کردن کانال در SIGHUP باید جارو را بسازد و به بات وصل کند."""
    env = {
        "TELEGRAM_BOT_TOKEN": "1:test",
        "TELEGRAM_BOT_PASSWORD": "pw",
    }
    service = _service(repo, tmp_path, env=env)
    assert service.sweeper is None
    assert service.gateway._sweeper is None

    enabled = CONFIG + "\nnotify:\n  channels: [telegram]\n"
    (tmp_path / "config.yaml").write_text(enabled, encoding="utf-8")
    service.reload_config()
    assert service.sweeper is not None
    assert "telegram" in service.sweeper._senders
    assert service.gateway._sweeper is service.sweeper

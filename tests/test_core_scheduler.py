import asyncio
import logging

import pytest

from top_divar.core.scheduler import PollScheduler, resolve_search_interval
from top_divar.core.settings import PollingSettings
from top_divar.divar.errors import DivarHTTPError


class FakeClock:
    def __init__(self, start=1000.0):
        self.now = start

    def __call__(self):
        return self.now

    def advance(self, seconds):
        self.now += seconds


class FakeSleeper:
    def __init__(self, clock):
        self.clock = clock
        self.sleeps = []

    async def __call__(self, seconds):
        self.sleeps.append(seconds)
        self.clock.advance(seconds)


def _settings(**overrides):
    fields = {
        "min_interval": 300.0,
        "default_interval": 300.0,
        "jitter": 30.0,
        "max_consecutive_errors": 3,
    }
    fields.update(overrides)
    return PollingSettings(**fields)


def _scheduler(searches, poll, *, settings=None, clock=None, rng=lambda a, b: 0.0):
    return PollScheduler(
        searches,
        settings or _settings(),
        poll,
        clock=clock or FakeClock(),
        sleeper=FakeSleeper(clock or FakeClock()),
        rng=rng,
    )


def test_enabled_flag_filters_searches():
    polled = []

    async def poll(search):
        polled.append(search["id"])

    scheduler = _scheduler(
        [{"id": "on", "enabled": True}, {"id": "off", "enabled": False}],
        poll,
    )
    asyncio.run(scheduler.run_once())
    assert polled == ["on"]


def test_interval_resolution_default_and_override():
    settings = _settings(default_interval=120.0)
    assert resolve_search_interval({"id": "s1"}, settings) == 120.0
    assert resolve_search_interval({"id": "s1", "interval": "7m"}, settings) == 420.0
    assert resolve_search_interval({"id": "s1", "interval": "خراب"}, settings) == 120.0


def test_jitter_offset_applied_and_floored():
    clock = FakeClock()
    polled = []

    async def poll(search):
        polled.append(search["id"])

    scheduler = _scheduler(
        [{"id": "s1", "interval": "6m"}],
        poll,
        settings=_settings(min_interval=300.0, default_interval=300.0, jitter=30.0),
        clock=clock,
        rng=lambda a, b: 10.0,
    )
    asyncio.run(scheduler.run_once())
    assert scheduler.schedules[0].next_due == clock.now + 370.0  # 360 + 10

    clock.advance(370.0)
    asyncio.run(scheduler.run_once())
    # لرزش منفی بزرگ نباید زیر کف برود
    scheduler._rng = lambda a, b: -999.0
    clock.advance(scheduler.schedules[0].next_due - clock.now)
    asyncio.run(scheduler.run_once())
    assert scheduler.schedules[0].next_due == clock.now + 300.0


def test_success_reschedules_with_interval():
    clock = FakeClock()
    calls = []

    async def poll(search):
        calls.append(search["id"])

    scheduler = _scheduler([{"id": "s1", "interval": "5m"}], poll, clock=clock)
    assert asyncio.run(scheduler.run_once()) == 1
    assert asyncio.run(scheduler.run_once()) == 0  # هنوز سر نرسیده
    clock.advance(300.0)
    assert asyncio.run(scheduler.run_once()) == 1
    assert calls == ["s1", "s1"]


def test_consecutive_errors_backoff_and_pause_log(caplog):
    clock = FakeClock()

    async def poll(search):
        raise DivarHTTPError("دیوار پاسخ نداد", status=503)

    settings = _settings(max_consecutive_errors=3)
    scheduler = _scheduler([{"id": "s1", "interval": "5m"}], poll, settings=settings, clock=clock)
    schedule = scheduler.schedules[0]

    with caplog.at_level(logging.ERROR, logger="top_divar"):
        asyncio.run(scheduler.run_once())
        assert schedule.consecutive_errors == 1
        first_delay = schedule.next_due - clock.now
        assert first_delay == 600.0  # 300 × ۲¹

        clock.advance(first_delay)
        asyncio.run(scheduler.run_once())
        assert schedule.consecutive_errors == 2
        second_delay = schedule.next_due - clock.now
        assert second_delay == 1200.0  # 300 × ۲²

        clock.advance(second_delay)
        asyncio.run(scheduler.run_once())
        assert schedule.consecutive_errors == 3

    assert any("توقف موقت" in record.message for record in caplog.records)
    paused_delay = schedule.next_due - clock.now
    assert paused_delay == 2400.0


def test_error_backoff_capped():
    clock = FakeClock()

    async def poll(search):
        raise DivarHTTPError("دیوار پاسخ نداد", status=500)

    scheduler = _scheduler(
        [{"id": "s1", "interval": "1h"}],
        poll,
        settings=_settings(max_consecutive_errors=99),
        clock=clock,
    )
    schedule = scheduler.schedules[0]
    delay = 0.0
    for _ in range(12):
        asyncio.run(scheduler.run_once())
        delay = schedule.next_due - clock.now
        assert delay <= 3600.0
        clock.advance(delay)
    assert delay == 3600.0


def test_retry_after_is_honored():
    clock = FakeClock()

    async def poll(search):
        raise DivarHTTPError("محدودیت نرخ", status=429, retry_after="900")

    scheduler = _scheduler([{"id": "s1", "interval": "5m"}], poll, clock=clock)
    schedule = scheduler.schedules[0]
    asyncio.run(scheduler.run_once())
    assert schedule.next_due - clock.now == 900.0


def test_success_resets_consecutive_errors():
    clock = FakeClock()
    outcomes = [False, False, True, False]

    async def poll(search):
        if not outcomes.pop(0):
            raise DivarHTTPError("خطا", status=500)

    scheduler = _scheduler([{"id": "s1", "interval": "5m"}], poll, clock=clock)
    schedule = scheduler.schedules[0]
    asyncio.run(scheduler.run_once())
    clock.advance(schedule.next_due - clock.now)
    asyncio.run(scheduler.run_once())
    assert schedule.consecutive_errors == 2
    clock.advance(schedule.next_due - clock.now)
    asyncio.run(scheduler.run_once())  # موفقیت
    assert schedule.consecutive_errors == 0
    clock.advance(schedule.next_due - clock.now)
    asyncio.run(scheduler.run_once())  # دوباره خطا
    assert schedule.consecutive_errors == 1


def test_run_returns_immediately_when_stopped():
    clock = FakeClock()
    polled = []

    async def poll(search):
        polled.append(search["id"])

    scheduler = _scheduler([{"id": "s1"}], poll, clock=clock)
    stopped = asyncio.Event()
    stopped.set()
    asyncio.run(scheduler.run(stop=stopped))
    asyncio.run(scheduler.run(stop=lambda: True))
    assert polled == []


def test_run_polls_then_stops():
    clock = FakeClock()
    stop = asyncio.Event()

    async def poll(search):
        polled.append(search["id"])
        stop.set()

    polled = []
    scheduler = _scheduler([{"id": "s1"}], poll, clock=clock)
    asyncio.run(scheduler.run(stop=stop))
    assert polled == ["s1"]

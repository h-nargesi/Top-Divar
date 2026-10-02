"""تست گاردهای حافظه‌ای بات (مرحلهٔ ۷) — configuration.md بخش ۳.۱."""

from top_divar.bot.guards import (
    AWAITING_PASSWORD,
    AWAITING_USERNAME,
    GlobalPasswordCounter,
    PasswordThrottle,
    RegistrationSessions,
    ResendCooldowns,
    valid_username,
)


class FakeClock:
    def __init__(self, start=1000.0):
        self.now = start

    def __call__(self):
        return self.now

    def advance(self, seconds):
        self.now += seconds


def test_valid_username_rules():
    assert valid_username("alice")
    assert valid_username("a_9")
    assert valid_username("x" * 30)
    assert not valid_username("ab")  # کوتاه
    assert not valid_username("x" * 31)  # بلند
    assert not valid_username("Ali")  # حرف بزرگ
    assert not valid_username("ali-1")  # علامت غیرمجاز
    assert not valid_username("آلیس")
    assert not valid_username(None)


def test_sessions_timeout_drops_half_finished_conversation():
    clock = FakeClock()
    sessions = RegistrationSessions(clock=clock)
    assert sessions.start(7) == AWAITING_PASSWORD
    sessions.advance_to_username(7)
    assert sessions.get(7) == AWAITING_USERNAME
    clock.advance(10 * 60 + 1)  # تایم‌اوت ۱۰ دقیقه
    assert sessions.get(7) is None  # گفتگوی نیمه‌کاره انداخته شد
    sessions.start(7)
    sessions.clear(7)
    assert sessions.get(7) is None


def test_sessions_cleanup_drops_expired():
    clock = FakeClock()
    sessions = RegistrationSessions(clock=clock)
    sessions.start(1)
    sessions.start(2)
    clock.advance(11 * 60)
    sessions.start(3)
    sessions.cleanup()
    assert sessions.get(1) is None
    assert sessions.get(2) is None
    assert sessions.get(3) == AWAITING_PASSWORD


def test_password_throttle_blocks_after_five_failures_in_window():
    clock = FakeClock()
    throttle = PasswordThrottle(clock=clock)
    for index in range(4):
        failures = throttle.record_failure(7)
        assert failures == index + 1
        assert not throttle.is_blocked(7)
    throttle.record_failure(7)
    assert throttle.is_blocked(7)
    assert 0 < throttle.blocked_for_seconds(7) <= 30 * 60
    # پنجرهٔ تازه بعد از ۱۰ دقیقه — ولی بلاک ۳۰ دقیقه‌ای سر جایش است
    clock.advance(11 * 60)
    assert throttle.is_blocked(7)
    clock.advance(20 * 60)
    assert not throttle.is_blocked(7)


def test_password_throttle_window_slides():
    clock = FakeClock()
    throttle = PasswordThrottle(clock=clock)
    for _ in range(4):
        throttle.record_failure(7)
    clock.advance(11 * 60)  # تلاش‌ها از پنجره بیرون رفتند
    assert throttle.record_failure(7) == 1
    assert not throttle.is_blocked(7)


def test_password_throttle_per_chat_isolation():
    clock = FakeClock()
    throttle = PasswordThrottle(clock=clock)
    for _ in range(5):
        throttle.record_failure(7)
    assert throttle.is_blocked(7)
    assert not throttle.is_blocked(8)
    # reset فقط پنجرهٔ خطاها را پاک می‌کند؛ بلاک ۳۰ دقیقه‌ای سر جایش است
    throttle.reset(7)
    assert throttle.is_blocked(7)
    clock.advance(31 * 60)
    assert not throttle.is_blocked(7)


def test_global_counter_alerts_once_per_threshold():
    clock = FakeClock()
    counter = GlobalPasswordCounter(clock=clock)
    alerted = 0
    for _ in range(20):
        if counter.record_failure():
            alerted += 1
    assert alerted == 1
    # تلاش بعدی هنوز بالای آستانه است ولی هشدار تکرار نمی‌شود
    assert counter.record_failure() is False
    clock.advance(11 * 60)  # پنجره خالی شد
    for _ in range(20):
        if counter.record_failure():
            alerted += 1
    assert alerted == 2


def test_resend_cooldown_ten_minutes():
    clock = FakeClock()
    cooldowns = ResendCooldowns(clock=clock)
    assert cooldowns.check_and_set("alice") == 0.0
    remaining = cooldowns.check_and_set("alice")
    assert 0 < remaining <= 10 * 60
    # کاربر دیگری محدود نیست
    assert cooldowns.check_and_set("bob") == 0.0
    clock.advance(10 * 60 + 1)
    assert cooldowns.check_and_set("alice") == 0.0

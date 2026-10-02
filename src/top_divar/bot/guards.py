"""گاردهای حافظه‌ای درگاه بات (مرحلهٔ ۷) — configuration.md بخش ۳.۱.

همهٔ stateها فقط در حافظهٔ پروسه‌اند: ری‌استارت سرویس گفتگوی نیمه‌کاره
را می‌اندازد و کاربر دوباره /start می‌زند (ADR-0010 — ذخیره در
دیتابیس لازم نیست). ساعت تزریق‌پذیر است تا تست‌ها زمان را جلو ببرند.
"""

import re
import time

USERNAME_PATTERN = re.compile(r"^[a-z0-9_]{3,30}$")

AWAITING_PASSWORD = "password"
AWAITING_USERNAME = "username"

SESSION_TIMEOUT_SECONDS = 10 * 60
PASSWORD_MAX_FAILURES = 5
PASSWORD_FAILURE_WINDOW_SECONDS = 10 * 60
PASSWORD_BLOCK_SECONDS = 30 * 60
GLOBAL_PASSWORD_THRESHOLD = 20
GLOBAL_PASSWORD_WINDOW_SECONDS = 10 * 60
RESEND_COOLDOWN_SECONDS = 10 * 60


def valid_username(text) -> bool:
    """قواعد username: ^[a-z0-9_]{3,30}$ (بخش ۳.۱)."""
    return isinstance(text, str) and bool(USERNAME_PATTERN.fullmatch(text.strip()))


class _SlidingWindow:
    """پنجرهٔ لغزان مهرهای زمانی (monotonic)."""

    def __init__(self, window_seconds: float, clock=None):
        self.window_seconds = float(window_seconds)
        self._clock = clock or time.monotonic
        self._events = []

    def _prune(self) -> None:
        now = self._clock()
        self._events = [t for t in self._events if now - t < self.window_seconds]

    def record(self) -> int:
        """ثبت رویداد تازه؛ خروجی: تعداد رویدادهای پنجره."""
        self._prune()
        self._events.append(self._clock())
        return len(self._events)

    def count(self) -> int:
        self._prune()
        return len(self._events)


class RegistrationSessions:
    """وضعیت گفتگوی ثبت‌نام: انتظار پسورد / انتظار username.

    فقط در حافظه؛ هر ورودی ۱۰ دقیقه بعد منقضی می‌شود.
    """

    AWAITING_PASSWORD = AWAITING_PASSWORD
    AWAITING_USERNAME = AWAITING_USERNAME

    def __init__(self, *, timeout_seconds: float = SESSION_TIMEOUT_SECONDS, clock=None):
        self._timeout = float(timeout_seconds)
        self._clock = clock or time.monotonic
        self._sessions = {}

    def start(self, chat_id) -> str:
        """شروع گفتگوی تازه (یا بازنشانی گفتگوی قبلی) در انتظار پسورد."""
        self._sessions[chat_id] = {
            "state": self.AWAITING_PASSWORD,
            "started_at": self._clock(),
        }
        return self.AWAITING_PASSWORD

    def get(self, chat_id):
        """وضعیت جاری گفتگو؛ منقضی‌شده حذف و None برمی‌گردد."""
        session = self._sessions.get(chat_id)
        if session is None:
            return None
        if self._clock() - session["started_at"] > self._timeout:
            del self._sessions[chat_id]
            return None
        return session["state"]

    def advance_to_username(self, chat_id) -> None:
        session = self._sessions.get(chat_id)
        if session is not None:
            session["state"] = self.AWAITING_USERNAME
            session["started_at"] = self._clock()

    def clear(self, chat_id) -> None:
        self._sessions.pop(chat_id, None)

    def cleanup(self) -> None:
        """حذف ورودی‌های منقضی — فراخوانی دوره‌ای درگاه."""
        now = self._clock()
        expired = [
            chat_id
            for chat_id, session in self._sessions.items()
            if now - session["started_at"] > self._timeout
        ]
        for chat_id in expired:
            del self._sessions[chat_id]


class PasswordThrottle:
    """۵ تلاش ناموفق پسورد در ۱۰ دقیقه به‌ازای هر chat → بلاک ۳۰ دقیقه."""

    def __init__(
        self,
        *,
        max_failures: int = PASSWORD_MAX_FAILURES,
        window_seconds: float = PASSWORD_FAILURE_WINDOW_SECONDS,
        block_seconds: float = PASSWORD_BLOCK_SECONDS,
        clock=None,
    ):
        self.max_failures = int(max_failures)
        self._block = float(block_seconds)
        self._clock = clock or time.monotonic
        self._windows = {}
        self._blocked_until = {}

    def is_blocked(self, chat_id) -> bool:
        until = self._blocked_until.get(chat_id)
        if until is None:
            return False
        if self._clock() >= until:
            del self._blocked_until[chat_id]
            return False
        return True

    def blocked_for_seconds(self, chat_id) -> float:
        until = self._blocked_until.get(chat_id)
        if until is None:
            return 0.0
        return max(0.0, until - self._clock())

    def record_failure(self, chat_id) -> int:
        """ثبت تلاش ناموفق؛ خروجی: تعداد تلاش‌های پنجره. بلاک را روشن می‌کند."""
        window = self._windows.get(chat_id)
        if window is None:
            window = _SlidingWindow(
                PASSWORD_FAILURE_WINDOW_SECONDS, clock=self._clock
            )
            self._windows[chat_id] = window
        failures = window.record()
        if failures >= self.max_failures:
            self._blocked_until[chat_id] = self._clock() + self._block
            self._windows.pop(chat_id, None)
        return failures

    def reset(self, chat_id) -> None:
        self._windows.pop(chat_id, None)


class GlobalPasswordCounter:
    """شمارندهٔ سراسری خطای پسورد بین همهٔ chatها (بخش ۳.۱).

    عبور از آستانهٔ ~۲۰ در ۱۰ دقیقه → هشدار اپراتور (بروت‌فورس).
    `record_failure` فقط یک بار در هر پنجره هشدار می‌دهد.
    """

    def __init__(
        self,
        *,
        threshold: int = GLOBAL_PASSWORD_THRESHOLD,
        window_seconds: float = GLOBAL_PASSWORD_WINDOW_SECONDS,
        clock=None,
    ):
        self._threshold = int(threshold)
        self._clock = clock or time.monotonic
        self._window = _SlidingWindow(window_seconds, clock=self._clock)
        self._last_alert = None

    def count(self) -> int:
        """تعداد تلاش‌های ناموفق پنجرهٔ جاری."""
        return self._window.count()

    def record_failure(self) -> bool:
        """ثبت تلاش ناموفق تازه؛ True یعنی وقت هشدار به اپراتور."""
        count = self._window.record()
        if count < self._threshold:
            return False
        now = self._clock()
        if (
            self._last_alert is not None
            and now - self._last_alert < self._window.window_seconds
        ):
            return False
        self._last_alert = now
        return True


class ResendCooldowns:
    """cooldown ‏۱۰ دقیقه per user برای /resend (state در حافظه)."""

    def __init__(
        self,
        *,
        cooldown_seconds: float = RESEND_COOLDOWN_SECONDS,
        clock=None,
    ):
        self._cooldown = float(cooldown_seconds)
        self._clock = clock or time.monotonic
        self._until = {}

    def check_and_set(self, key) -> float:
        """اگر مجاز است cooldown را روشن کند و ۰ برگرداند؛ وگرنه ثانیهٔ باقی‌مانده."""
        now = self._clock()
        until = self._until.get(key)
        if until is not None and now < until:
            return until - now
        self._until[key] = now + self._cooldown
        return 0.0

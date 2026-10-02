"""درگاه بات تلگرام (مرحلهٔ ۷) — ADR-0010 + configuration.md بخش ۳.۱.

- long-polling «getUpdates» با دامنهٔ مینیمال: ثبت‌نام (/start → پسورد →
  username یونیک) و دستورهای /resend، /help، /status
- جبران تعاملی: هر پیام متنی کاربرِ ثبت‌شده، pendingهای او را فوری
  می‌فرستد — بی‌تاب به backoff ردیف‌محور (G5)، dead برنمی‌گردد
- /resend YYYY/MM/DD: ممتازهای از آن تاریخ شمسی فقط به خود کاربر؛
  سقف ۳۰ روز، cooldown ‏۱۰ دقیقه (حافظه)، مستقل از جدول delivery
- 409 تلگرام گذرا است: backoff کوتاه و ادامهٔ polling (نه کرش)
"""

import asyncio
import datetime
import hmac
import math
import threading

from top_divar.bot.client import TelegramBotClient
from top_divar.bot.guards import (
    AWAITING_PASSWORD,
    AWAITING_USERNAME,
    GlobalPasswordCounter,
    PasswordThrottle,
    RegistrationSessions,
    ResendCooldowns,
    valid_username,
)
from top_divar.divar.jalali import (
    jalali_start_of_day_utc,
    jalali_today,
    parse_jalali_date,
)
from top_divar.notify.errors import SendError
from top_divar.notify.message import build_telegram_message, to_persian_digits
from top_divar.notify.planner import resolve_search_label
from top_divar.shared.logging import get_logger
from top_divar.storage.errors import DuplicateUsernameError
from top_divar.storage.timestamps import utc_now

_log = get_logger("bot.gateway")

RESEND_WINDOW_DAYS = 30
LONG_POLL_TIMEOUT_SECONDS = 25
POLL_ERROR_BACKOFF_SECONDS = 5.0
RETRY_AFTER_CAP_SECONDS = 60.0
MESSAGE_PAUSE_SECONDS = 1.0
EMPTY_POLL_PAUSE_SECONDS = 0.5

HELP_TEXT = (
    "دستورهای بات:\n"
    "/start — شروع یا ادامهٔ ثبت‌نام؛ ارسال پیام‌های در انتظار\n"
    "/resend YYYY/MM/DD — ارسال دوبارهٔ آگهی‌های ممتاز از یک تاریخ شمسی "
    "(حداکثر ۳۰ روز گذشته)\n"
    "/status — نام کاربری و تعداد پیام‌های در انتظار شما\n"
    "/help — همین راهنما"
)

MSG_ASK_PASSWORD = "پسورد مشترک ثبت‌نام را بفرستید."
MSG_ASK_USERNAME = (
    "پسورد درست است. حالا یک نام کاربری انتخاب و بفرستید "
    "(حروف کوچک انگلیسی، رقم و _؛ ۳ تا ۳۰ کاراکتر)."
)
MSG_USERNAME_INVALID = (
    "نام کاربری معتبر نیست؛ فقط حروف کوچک انگلیسی، رقم و _ "
    "(۳ تا ۳۰ کاراکتر). یکی دیگر بفرستید."
)
MSG_USERNAME_TAKEN = "این نام کاربری قبلاً گرفته شده؛ یکی دیگر انتخاب کنید."
MSG_REGISTERED = "ثبت‌نام کامل شد. خوش آمدید {username}!"
MSG_ALREADY_REGISTERED = (
    "شما با نام کاربری {username} ثبت‌نام کرده‌اید؛ "
    "پیام‌های در انتظار همین حالا ارسال می‌شوند."
)
MSG_NOT_REGISTERED = "اول ثبت‌نام کنید: /start"
MSG_HINT_START = "برای ثبت‌نام، /start را بفرستید."
MSG_UNKNOWN_COMMAND = "دستور ناشناخته است. /help را ببینید."
MSG_WRONG_PASSWORD = "پسورد نادرست است. {remaining} تلاش دیگر در ۱۰ دقیقه باقی مانده."
MSG_BLOCKED = (
    "تلاش‌های ناموفق زیاد بود؛ حدود {minutes} دقیقه دیگر دوباره /start بزنید."
)
MSG_RESEND_USAGE = (
    "فرمت درست: /resend 1405/06/01 — تاریخ شمسی، حداکثر ۳۰ روز گذشته."
)
MSG_RESEND_FUTURE = "تاریخ نمی‌تواند در آینده باشد."
MSG_RESEND_TOO_OLD = "سقف ارسال مجدد ۳۰ روز است؛ تاریخ جدیدتری بدهید."
MSG_RESEND_COOLDOWN = (
    "این دستور تازه اجرا شده؛ حدود {minutes} دقیقه دیگر دوباره تلاش کنید."
)
MSG_RESEND_EMPTY = "آگهی ممتازی از این تاریخ به بعد پیدا نشد."
MSG_RESEND_DONE = "{count} آگهی ارسال شد."
MSG_RESEND_DONE_WITH_FAILURES = "{count} آگهی ارسال شد؛ {failures} پیام خطا خورد."
MSG_STATUS = "نام کاربری: {username}\nپیام‌های در انتظار: {pending}"


def minutes_text(seconds: float) -> str:
    """دقیقهٔ گردشده به رقم فارسی برای پیام‌های کاربر."""
    return to_persian_digits(max(1, math.ceil(seconds / 60)))


def poll_error_delay(exc: SendError) -> float:
    """تأخیر بعد از خطای getUpdates: retry_after (سقف ۶۰) وگرنه backoff کوتاه."""
    if exc.retry_after is not None and float(exc.retry_after) > 0:
        return min(float(exc.retry_after), RETRY_AFTER_CAP_SECONDS)
    return POLL_ERROR_BACKOFF_SECONDS


class BotGateway:
    """پاسخ به به‌روزهای بات + محرک جبران pendingهای کاربر."""

    def __init__(
        self,
        repository,
        client: TelegramBotClient,
        *,
        password: str,
        ad_sender=None,
        sweeper=None,
        ops_chat_id=None,
        searches_by_id: dict = None,
        backfill_days: int = 7,
        resend_window_days: int = RESEND_WINDOW_DAYS,
        sleeper=None,
        today_provider=None,
        sessions: RegistrationSessions = None,
        throttle: PasswordThrottle = None,
        global_counter: GlobalPasswordCounter = None,
        resend_cooldowns: ResendCooldowns = None,
    ):
        if not isinstance(password, str) or not password:
            raise ValueError("پسورد ثبت‌نام بات لازم است (TELEGRAM_BOT_PASSWORD).")
        self._repository = repository
        self._client = client
        self._password = password
        self._ad_sender = ad_sender
        self._sweeper = sweeper
        self._ops_chat_id = ops_chat_id
        self._searches_by_id = dict(searches_by_id or {})
        self._backfill_days = int(backfill_days)
        self._resend_window_days = int(resend_window_days)
        self._sleeper = sleeper or asyncio.sleep
        self._today_provider = today_provider or jalali_today
        self._sessions = sessions or RegistrationSessions()
        self._throttle = throttle or PasswordThrottle()
        self._global_counter = global_counter or GlobalPasswordCounter()
        self._resend_cooldowns = resend_cooldowns or ResendCooldowns()
        self._offset = 0

    def apply_config(self, searches_by_id: dict, *, backfill_days: int) -> None:
        """به‌روزرسانی زندهٔ برچسب جستجوها و پنجرهٔ جبران بعد از SIGHUP."""
        self._searches_by_id = dict(searches_by_id or {})
        self._backfill_days = int(backfill_days)

    def set_sweeper(self, sweeper) -> None:
        """وصل/جدا کردن جارو بعد از تغییر کانال‌ها در reload."""
        self._sweeper = sweeper

    async def run(self, stop=None) -> None:
        """حلقهٔ long polling تا set شدن stop — 409 گذرا و backoff کوتاه."""
        while not _is_stopped(stop):
            self._sessions.cleanup()
            try:
                updates = await self._client.get_updates(
                    offset=self._offset or None,
                    timeout=LONG_POLL_TIMEOUT_SECONDS,
                )
            except SendError as exc:
                delay = poll_error_delay(exc)
                _log.warning(
                    "خطای گذرای getUpdates (احتمال 409 تزاحم)؛ %s ثانیه دیگر ادامه می‌دهیم: %s",
                    delay,
                    exc,
                    extra={
                        "fields": {
                            "event": "bot_poll_failed",
                            "category": exc.category,
                            "backoff_seconds": delay,
                        }
                    },
                )
                await self._sleeper(delay)
                continue
            if not updates:
                await self._sleeper(EMPTY_POLL_PAUSE_SECONDS)
                continue
            for update in updates:
                self._advance_offset(update)
                try:
                    await self.handle_update(update)
                except Exception as exc:  # noqa: BLE001 - یک به‌روز خراب بات را نمی‌خواباند
                    _log.error(
                        "پردازش به‌روز بات شکست خورد: %s",
                        exc,
                        extra={"fields": {"event": "bot_update_failed", "error": str(exc)}},
                    )

    def _advance_offset(self, update: dict) -> None:
        update_id = update.get("update_id")
        if isinstance(update_id, int):
            self._offset = max(self._offset, update_id + 1)

    async def handle_update(self, update: dict) -> None:
        """گوش دادن فقط به پیام‌های متنی (دامنهٔ مینیمال — ADR-0010)."""
        if not isinstance(update, dict):
            return
        message = update.get("message")
        if not isinstance(message, dict):
            return
        chat = message.get("chat")
        chat_id = chat.get("id") if isinstance(chat, dict) else None
        text = message.get("text")
        if chat_id is None or not isinstance(text, str) or not text.strip():
            return
        await self.handle_text(chat_id, text.strip())

    async def handle_text(self, chat_id, text: str) -> None:
        user = await self._repository.get_user_by_chat_id(chat_id)
        if user is not None:
            # هر پیام متنی کاربر ثبت‌شده محرک جبران است (ADR-0010 — G5)
            await self._backfill(user)
        if text.startswith("/"):
            command, _, args = text.partition(" ")
            command = command[1:].split("@", 1)[0].lower()
            await self._dispatch_command(command, args.strip(), chat_id, user)
            return
        if user is not None:
            return
        state = self._sessions.get(chat_id)
        if state == AWAITING_PASSWORD:
            await self._handle_password_input(chat_id, text)
        elif state == AWAITING_USERNAME:
            await self._handle_username_input(chat_id, text)
        else:
            await self._reply(chat_id, MSG_HINT_START)

    async def _dispatch_command(
        self, command: str, args: str, chat_id, user
    ) -> None:
        if command == "start":
            await self._cmd_start(chat_id, user)
        elif command == "resend":
            await self._cmd_resend(args, chat_id, user)
        elif command == "help":
            await self._reply(chat_id, HELP_TEXT)
        elif command == "status":
            await self._cmd_status(chat_id, user)
        else:
            await self._reply(
                chat_id,
                MSG_UNKNOWN_COMMAND if user is not None else MSG_NOT_REGISTERED,
            )

    async def _cmd_start(self, chat_id, user) -> None:
        if user is not None:
            await self._reply(
                chat_id, MSG_ALREADY_REGISTERED.format(username=user["username"])
            )
            return
        if self._throttle.is_blocked(chat_id):
            await self._reply(
                chat_id,
                MSG_BLOCKED.format(
                    minutes=minutes_text(self._throttle.blocked_for_seconds(chat_id))
                ),
            )
            return
        self._sessions.start(chat_id)
        await self._reply(chat_id, MSG_ASK_PASSWORD)

    async def _cmd_status(self, chat_id, user) -> None:
        if user is None:
            await self._reply(chat_id, MSG_NOT_REGISTERED)
            return
        pending = await self._repository.count_pending_deliveries(
            channel="telegram", recipient=str(chat_id)
        )
        await self._reply(
            chat_id,
            MSG_STATUS.format(
                username=user["username"],
                pending=to_persian_digits(pending),
            ),
        )

    async def _cmd_resend(self, args: str, chat_id, user) -> None:
        if user is None:
            await self._reply(chat_id, MSG_NOT_REGISTERED)
            return
        date = parse_jalali_date(args)
        if date is None:
            await self._reply(chat_id, MSG_RESEND_USAGE)
            return
        start_utc = jalali_start_of_day_utc(*date)
        today_utc = jalali_start_of_day_utc(*self._today_provider())
        if start_utc > today_utc:
            await self._reply(chat_id, MSG_RESEND_FUTURE)
            return
        window = datetime.timedelta(days=self._resend_window_days)
        if today_utc - start_utc > window:
            await self._reply(chat_id, MSG_RESEND_TOO_OLD)
            return
        rows = await self._repository.get_notable_ads_since(start_utc)
        if not rows:
            await self._reply(chat_id, MSG_RESEND_EMPTY)
            return
        remaining = self._resend_cooldowns.check_and_set(chat_id)
        if remaining > 0:
            await self._reply(
                chat_id, MSG_RESEND_COOLDOWN.format(minutes=minutes_text(remaining))
            )
            return
        sent = 0
        failures = 0
        for index, ad in enumerate(rows):
            label = await resolve_search_label(
                self._repository, self._searches_by_id, ad["id"]
            )
            try:
                await self._send_ad(chat_id, ad, label)
                sent += 1
            except SendError as exc:
                failures += 1
                _log.warning(
                    "ارسال مجدد آگهی %s به %s شکست خورد: %s",
                    ad.get("token"),
                    chat_id,
                    exc,
                    extra={
                        "fields": {
                            "event": "resend_send_failed",
                            "token": ad.get("token"),
                            "chat_id": chat_id,
                            "error": str(exc),
                        }
                    },
                )
            if index + 1 < len(rows):
                await self._sleeper(MESSAGE_PAUSE_SECONDS)
        if failures:
            await self._reply(
                chat_id,
                MSG_RESEND_DONE_WITH_FAILURES.format(
                    count=to_persian_digits(sent),
                    failures=to_persian_digits(failures),
                ),
            )
        else:
            await self._reply(
                chat_id, MSG_RESEND_DONE.format(count=to_persian_digits(sent))
            )
        _log.info(
            "ارسال مجدد از تاریخ %s برای کاربر %s تمام شد.",
            args,
            user["username"],
            extra={
                "fields": {
                    "event": "resend_finished",
                    "username": user["username"],
                    "chat_id": chat_id,
                    "sent": sent,
                    "failures": failures,
                }
            },
        )

    async def _send_ad(self, chat_id, ad: dict, label: str) -> None:
        if self._ad_sender is None:
            raise SendError(
                category="transient",
                message="ارسال‌کنندهٔ پیام آگهی در دسترس نیست (کانال telegram غیرفعال است).",
            )
        await self._ad_sender(chat_id, build_telegram_message(ad, label))

    async def _handle_password_input(self, chat_id, text: str) -> None:
        if self._throttle.is_blocked(chat_id):
            self._sessions.clear(chat_id)
            await self._reply(
                chat_id,
                MSG_BLOCKED.format(
                    minutes=minutes_text(self._throttle.blocked_for_seconds(chat_id))
                ),
            )
            return
        if hmac.compare_digest(text.encode(), self._password.encode()):
            self._throttle.reset(chat_id)
            self._sessions.advance_to_username(chat_id)
            await self._reply(chat_id, MSG_ASK_USERNAME)
            return
        failures = self._throttle.record_failure(chat_id)
        _log.warning(
            "تلاش ناموفق پسورد ثبت‌نام در chat %s.",
            chat_id,
            extra={
                "fields": {
                    "event": "registration_password_failed",
                    "chat_id": chat_id,
                    "failures_in_window": failures,
                }
            },
        )
        if self._throttle.is_blocked(chat_id):
            self._sessions.clear(chat_id)
            await self._reply(
                chat_id,
                MSG_BLOCKED.format(
                    minutes=minutes_text(self._throttle.blocked_for_seconds(chat_id))
                ),
            )
        else:
            remaining_attempts = max(
                1, self._throttle.max_failures - failures
            )
            await self._reply(
                chat_id,
                MSG_WRONG_PASSWORD.format(
                    remaining=to_persian_digits(remaining_attempts)
                ),
            )
        if self._global_counter.record_failure():
            count = self._global_counter.count()
            await self._alert_ops(
                "هشدار: تلاش ناموفق پسورد ثبت‌نام در بات به "
                f"{count} رسیده (۱۰ دقیقهٔ اخیر) — احتمال بروت‌فورس."
            )

    async def _handle_username_input(self, chat_id, text: str) -> None:
        username = text.strip()
        if not valid_username(username):
            await self._reply(chat_id, MSG_USERNAME_INVALID)
            return
        try:
            await self._repository.add_user(username, chat_id)
        except DuplicateUsernameError:
            await self._reply(chat_id, MSG_USERNAME_TAKEN)
            return
        self._sessions.clear(chat_id)
        _log.info(
            "کاربر تازه ثبت‌نام کرد: %s (chat %s).",
            username,
            chat_id,
            extra={
                "fields": {
                    "event": "user_registered",
                    "username": username,
                    "chat_id": chat_id,
                }
            },
        )
        await self._reply(chat_id, MSG_REGISTERED.format(username=username))

    async def _backfill(self, user: dict) -> None:
        """جبران pendingهای کاربر: فوری، قدیمی‌ترین اول، سقف پنجرهٔ کانفیگ."""
        if self._sweeper is None:
            return
        since = utc_now() - datetime.timedelta(days=self._backfill_days)
        try:
            result = await self._sweeper.backfill_recipient(
                "telegram", str(user["chat_id"]), since=since
            )
        except Exception as exc:  # noqa: BLE001 - جبران شکسته سرویس را نمی‌خواباند
            _log.error(
                "جبران pendingهای کاربر %s شکست خورد: %s",
                user.get("username"),
                exc,
                extra={
                    "fields": {
                        "event": "backfill_failed",
                        "username": user.get("username"),
                    }
                },
            )
            return
        if result.attempted:
            _log.info(
                "جبران تعاملی کاربر %s تمام شد.",
                user.get("username"),
                extra={
                    "fields": {
                        "event": "backfill_finished",
                        "username": user.get("username"),
                        "chat_id": user.get("chat_id"),
                        "attempted": result.attempted,
                        "sent": result.sent,
                        "dead": result.dead,
                    }
                },
            )

    async def _alert_ops(self, text: str) -> None:
        _log.error(
            text,
            extra={"fields": {"event": "ops_alert_password_bruteforce"}},
        )
        if not self._ops_chat_id:
            return
        try:
            await self._client.send_message(self._ops_chat_id, text)
        except SendError as exc:
            _log.error(
                "ارسال هشدار به اپراتور شکست خورد: %s",
                exc,
                extra={"fields": {"event": "ops_alert_send_failed"}},
            )

    async def _reply(self, chat_id, text: str) -> None:
        try:
            await self._client.send_message(chat_id, text)
        except SendError as exc:
            _log.warning(
                "پاسخ بات به %s ارسال نشد: %s",
                chat_id,
                exc,
                extra={
                    "fields": {
                        "event": "bot_reply_failed",
                        "chat_id": chat_id,
                        "error": str(exc),
                    }
                },
            )


def _is_stopped(stop) -> bool:
    if stop is None:
        return False
    if isinstance(stop, (asyncio.Event, threading.Event)):
        return stop.is_set()
    if callable(stop):
        return bool(stop())
    return bool(stop)

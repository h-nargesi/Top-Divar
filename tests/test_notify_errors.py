"""تست طبقه‌بندی خطاهای ارسال (مرحلهٔ ۶) — ADR-0010 اصلاح ۲۰۲۶-۰۹-۱۸."""

import asyncio
import json

import pytest

from top_divar.notify.errors import (
    ETERNAL,
    RESURRECTABLE,
    TRANSIENT,
    SendError,
    classify_smtp_code,
    classify_telegram_status,
)
from top_divar.notify.telegram import TelegramNotifier


def test_telegram_status_classification():
    assert classify_telegram_status(403) == ETERNAL       # بلاک/بلاک‌شده
    assert classify_telegram_status(400) == ETERNAL       # پارامتر بد
    assert classify_telegram_status(429) == RESURRECTABLE  # بعد از تلاش مجدد
    assert classify_telegram_status(500) == TRANSIENT
    assert classify_telegram_status(502) == TRANSIENT
    assert classify_telegram_status(418) == TRANSIENT     # ناشناخته → گذرا
    assert classify_telegram_status(None) == TRANSIENT
    assert classify_telegram_status("garbage") == TRANSIENT


def test_smtp_code_classification():
    assert classify_smtp_code(550) == ETERNAL   # گیرنده نامعتبر
    assert classify_smtp_code(535) == ETERNAL   # احراز هویت دائم
    assert classify_smtp_code(421) == RESURRECTABLE  # انقضای موقت
    assert classify_smtp_code(450) == RESURRECTABLE
    assert classify_smtp_code(250) == TRANSIENT
    assert classify_smtp_code(None) == TRANSIENT
    assert classify_smtp_code("xxx") == TRANSIENT


def test_send_error_str_and_fields():
    exc = SendError(category=ETERNAL, message="رد شد", retry_after=3)
    assert str(exc) == "رد شد"
    assert exc.category == ETERNAL
    assert exc.retry_after == 3


class RecordedTransport:
    """ضبط‌شدهٔ پاسخ‌های Bot API برای تست ارسال آزمایشی."""

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    async def __call__(self, method, url, headers, body=None):
        self.calls.append((method, url, headers, json.loads(body.decode("utf-8"))))
        response = self.responses.pop(0)
        status, payload = response
        return status, {}, json.dumps(payload).encode("utf-8")


class FakeSleeper:
    def __init__(self):
        self.waited = []

    async def __call__(self, seconds):
        self.waited.append(seconds)


def _ok_payload():
    return {"ok": True, "result": {"message_id": 42}}


def test_send_message_success_marks_ok(tmp_path):
    sleeper = FakeSleeper()
    transport = RecordedTransport([(200, _ok_payload())])
    notifier = TelegramNotifier("TOK", transport=transport, sleeper=sleeper)
    message_id = asyncio.run(notifier.send_message(123, "<b>سلام</b>"))
    assert message_id == 42
    method, url, headers, payload = transport.calls[0]
    assert method == "POST"
    assert url == "https://api.telegram.org/botTOK/sendMessage"
    assert payload["chat_id"] == 123
    assert payload["parse_mode"] == "HTML"
    assert payload["disable_web_page_preview"] is True
    assert payload["text"] == "<b>سلام</b>"
    assert sleeper.waited == []  # موفقیت یعنی بدون انتظار


def test_send_message_429_retries_once_after_retry_after():
    sleeper = FakeSleeper()
    transport = RecordedTransport(
        [
            (
                429,
                {
                    "ok": False,
                    "error_code": 429,
                    "description": "Too Many Requests",
                    "parameters": {"retry_after": 7},
                },
            ),
            (200, _ok_payload()),
        ],
    )
    notifier = TelegramNotifier("TOK", transport=transport, sleeper=sleeper)
    message_id = asyncio.run(notifier.send_message(1, "text"))
    assert message_id == 42
    assert sleeper.waited == [7]  # انتظار retry_after + یک تلاش مجدد همان پیام
    assert len(transport.calls) == 2
    assert transport.calls[0][3]["text"] == transport.calls[1][3]["text"]


def test_send_message_429_retry_after_capped_at_60():
    sleeper = FakeSleeper()
    transport = RecordedTransport(
        [
            (429, {"ok": False, "error_code": 429,
                   "description": "x", "parameters": {"retry_after": 300}}),
            (200, _ok_payload()),
        ],
    )
    notifier = TelegramNotifier("TOK", transport=transport, sleeper=sleeper)
    asyncio.run(notifier.send_message(1, "text"))
    assert sleeper.waited == [60]


def test_send_message_repeated_429_is_resurrectable():
    sleeper = FakeSleeper()
    transport = RecordedTransport(
        [
            (429, {"ok": False, "error_code": 429,
                   "description": "x", "parameters": {"retry_after": 5}}),
            (429, {"ok": False, "error_code": 429,
                   "description": "x", "parameters": {"retry_after": 5}}),
        ],
    )
    notifier = TelegramNotifier("TOK", transport=transport, sleeper=sleeper)
    with pytest.raises(SendError) as excinfo:
        asyncio.run(notifier.send_message(1, "text"))
    assert excinfo.value.category == RESURRECTABLE
    assert excinfo.value.retry_after == 5


def test_send_message_403_is_eternal_without_retry():
    sleeper = FakeSleeper()
    transport = RecordedTransport(
        [(403, {"ok": False, "error_code": 403, "description": "Forbidden: bot was blocked"})],
    )
    notifier = TelegramNotifier("TOK", transport=transport, sleeper=sleeper)
    with pytest.raises(SendError) as excinfo:
        asyncio.run(notifier.send_message(1, "text"))
    assert excinfo.value.category == ETERNAL
    assert "Forbidden" in str(excinfo.value)
    assert len(transport.calls) == 1


def test_send_message_400_is_eternal():
    transport = RecordedTransport(
        [(400, {"ok": False, "error_code": 400, "description": "Bad Request"})],
    )
    notifier = TelegramNotifier("TOK", transport=transport, sleeper=FakeSleeper())
    with pytest.raises(SendError) as excinfo:
        asyncio.run(notifier.send_message(1, "<i>خراب</b>"))
    assert excinfo.value.category == ETERNAL


def test_send_message_5xx_is_transient():
    transport = RecordedTransport([(502, {"ok": False, "error_code": 502})])
    notifier = TelegramNotifier("TOK", transport=transport, sleeper=FakeSleeper())
    with pytest.raises(SendError) as excinfo:
        asyncio.run(notifier.send_message(1, "text"))
    assert excinfo.value.category == TRANSIENT


def test_send_message_network_error_is_transient():
    class BrokenTransport:
        async def __call__(self, method, url, headers, body=None):
            raise SendError(category=TRANSIENT, message="خطای شبکه")

    notifier = TelegramNotifier("TOK", transport=BrokenTransport(), sleeper=FakeSleeper())
    with pytest.raises(SendError) as excinfo:
        asyncio.run(notifier.send_message(1, "text"))
    assert excinfo.value.category == TRANSIENT


def test_empty_token_rejected():
    with pytest.raises(ValueError):
        TelegramNotifier("  ")

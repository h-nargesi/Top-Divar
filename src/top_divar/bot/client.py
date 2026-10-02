"""کلاینت Bot API تلگرام برای درگاه بات (مرحلهٔ ۷) — ADR-0002/0010.

`getUpdates` (long polling) و `sendMessage` متن ساده برای پاسخ
دستورها؛ پروکسی HTTPS_PROXY روی همهٔ فراخوانی‌ها (ADR-0002). خطاها
با همان طبقه‌بندی سه‌دستهٔ ارسال برمی‌گردند؛ 409 تلگرام در
getUpdates گذرا تلقی می‌شود و درگاه با backoff کوتاه ادامه می‌دهد.
"""

import json

from top_divar.notify.errors import SendError, classify_telegram_status
from top_divar.notify.telegram import (
    DEFAULT_TIMEOUT_SECONDS,
    TELEGRAM_API_BASE,
    UrllibTransport,
    extract_error_fields,
)


class TelegramBotClient:
    """فراخوانی متدهای Bot API؛ خروجی فیلد result پاسخ موفق."""

    def __init__(
        self,
        bot_token: str,
        *,
        proxy: str = None,
        transport=None,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
    ):
        if not isinstance(bot_token, str) or not bot_token.strip():
            raise ValueError("توکن ربات تلگرام باید رشتهٔ غیرخالی باشد.")
        self._base_url = f"{TELEGRAM_API_BASE}/bot{bot_token.strip()}"
        self._transport = transport or UrllibTransport(proxy=proxy, timeout=timeout)

    async def call(self, method: str, payload: dict) -> dict:
        """فراخوانی یک متد Bot API؛ شکست → SendError طبقه‌بندی‌شده."""
        url = f"{self._base_url}/{method}"
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        status, _, response_body = await self._transport(
            "POST", url, {"content-type": "application/json"}, body
        )
        data = None
        try:
            data = json.loads(response_body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            pass
        if status == 200 and isinstance(data, dict) and data.get("ok"):
            result = data.get("result")
            return result if isinstance(result, dict) else {}

        error_code, description, retry_after = extract_error_fields(status, data)
        raise SendError(
            category=classify_telegram_status(error_code),
            message=f"فراخوانی {method} تلگرام شکست خورد (وضعیت {error_code}"
            + (f": {description}" if description else "")
            + ").",
            retry_after=retry_after,
        )

    async def get_updates(
        self,
        *,
        offset: int = None,
        timeout: float = 0,
        allowed_updates=("message",),
    ) -> list:
        payload = {"timeout": int(timeout), "allowed_updates": list(allowed_updates)}
        if offset is not None:
            payload["offset"] = int(offset)
        result = await self.call("getUpdates", payload)
        return result if isinstance(result, list) else []

    async def send_message(
        self, chat_id, text: str, *, parse_mode: str = None
    ) -> None:
        """ارسال پیام (پیش‌فرض متن ساده برای پاسخ دستورها)."""
        payload = {"chat_id": chat_id, "text": text}
        if parse_mode is not None:
            payload["parse_mode"] = parse_mode
            payload["disable_web_page_preview"] = True
        await self.call("sendMessage", payload)

"""آداپتور TelegramNotifier — ADR-0002.

- ارسال با Bot API مستقیم: POST api.telegram.org/bot<TOKEN>/sendMessage
  با chat_id، text، parse_mode=HTML و disable_web_page_preview: true
- پروکسی: اگر HTTPS_PROXY در محیط باشد همهٔ فراخوانی‌های بات از آن
  می‌گذرند (ADR-0002 اصلاح ۲۰۲۶-۰۹-۱۸)
- 429: انتظار retry_after (سقف ۶۰ ثانیه) + یک تلاش مجدد همان پیام؛
  تکرار → خطای قابل‌احیا با سرنخ next_attempt (ADR-0010)
- 403/400 ابدی؛ 5xx و خطای شبکه گذرا؛ ناشناخته گذرا (محافظه‌کارانه)

درگاه بات (getUpdates و پاسخ دستورها) مال بستهٔ `top_divar.bot` است و
از همان UrllibTransport این ماژول استفاده می‌کند.
"""

import asyncio
import json

from top_divar.notify.errors import (
    SendError,
    classify_telegram_status,
)
from top_divar.shared.logging import get_logger

_log = get_logger("notify.telegram")

TELEGRAM_API_BASE = "https://api.telegram.org"
DEFAULT_TIMEOUT_SECONDS = 20.0
RETRY_AFTER_CAP_SECONDS = 60.0


class UrllibTransport:
    """حمل HTTP با urllib؛ پروکسی صریح روی همهٔ فراخوانی‌ها (ADR-0002)."""

    def __init__(self, *, proxy=None, timeout: float = DEFAULT_TIMEOUT_SECONDS):
        self._timeout = timeout
        self._proxy = proxy

    async def __call__(self, method: str, url: str, headers: dict, body: bytes = None):
        return await asyncio.to_thread(self._call, method, url, headers, body)

    def _call(self, method: str, url: str, headers: dict, body):
        import urllib.error
        import urllib.request

        handlers = []
        if self._proxy:
            handlers.append(
                urllib.request.ProxyHandler(
                    {"https": self._proxy, "http": self._proxy}
                )
            )
        opener = urllib.request.build_opener(*handlers)
        request = urllib.request.Request(url=url, data=body, method=method)
        for name, value in headers.items():
            request.add_header(name, value)
        try:
            with opener.open(request, timeout=self._timeout) as response:
                return (
                    response.status,
                    {name.lower(): value for name, value in response.headers.items()},
                    response.read(),
                )
        except urllib.error.HTTPError as exc:
            error_body = b""
            try:
                error_body = exc.read()
            except Exception:  # noqa: BLE001 - بدنهٔ خطا اختیاری است
                pass
            return (
                exc.code,
                {name.lower(): value for name, value in (exc.headers or {}).items()},
                error_body,
            )
        except OSError as exc:  # شبکه/DNS/تایم‌اوت/پروکسی → گذرا
            raise SendError(
                category="transient",
                message=f"خطای شبکه در فراخوانی Bot API تلگرام: {exc}",
            ) from exc


def _decode_json(body: bytes):
    try:
        return json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return None


class TelegramNotifier:
    """ارسال پیام HTML به یک chat با Bot API مستقیم (بخش ۳.۲)."""

    def __init__(
        self,
        bot_token: str,
        *,
        proxy: str = None,
        transport=None,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        sleeper=None,
    ):
        if not isinstance(bot_token, str) or not bot_token.strip():
            raise ValueError("توکن ربات تلگرام باید رشتهٔ غیرخالی باشد.")
        self._url = f"{TELEGRAM_API_BASE}/bot{bot_token.strip()}/sendMessage"
        self._transport = transport or UrllibTransport(
            proxy=proxy, timeout=timeout
        )
        self._sleeper = sleeper or asyncio.sleep

    async def send_message(self, chat_id, text: str) -> int:
        """ارسال یک پیام؛ خروجی message_id. شکست → SendError طبقه‌بندی‌شده."""
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        }
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers = {"content-type": "application/json"}
        status, _, response_body = await self._transport(
            "POST", self._url, headers, body
        )
        data = _decode_json(response_body)
        if status == 200 and isinstance(data, dict) and data.get("ok"):
            result = data.get("result")
            return int(result.get("message_id")) if isinstance(result, dict) else None

        error_code, description, retry_after = extract_error_fields(status, data)
        if error_code == 429:
            wait = min(float(retry_after or 0) or RETRY_AFTER_CAP_SECONDS, RETRY_AFTER_CAP_SECONDS)
            _log.warning(
                "تلگرام 429 داد؛ %s ثانیه صبر و یک تلاش مجدد همان پیام.",
                wait,
                extra={
                    "fields": {
                        "event": "telegram_rate_limited",
                        "chat_id": chat_id,
                        "wait_seconds": wait,
                    }
                },
            )
            await self._sleeper(wait)
            status, _, response_body = await self._transport(
                "POST", self._url, headers, body
            )
            data = _decode_json(response_body)
            if status == 200 and isinstance(data, dict) and data.get("ok"):
                result = data.get("result")
                return int(result.get("message_id")) if isinstance(result, dict) else None
            error_code, description, retry_after = extract_error_fields(status, data)

        category = classify_telegram_status(error_code)
        raise SendError(
            category=category,
            message=f"ارسال تلگرام به {chat_id} شکست خورد (وضعیت {error_code}"
            + (f": {description}" if description else "")
            + ").",
            retry_after=retry_after,
        )


def extract_error_fields(status, data):
    """استخراج (error_code, description, retry_after) از پاسخ خطای تلگرام."""
    error_code = status
    description = None
    retry_after = None
    if isinstance(data, dict):
        if isinstance(data.get("error_code"), int):
            error_code = data["error_code"]
        if isinstance(data.get("description"), str):
            description = data["description"]
        parameters = data.get("parameters")
        if isinstance(parameters, dict):
            value = parameters.get("retry_after")
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                retry_after = float(value)
    return error_code, description, retry_after

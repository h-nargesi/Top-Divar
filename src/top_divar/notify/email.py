"""آداپتور EmailNotifier (مرحلهٔ ۶) — configuration.md بخش ۳.۴.

- متن ساده (plain text) + موضوع مصوب؛ معیار تحویل: پذیرش 250 سرور SMTP
- رمزنگاری starttls (پیش‌فرض) / tls (465) / none (آزمایش محلی — هشدار startup)
- اعتبارسنجی گواهی TLS الزامی؛ گواهی نامعتبر → خطای ارسال، بدون downgrade
- طبقه‌بندی خطا: 5yz ابدی، 4yz قابل‌احیا، شبکه/ناشناخته گذرا (ADR-0010)
"""

import asyncio
import email.message
import smtplib
import ssl

from top_divar.notify.errors import SendError, classify_smtp_code
from top_divar.notify.settings import SMTPSettings
from top_divar.shared.logging import get_logger

_log = get_logger("notify.email")

DEFAULT_SMTP_TIMEOUT_SECONDS = 30.0


class EmailNotifier:
    """ارسال ایمیل متن ساده به یک گیرنده با SMTP."""

    def __init__(
        self,
        settings: SMTPSettings,
        password: str,
        *,
        timeout: float = DEFAULT_SMTP_TIMEOUT_SECONDS,
    ):
        if not settings.host:
            raise ValueError("میزبان SMTP در کانفیگ تنظیم نشده است.")
        self._settings = settings
        self._password = password
        self._timeout = timeout

    async def send_message(self, to: str, subject: str, body: str) -> None:
        """ارسال یک ایمیل؛ شکست → SendError طبقه‌بندی‌شده (بخش ۳.۴)."""
        await asyncio.to_thread(self._send_sync, to, subject, body)

    def _send_sync(self, to: str, subject: str, body: str) -> None:
        message = email.message.EmailMessage()
        message["From"] = self._settings.sender or self._settings.username or to
        message["To"] = to
        message["Subject"] = subject
        message.set_content(body)
        context = ssl.create_default_context()
        encryption = self._settings.encryption
        try:
            if encryption == "tls":
                with smtplib.SMTP_SSL(
                    self._settings.host,
                    self._settings.port,
                    timeout=self._timeout,
                    context=context,
                ) as smtp:
                    self._login_and_send(smtp, message, to)
            else:
                with smtplib.SMTP(
                    self._settings.host, self._settings.port, timeout=self._timeout
                ) as smtp:
                    if encryption == "starttls":
                        smtp.starttls(context=context)
                    self._login_and_send(smtp, message, to)
        except SendError:
            raise
        except smtplib.SMTPRecipientsRefused as exc:
            # همهٔ گیرنده‌ها رد شدند — معمولاً نشانی نامعتبر (ADR-0010)
            refused = "; ".join(
                f"{recipient} → {code} {text}"
                for recipient, (code, text) in (exc.recipients or {}).items()
            )
            raise SendError(
                category="eternal",
                message=f"سرور SMTP گیرندهٔ «{to}» را رد کرد: {refused}",
            ) from exc
        except smtplib.SMTPException as exc:
            code = getattr(exc, "smtp_code", None)
            raise SendError(
                category=classify_smtp_code(code),
                message=f"ارسال ایمیل به «{to}» شکست خورد"
                + (f" (کد {code})" if code else "")
                + f": {exc}",
            ) from exc
        except OSError as exc:
            # اتصال/DNS/تایم‌اوت/TLS — قطع موقت فرض می‌شود
            raise SendError(
                category="transient",
                message=f"خطای شبکه/اتصال SMTP به «{to}»: {exc}",
            ) from exc
        except Exception as exc:  # noqa: BLE001 - ناشناخته گذرا (محافظه‌کارانه)
            raise SendError(
                category="transient",
                message=f"خطای ناشناختهٔ SMTP برای «{to}»: {exc}",
            ) from exc

    def _login_and_send(self, smtp: smtplib.SMTP, message, to: str) -> None:
        if self._settings.username is not None and self._password is not None:
            smtp.login(self._settings.username, self._password)
        refused = smtp.send_message(message)
        if refused:
            # send_message فقط گیرنده‌های بدون پاسخ را برمی‌گرداند
            names = ", ".join(refused)
            raise SendError(
                category="eternal",
                message=f"سرور SMTP پیام برای «{names}» را نپذیرفت.",
            )
        _log.info(
            "ایمیل تحویل سرور SMTP شد (250).",
            extra={"fields": {"event": "email_accepted", "recipient": to}},
        )

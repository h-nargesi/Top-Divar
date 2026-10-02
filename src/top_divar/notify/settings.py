"""تنظیمات اطلاع‌رسانی به شکل قابل استفاده در اجرا (مرحلهٔ ۶).

مقادیر از بلوک `notify` کانفیگ خوانده می‌شوند (configuration.md بخش ۳)؛
اعتبارسنجی در startup مال `config.validator` است — اینجا خواندن دفاعی
با پیش‌فرض‌های همان‌جاست: retry_interval = ۳۰m و sweep_max_sends = ۵۰.
"""

from dataclasses import dataclass

from top_divar.config.durations import DurationError, parse_duration
from top_divar.config.validator import (
    DEFAULT_BACKFILL_DAYS,
    DEFAULT_RETRY_INTERVAL,
    DEFAULT_SWEEP_MAX_SENDS,
)


@dataclass(frozen=True)
class TelegramSettings:
    backfill_days: int = DEFAULT_BACKFILL_DAYS


@dataclass(frozen=True)
class SMTPSettings:
    host: str = ""
    port: int = 587
    encryption: str = "starttls"
    username: str = None
    password_env: str = "SMTP_PASSWORD"
    sender: str = None


@dataclass(frozen=True)
class EmailSettings:
    smtp: SMTPSettings = SMTPSettings()
    to: tuple = ()


@dataclass(frozen=True)
class NotifySettings:
    channels: tuple = ()
    retry_interval: float = parse_duration(DEFAULT_RETRY_INTERVAL)
    sweep_max_sends: int = DEFAULT_SWEEP_MAX_SENDS
    telegram: TelegramSettings = TelegramSettings()
    email: EmailSettings = EmailSettings()

    @property
    def telegram_enabled(self) -> bool:
        return "telegram" in self.channels

    @property
    def email_enabled(self) -> bool:
        return "email" in self.channels

    @classmethod
    def from_config(cls, raw: dict) -> "NotifySettings":
        notify = raw.get("notify") if isinstance(raw, dict) else None
        if not isinstance(notify, dict):
            notify = {}
        channels = tuple(
            channel for channel in notify.get("channels") or [] if isinstance(channel, str)
        )
        try:
            retry_interval = parse_duration(
                notify.get("retry_interval", DEFAULT_RETRY_INTERVAL),
                what="notify.retry_interval",
            )
        except DurationError:
            retry_interval = parse_duration(
                DEFAULT_RETRY_INTERVAL, what="notify.retry_interval"
            )
        sweep_max_sends = notify.get("sweep_max_sends")
        if not isinstance(sweep_max_sends, int) or isinstance(sweep_max_sends, bool) or sweep_max_sends < 1:
            sweep_max_sends = DEFAULT_SWEEP_MAX_SENDS

        telegram_raw = notify.get("telegram")
        if not isinstance(telegram_raw, dict):
            telegram_raw = {}
        backfill = telegram_raw.get("backfill_days", DEFAULT_BACKFILL_DAYS)
        if not isinstance(backfill, int) or isinstance(backfill, bool) or backfill < 0:
            backfill = DEFAULT_BACKFILL_DAYS
        telegram = TelegramSettings(backfill_days=backfill)

        email = cls._email_from_config(notify.get("email"))
        return cls(
            channels=channels,
            retry_interval=retry_interval,
            sweep_max_sends=sweep_max_sends,
            telegram=telegram,
            email=email,
        )

    @staticmethod
    def _email_from_config(raw) -> EmailSettings:
        if not isinstance(raw, dict):
            return EmailSettings()
        smtp_raw = raw.get("smtp")
        if not isinstance(smtp_raw, dict):
            smtp_raw = {}
        port = smtp_raw.get("port")
        if not isinstance(port, int) or isinstance(port, bool) or port < 1:
            port = 587
        encryption = smtp_raw.get("encryption", "starttls")
        if encryption not in ("starttls", "tls", "none"):
            encryption = "starttls"
        username = smtp_raw.get("username")
        password_env = smtp_raw.get("password_env")
        if not isinstance(password_env, str) or not password_env:
            password_env = "SMTP_PASSWORD"
        sender = smtp_raw.get("from")
        to = tuple(
            address for address in raw.get("to") or [] if isinstance(address, str)
        )
        smtp = SMTPSettings(
            host=smtp_raw.get("host") if isinstance(smtp_raw.get("host"), str) else "",
            port=port,
            encryption=encryption,
            username=username if isinstance(username, str) else None,
            password_env=password_env,
            sender=sender if isinstance(sender, str) else None,
        )
        return EmailSettings(smtp=smtp, to=to)

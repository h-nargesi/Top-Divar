"""پکیج notify — ارسال اطلاع‌رسانی (مرحلهٔ ۶) — architecture.md بخش ۳.

کانال‌های MVP تلگرام و ایمیل؛ مستقل و بدون زنجیرهٔ fallback (ADR-0002).
ثبت‌نام بات، جبران تعاملی و دستورها مال مرحلهٔ ۷ هستند.
"""

from top_divar.notify.email import EmailNotifier
from top_divar.notify.errors import (
    ETERNAL,
    RESURRECTABLE,
    TRANSIENT,
    SendError,
    classify_smtp_code,
    classify_telegram_status,
)
from top_divar.notify.message import (
    build_email_body,
    build_email_subject,
    build_telegram_message,
)
from top_divar.notify.planner import (
    PlanResult,
    plan_delivery_rows,
    resolve_recipients,
)
from top_divar.notify.settings import (
    EmailSettings,
    NotifySettings,
    SMTPSettings,
    TelegramSettings,
)
from top_divar.notify.sweep import (
    BACKOFF_CAP_SECONDS,
    ChannelSweepResult,
    DeliverySweeper,
    SweepOutcome,
    compute_backoff_seconds,
    email_sender,
    telegram_sender,
)
from top_divar.notify.telegram import TelegramNotifier

__all__ = [
    "BACKOFF_CAP_SECONDS",
    "ETERNAL",
    "RESURRECTABLE",
    "TRANSIENT",
    "ChannelSweepResult",
    "DeliverySweeper",
    "EmailNotifier",
    "EmailSettings",
    "NotifySettings",
    "PlanResult",
    "SMTPSettings",
    "SendError",
    "SweepOutcome",
    "TelegramNotifier",
    "TelegramSettings",
    "build_email_body",
    "build_email_subject",
    "build_telegram_message",
    "classify_smtp_code",
    "classify_telegram_status",
    "compute_backoff_seconds",
    "email_sender",
    "plan_delivery_rows",
    "resolve_recipients",
    "telegram_sender",
]

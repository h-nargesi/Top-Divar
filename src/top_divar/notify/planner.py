"""ساخت ردیف‌های تحویل قبل از ارسال (مرحلهٔ ۶) — ADR-0010.

مدل گیرنده‌ها پخش عمومی است: هر آگهی ممتاز برای همهٔ کاربران تلگرامِ
ثبت‌شده (جدول users) و همهٔ گیرنده‌های ایمیلِ کانفیگ یک ردیف delivery
با وضعیت pending می‌گیرد — قبل از هر ارسالی (تحویل at-least-once).
ساخت ردیف idempotent است؛ (آگهی، کانال، گیرنده) تکراری ساخته نمی‌شود.
"""

from dataclasses import dataclass

from top_divar.notify.settings import NotifySettings
from top_divar.shared.logging import get_logger

_log = get_logger("notify.planner")

CHANNEL_TELEGRAM = "telegram"
CHANNEL_EMAIL = "email"


@dataclass
class PlanResult:
    """نتیجهٔ برنامه‌ریزی تحویل یک آگهی برای لاگ و تست‌ها."""

    ad_id: int
    created: int = 0


async def resolve_recipients(repository, settings: NotifySettings) -> dict:
    """گیرنده‌های فعال به تفکیک کانال — {channel: [recipient, ...]}.

    تلگرام: همهٔ chat_idهای ثبت‌شده (ثبت‌نام بات مال مرحلهٔ ۷ است؛
    جدول از حال خالی شروع می‌شود). ایمیل: فهرست کانفیگ.
    """
    recipients = {}
    if settings.telegram_enabled:
        users = await repository.list_users()
        recipients[CHANNEL_TELEGRAM] = [str(user["chat_id"]) for user in users]
    if settings.email_enabled:
        recipients[CHANNEL_EMAIL] = list(settings.email.to)
    return recipients


async def plan_delivery_rows(
    repository, settings: NotifySettings, ad_id: int
) -> PlanResult:
    """ساخت ردیف‌های delivery ممتاز بودن آگهی — فقط جفت‌های تازه."""
    recipients = await resolve_recipients(repository, settings)
    existing = {
        (row["channel"], row["recipient"])
        for row in await repository.get_deliveries(ad_id)
    }
    pairs = [
        (channel, recipient)
        for channel, channel_recipients in recipients.items()
        for recipient in channel_recipients
        if (channel, recipient) not in existing
    ]
    result = PlanResult(ad_id=ad_id)
    if not pairs:
        return result
    result.created = await repository.create_delivery_rows(ad_id, pairs)
    _log.info(
        "ردیف‌های تحویل قبل از ارسال ساخته شدند.",
        extra={
            "fields": {
                "event": "delivery_planned",
                "ad_id": ad_id,
                "rows": result.created,
            }
        },
    )
    return result

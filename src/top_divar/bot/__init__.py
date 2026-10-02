"""پکیج bot — درگاه بات تلگرام (مرحلهٔ ۷) — architecture.md بخش ۴.

long-polling «getUpdates» با دامنهٔ مینیمال: ثبت‌نام (/start → پسورد →
username یونیک)، جبران تعاملی، ارسال مجدد از تاریخ و /help و /status
(ADR-0010؛ configuration.md بخش ۳.۱). مدیریت جستجو از بات → backlog.
getUpdates یعنی فقط یک نمونهٔ فعال از سرویس (قفل تک‌نمونه در service).
"""

from top_divar.bot.client import TelegramBotClient
from top_divar.bot.gateway import BotGateway
from top_divar.bot.guards import (
    AWAITING_PASSWORD,
    AWAITING_USERNAME,
    GlobalPasswordCounter,
    PasswordThrottle,
    RegistrationSessions,
    ResendCooldowns,
    valid_username,
)

__all__ = [
    "AWAITING_PASSWORD",
    "AWAITING_USERNAME",
    "BotGateway",
    "GlobalPasswordCounter",
    "PasswordThrottle",
    "RegistrationSessions",
    "ResendCooldowns",
    "TelegramBotClient",
    "valid_username",
]

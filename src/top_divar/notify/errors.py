"""طبقه‌بندی خطاهای ارسال (مرحلهٔ ۶) — ADR-0010 اصلاح ۲۰۲۶-۰۹-۱۸.

سه دسته:
- گذرا (transient): ردیف pending می‌ماند؛ تلاش در سویپ بعدی بدون backoff
- قابل‌احیا (resurrectable): pending + next_attempt_at با backoff تا سقف ۲۴ ساعت
- ابدی (eternal): وضعیت dead — دیگر ارسال نمی‌شود

خطای ناشناخته گذرا فرض می‌شود (محافظه‌کارانه).
"""

import dataclasses

TRANSIENT = "transient"
RESURRECTABLE = "resurrectable"
ETERNAL = "eternal"

CATEGORIES = (TRANSIENT, RESURRECTABLE, ETERNAL)


@dataclasses.dataclass(frozen=True)
class SendError(Exception):
    """خطای ارسال یک پیام به یک گیرنده، با دستهٔ رفتاری."""

    category: str
    message: str
    retry_after: float = None  # ثانیه؛ سرنخ سرور برای next_attempt_at (429 تلگرام)

    def __str__(self) -> str:
        return self.message


def classify_telegram_status(status) -> str:
    """دستهٔ خطای Bot API تلگرام بر اساس کد وضعیت (ADR-0002).

    429 بعد از تلاش مجدد داخل notifier می‌رسد و «قابل‌احیا» است؛
    403/400 ابدی‌اند؛ 5xx و ناشناخته‌ها گذرا.
    """
    try:
        code = int(status)
    except (TypeError, ValueError):
        return TRANSIENT
    if code in (400, 403):
        return ETERNAL
    if code == 429:
        return RESURRECTABLE
    return TRANSIENT


def classify_smtp_code(code) -> str:
    """دستهٔ خطای SMTP بر اساس کد پاسخ سرور — 5yz ابدی، 4yz قابل‌احیا."""
    try:
        value = int(code)
    except (TypeError, ValueError):
        return TRANSIENT
    if 500 <= value < 600:
        return ETERNAL
    if 400 <= value < 500:
        return RESURRECTABLE
    return TRANSIENT

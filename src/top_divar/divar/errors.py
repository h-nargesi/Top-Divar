"""خطاهای لایهٔ دیوار (مرحلهٔ ۳)."""


class DivarError(Exception):
    """پایهٔ خطاهای برخورد با دیوار."""


class DivarHTTPError(DivarError):
    """پاسخ HTTP ناموفق؛ وضعیت و هدرهای مرتبط برای لاگ نگه داشته می‌شوند."""

    def __init__(self, message: str, *, status: int = None, url: str = None, retry_after=None):
        super().__init__(message)
        self.status = status
        self.url = url
        self.retry_after = retry_after


class DivarSchemaError(DivarError):
    """ساختار پاسخ آنچه انتظار داشتیم نیست (تغییر اسکیمای API)."""


class DivarUnavailableError(DivarError):
    """نه JSON و نه fallback HTML ویجت نداشتند — فیلدهای جزئیات غایب می‌مانند."""

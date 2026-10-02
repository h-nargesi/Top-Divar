"""صف سریال درخواست‌های دیوار (مرحلهٔ ۳).

concurrency = ۱ (بدون درخواست موازی — AGENTS.md) و حداقل فاصلهٔ
مستقل به تفکیک نوع: search و detail (divar-api.md بخش ۱۰؛
configuration.md بخش ۴). صف جزئیات FIFO است چون همه از یک صف
واحد عبور می‌کنند.
"""

import asyncio
import time

KIND_SEARCH = "search"
KIND_DETAIL = "detail"


class DivarRequestQueue:
    """اجرای سریال کارهای async با فاصلهٔ حداقلی مستقل بین هر نوع درخواست.

    «فاصله» بین شروع دو درخواست هم‌نوع سنجیده می‌شود؛ قفل سراسری
    تضمین می‌کند هیچ درخواستی به دیوار هم‌زمان با دیگری نرود.
    """

    def __init__(self, *, search_min_interval: float, detail_min_interval: float, clock=None, sleeper=None):
        self._intervals = {
            KIND_SEARCH: float(search_min_interval),
            KIND_DETAIL: float(detail_min_interval),
        }
        self._last_started = {KIND_SEARCH: None, KIND_DETAIL: None}
        self._lock = asyncio.Lock()
        self._clock = clock or time.monotonic
        self._sleeper = sleeper or asyncio.sleep

    async def execute(self, kind: str, action):
        if kind not in self._intervals:
            raise ValueError(f"نوع درخواست ناشناخته: «{kind}»")
        async with self._lock:
            remaining = self.wait_seconds(kind)
            if remaining > 0:
                await self._sleeper(remaining)
            self._last_started[kind] = self._clock()
            return await action()

    async def run_search(self, action):
        return await self.execute(KIND_SEARCH, action)

    async def run_detail(self, action):
        return await self.execute(KIND_DETAIL, action)

    def wait_seconds(self, kind: str) -> float:
        """فاصلهٔ باقی‌مانده تا مجاز شدن درخواست بعدیِ همین نوع."""
        last = self._last_started[kind]
        if last is None:
            return 0.0
        return max(0.0, self._intervals[kind] - (self._clock() - last))

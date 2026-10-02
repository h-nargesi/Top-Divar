"""پکیج systemd — پایداری سرویس (مرحلهٔ ۷) — ADR-0003/0012.

sd_notify بدون وابستگی بیرونی (فقط socket کتابخانهٔ استاندارد):
READY=1 در startup، WATCHDOG=1 دوره‌ای برای WatchdogSec و STOPPING=1
در خروج. تسک heartbeat جدا از صف کاری است (ADR-0012) — قفل‌شدن
صف دیوار/ارسال نباید watchdog را بخشکند و برعکس.
"""

from top_divar.systemd.notify import (
    heartbeat_loop,
    sd_notify,
    watchdog_interval_seconds,
)

__all__ = [
    "heartbeat_loop",
    "sd_notify",
    "watchdog_interval_seconds",
]

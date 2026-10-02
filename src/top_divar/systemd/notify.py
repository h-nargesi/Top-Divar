"""sd_notify و ضربان نگهبان (مرحلهٔ ۷) — ADR-0003/0012.

- پیام‌ها روی سوکت NOTIFY_SOCKET (دايتاگرام AF_UNIX)؛ بدون سوکت → False
- فواصل watchdog از WATCHDOG_USEC می‌آید: نصف فاصلهٔ WatchdogSec
  (توصیهٔ systemd برای ضربان)
- heartbeat_loop تسک مستقلی است که فقط sd_notify می‌زند — حتی در حالت
  اشباع صف دیوار تیک می‌زند (وگرنه ری‌استارتهای کاذب)
"""

import asyncio
import os
import socket
import threading

from top_divar.shared.logging import get_logger

_log = get_logger("systemd.notify")

MIN_WATCHDOG_INTERVAL_SECONDS = 1.0
DEFAULT_HEARTBEAT_INTERVAL_SECONDS = 30.0


def sd_notify(message: str, *, env=None) -> bool:
    """فرستادن یک پیام sd_notify؛ خارج از systemd → False."""
    env_map = os.environ if env is None else env
    address = env_map.get("NOTIFY_SOCKET")
    if not address:
        return False
    if address.startswith("@"):
        # سوکت abstract نامک — بایت اول صفر می‌شود
        address = "\0" + address[1:]
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as sock:
            sock.connect(address)
            sock.sendall(message.encode("utf-8"))
        return True
    except OSError as exc:
        _log.warning(
            "ارسال sd_notify شکست خورد: %s",
            exc,
            extra={"fields": {"event": "sd_notify_failed", "error": str(exc)}},
        )
        return False


def watchdog_interval_seconds(env=None) -> float:
    """نصف WatchdogSec برای ضربان؛ بدون WATCHDOG_USEC → None."""
    env_map = os.environ if env is None else env
    raw = env_map.get("WATCHDOG_USEC")
    if not raw:
        return None
    try:
        usec = float(raw)
    except (TypeError, ValueError):
        return None
    if usec <= 0:
        return None
    return max(usec / 1_000_000.0 / 2.0, MIN_WATCHDOG_INTERVAL_SECONDS)


async def heartbeat_loop(
    stop=None,
    *,
    interval: float = None,
    env=None,
    notify=None,
    sleeper=None,
) -> None:
    """ضربان مستقل نگهبان: WATCHDOG=1 هر نصف WatchdogSec تا توقف."""
    sleeper = sleeper or asyncio.sleep
    if notify is None:
        target_env = env
        notify = lambda message: sd_notify(message, env=target_env)  # noqa: E731
    if interval is None:
        interval = watchdog_interval_seconds(env) or DEFAULT_HEARTBEAT_INTERVAL_SECONDS
    while not _is_stopped(stop):
        notify("WATCHDOG=1")
        await sleeper(interval)


def _is_stopped(stop) -> bool:
    if stop is None:
        return False
    if isinstance(stop, (asyncio.Event, threading.Event)):
        return stop.is_set()
    if callable(stop):
        return bool(stop())
    return bool(stop)

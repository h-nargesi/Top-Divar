"""قفل تک‌نمونه بودن سرویس (مرحلهٔ ۷).

getUpdates تلگرام فقط به یک poller فعال تحویل می‌دهد (ADR-0010/0011)؛
دو نمونهٔ هم‌زمان یعنی 409، به‌روزهای گم‌شده و پیام‌های تکراری. قفل
flock روی data/ خودکار با مرگ پروسه آزاد می‌شود — با Restart=always
سازگار است.
"""

import fcntl
import os
from pathlib import Path

from top_divar.shared.logging import get_logger

_log = get_logger("shared.locking")

DEFAULT_LOCK_PATH = Path("data") / "top_divar.lock"


class SingleInstanceLock:
    """قفل انحصاری non-blocking روی یک فایل قفل."""

    def __init__(self, path=DEFAULT_LOCK_PATH):
        self._path = Path(path)
        self._handle = None

    @property
    def path(self) -> Path:
        return self._path

    def acquire(self) -> bool:
        """گرفتن قفل؛ False یعنی نمونهٔ فعال دیگری قفل را دارد."""
        if self._handle is not None:
            return True
        self._path.parent.mkdir(parents=True, exist_ok=True)
        handle = open(self._path, "a+")
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            handle.close()
            return False
        handle.seek(0)
        handle.truncate()
        handle.write(f"{os.getpid()}\n")
        handle.flush()
        self._handle = handle
        return True

    def release(self) -> None:
        handle, self._handle = self._handle, None
        if handle is None:
            return
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        finally:
            handle.close()

    def __enter__(self):
        return self.acquire()

    def __exit__(self, exc_type, exc, tb):
        self.release()
        return False

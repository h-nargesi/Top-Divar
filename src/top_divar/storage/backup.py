"""پشتیبان روزانهٔ پایگاه با تصویر سازگار (مرحلهٔ ۷) — ADR-0001.

`VACUUM INTO` یک اسنپ‌شات کاملاً سازگار می‌سازد — بدون توقف سرویس و
بدون ناسازگاری با WAL (برخلاف کپی مستقیم فایل). نگه‌داشت ~۷ نسخهٔ
روزانهٔ چرخشی در `data/backups/`؛ مازاد قدیمی‌ها حذف می‌شوند.
"""

import re
from pathlib import Path

from top_divar.shared.logging import get_logger
from top_divar.storage.timestamps import utc_now

_log = get_logger("storage.backup")

DEFAULT_BACKUP_KEEP = 7
_BACKUP_PREFIX = "top_divar_"
_BACKUP_SUFFIX = ".sqlite3"
_BACKUP_PATTERN = re.compile(
    rf"^{_BACKUP_PREFIX}\d{{8}}_\d{{6}}(?:_\d+)?{_BACKUP_SUFFIX}$"
)


def backup_filename(moment) -> str:
    """نام فایل پشتیبان از زمان UTC: top_divar_YYYYMMDD_HHMMSS.sqlite3."""
    return f"{_BACKUP_PREFIX}{moment.strftime('%Y%m%d_%H%M%S')}{_BACKUP_SUFFIX}"


def _free_path(target_dir, base_name: str) -> Path:
    """مسیر تازه برای پشتیبان — VACUUM INTO روی فایل موجود خطا می‌دهد."""
    candidate = target_dir / base_name
    counter = 1
    while candidate.exists():
        stem = base_name[: -len(_BACKUP_SUFFIX)]
        candidate = target_dir / f"{stem}_{counter}{_BACKUP_SUFFIX}"
        counter += 1
    return candidate


def rotate_backups(dest_dir, *, keep: int = DEFAULT_BACKUP_KEEP) -> list:
    """حذف قدیمی‌ترین پشتیبانها تا `keep` نسخه بماند؛ خروجی: حذف‌شدهها."""
    if keep < 1:
        keep = 1
    backups = sorted(
        path
        for path in Path(dest_dir).iterdir()
        if path.is_file() and _BACKUP_PATTERN.match(path.name)
    )
    removed = []
    while len(backups) > keep:
        victim = backups.pop(0)
        victim.unlink()
        removed.append(victim)
    return removed


async def backup_database(
    repository,
    dest_dir,
    *,
    keep: int = DEFAULT_BACKUP_KEEP,
    now=None,
) -> Path:
    """ساخت پشتیبان تازه + چرخش؛ خروجی: مسیر فایل ساخته‌شده."""
    moment = utc_now() if now is None else now
    target_dir = Path(dest_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    dest_path = _free_path(target_dir, backup_filename(moment))
    await repository.vacuum_into(dest_path)
    removed = rotate_backups(target_dir, keep=keep)
    _log.info(
        "پشتیبان پایگاه ساخته شد.",
        extra={
            "fields": {
                "event": "backup_created",
                "path": str(dest_path),
                "rotated": len(removed),
                "keep": keep,
            }
        },
    )
    return dest_path

import argparse
import asyncio
import sys

from top_divar import __version__
from top_divar.config import (
    ConfigFileError,
    load_env,
    load_yaml_file,
    validate_config,
)
from top_divar.service import Service
from top_divar.shared.locking import SingleInstanceLock
from top_divar.shared.logging import setup_logging
from top_divar.storage import DEFAULT_DB_PATH, SqliteRepository, StorageError, backup_database


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="top-divar",
        description="پایش آگهی‌های دیوار و اطلاع‌رسانی فوری",
    )
    parser.add_argument(
        "--version", action="version", version=f"top-divar {__version__}"
    )
    subparsers = parser.add_subparsers(dest="command")

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--config", default="config.yaml", help="مسیر فایل کانفیگ")
    common.add_argument("--env", default=".env", help="مسیر فایل .env")

    validate_parser = subparsers.add_parser(
        "validate",
        parents=[common],
        help="خواندن و اعتبارسنجی کانفیگ؛ کد خروج ۰ یعنی سالم",
    )
    validate_parser.add_argument(
        "--log-level", default="INFO", help="سطح لاگ (پیش‌فرض: INFO)"
    )

    run_parser = subparsers.add_parser(
        "run",
        parents=[common],
        help="اجرای سرویس (مرحلهٔ ۷: پایش، ارسال، بات و پایداری)",
    )
    run_parser.add_argument(
        "--log-level", default="INFO", help="سطح لاگ (پیش‌فرض: INFO)"
    )

    user_parser = subparsers.add_parser(
        "user",
        parents=[common],
        help="مدیریت کاربران ثبت‌نام‌شده در بات (ADR-0010/0011)",
    )
    user_subparsers = user_parser.add_subparsers(dest="user_command")
    user_subparsers.add_parser(
        "list",
        parents=[common],
        help="فهرست usernameها + تعداد pending هر کدام",
    )
    user_remove = user_subparsers.add_parser(
        "remove",
        parents=[common],
        help="حذف کاربر + dead کردن pendingهای او (G3)",
    )
    user_remove.add_argument("username", help="نام کاربری")

    reset_watermark_parser = subparsers.add_parser(
        "reset-watermark",
        parents=[common],
        help="حذف خط مرز یک جستجو برای baseline عمدی (اختیاری — ADR-0011)",
    )
    reset_watermark_parser.add_argument("search_id", help="شناسهٔ جستجو")
    reset_watermark_parser.add_argument(
        "--log-level", default="ERROR", help="سطح لاگ (پیش‌فرض: ERROR)"
    )

    backup_parser = subparsers.add_parser(
        "backup",
        parents=[common],
        help="پشتیبان پایگاه با VACUUM INTO + چرخش نسخه‌ها (ADR-0001)",
    )
    backup_parser.add_argument(
        "--output",
        default="data/backups",
        help="پوشهٔ مقصد پشتیبان (پیش‌فرض: data/backups)",
    )
    backup_parser.add_argument(
        "--keep",
        type=int,
        default=7,
        help="تعداد نسخه‌های نگه‌داشتنی (پیش‌فرض: ۷)",
    )
    return parser


def _load_and_validate(config_path, env_path):
    env = load_env(env_path)
    try:
        raw = load_yaml_file(config_path)
    except ConfigFileError as exc:
        return None, None, str(exc)
    report = validate_config(raw, env)
    return raw, report, None


def cmd_validate(args) -> int:
    setup_logging(args.log_level)
    _, report, load_error = _load_and_validate(args.config, args.env)
    if load_error is not None:
        print(f"خطا: {load_error}", file=sys.stderr)
        return 1
    for warning in report.warnings:
        print(f"هشدار: {warning.message}")
    if not report.ok:
        for error in report.errors:
            print(f"خطا: {error.message}", file=sys.stderr)
        print(
            f"کانفیگ نامعتبر است — {len(report.errors)} خطا.",
            file=sys.stderr,
        )
        return 1
    print("کانفیگ معتبر است.")
    return 0


def cmd_run(args) -> int:
    log = setup_logging(args.log_level)
    raw, report, load_error = _load_and_validate(args.config, args.env)
    if load_error is not None:
        log.error("بارگذاری کانفیگ ناموفق بود: %s", load_error)
        return 1
    if raw is None or report is None:
        return 1
    for warning in report.warnings:
        log.warning(warning.message)
    if not report.ok:
        for error in report.errors:
            log.error(error.message)
        log.error("سرویس بهخاطر کانفیگ نامعتبر بالا نمی‌آید.")
        return 1

    # getUpdates فقط یک poller فعال تحمل می‌کند — نمونهٔ دوم همین‌جا می‌ایستد
    lock = SingleInstanceLock()
    if not lock.acquire():
        log.error(
            "نمونهٔ فعال دیگری از سرویس در حال اجراست (قفل %s). "
            "getUpdates تلگرام فقط با یک نمونه کار می‌کند؛ پیش از اجرای دوباره، همان را نگه دارید.",
            lock.path,
            extra={"fields": {"event": "single_instance_refused", "lock": str(lock.path)}},
        )
        return 1

    try:
        try:
            repository = SqliteRepository(DEFAULT_DB_PATH)
        except StorageError as exc:
            log.error(
                "بازکردن پایگاه داده ناموفق بود: %s",
                exc,
                extra={"fields": {"event": "storage_open_failed"}},
            )
            return 1
        exit_code = 0
        try:
            service = Service(
                repository,
                raw,
                load_env(args.env),
                config_path=args.config,
                env_path=args.env,
            )
            asyncio.run(service.run())
        except Exception as exc:  # noqa: BLE001 - خطای غیرمنتظره باید سرویس را بخواباند
            log.error(
                "خطای غیرمنتظره سرویس: %s",
                exc,
                extra={"fields": {"event": "service_crashed", "error": str(exc)}},
            )
            exit_code = 1
        finally:
            repository.close()
    finally:
        lock.release()
    log.info(
        "سیگنال توقف دریافت شد — خروج.",
        extra={"fields": {"event": "service_stopped", "exit_code": exit_code}},
    )
    return exit_code


def _open_repository(log):
    try:
        return SqliteRepository(DEFAULT_DB_PATH)
    except StorageError as exc:
        log.error(
            "بازکردن پایگاه داده ناموفق بود: %s",
            exc,
            extra={"fields": {"event": "storage_open_failed"}},
        )
        return None


def cmd_user(args) -> int:
    log = setup_logging("ERROR")
    repository = _open_repository(log)
    if repository is None:
        return 1
    try:
        if args.user_command == "list":
            users = asyncio.run(repository.list_users_with_pending())
            if not users:
                print("هیچ کاربری ثبت‌نام نکرده است.")
                return 0
            for user in users:
                print(
                    f"{user['username']} (chat {user['chat_id']}) — در انتظار: {user['pending']}"
                )
            return 0
        if args.user_command == "remove":
            removed = asyncio.run(repository.delete_user(args.username))
            if removed is None:
                print(f"کاربری با نام کاربری «{args.username}» پیدا نشد.", file=sys.stderr)
                return 1
            print(
                f"کاربر «{removed['username']}» حذف شد؛ "
                f"{removed['pending_dead']} ردیف pending او dead شد."
            )
            return 0
    finally:
        repository.close()
    return 2


def cmd_reset_watermark(args) -> int:
    log = setup_logging(args.log_level)
    repository = _open_repository(log)
    if repository is None:
        return 1
    try:
        removed = asyncio.run(repository.delete_watermark(args.search_id))
    finally:
        repository.close()
    if removed:
        print(
            f"خط مرز جستجوی «{args.search_id}» پاک شد؛ poll بعدی آن جستجو baseline می‌گیرد."
        )
        return 0
    print(f"خط مرزی برای جستجوی «{args.search_id}» نبود.", file=sys.stderr)
    return 1


def cmd_backup(args) -> int:
    log = setup_logging("ERROR")
    repository = _open_repository(log)
    if repository is None:
        return 1
    try:
        path = asyncio.run(
            backup_database(repository, args.output, keep=args.keep)
        )
    finally:
        repository.close()
    print(f"پشتیبان ساخته شد: {path}")
    return 0


def main(argv=None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    if args.command == "validate":
        return cmd_validate(args)
    if args.command == "run":
        return cmd_run(args)
    if args.command == "user":
        if args.user_command is None:
            parser_print_user_help()
            return 2
        return cmd_user(args)
    if args.command == "reset-watermark":
        return cmd_reset_watermark(args)
    if args.command == "backup":
        return cmd_backup(args)
    parser.print_help()
    return 2


def parser_print_user_help() -> None:
    print("از دستورهای «user list» یا «user remove <username>» استفاده کنید.")




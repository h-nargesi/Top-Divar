import argparse
import signal
import sys
import threading

from top_divar import __version__
from top_divar.config import (
    ConfigFileError,
    load_env,
    load_yaml_file,
    validate_config,
)
from top_divar.shared.logging import get_logger, setup_logging


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
        help="اجرای سرویس (مرحلهٔ ۱: فقط بارگذاری و پایش کانفیگ)",
    )
    run_parser.add_argument(
        "--log-level", default="INFO", help="سطح لاگ (پیش‌فرض: INFO)"
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
    searches = raw.get("searches", [])
    log.info(
        "سرویس راه‌اندازی شد.",
        extra={
            "fields": {
                "event": "service_started",
                "version": __version__,
                "searches": len(searches),
            }
        },
    )
    log.info(
        "پایش دیوار در این مرحله فعال نیست (مرحلهٔ ۱ — تنظیمات و نقطهٔ ورود).",
        extra={"fields": {"event": "phase1_skeleton"}},
    )
    stop = threading.Event()

    def _on_stop(signum, frame):
        stop.set()

    def _on_reload(signum, frame):
        _, new_report, new_load_error = _load_and_validate(args.config, args.env)
        if new_load_error is not None:
            log.error(
                "بارگذاری مجدد ناموفق — کانفیگ قبلی سر جایش می‌ماند: %s",
                new_load_error,
                extra={"fields": {"event": "config_reload_failed"}},
            )
            return
        if new_report.ok:
            log.info(
                "کانفیگ با SIGHUP دوباره خوانده و تأیید شد (اجرای زندهٔ تغییرها مال مرحلهٔ ۷ است).",
                extra={"fields": {"event": "config_reloaded"}},
            )
        else:
            log.error(
                "کانفیگ جدید نامعتبر است — کانفیگ قبلی سر جایش می‌ماند.",
                extra={"fields": {"event": "config_reload_rejected"}},
            )
            for error in new_report.errors:
                log.error(error.message)

    signal.signal(signal.SIGINT, _on_stop)
    signal.signal(signal.SIGTERM, _on_stop)
    if hasattr(signal, "SIGHUP"):
        signal.signal(signal.SIGHUP, _on_reload)
    log.info(
        "در انتظار سیگنال هستیم (SIGHUP = بارگذاری مجدد کانفیگ، SIGINT/SIGTERM = توقف).",
        extra={"fields": {"event": "waiting_for_signals"}},
    )
    while not stop.wait(timeout=3600):
        pass
    log.info("سیگنال توقف دریافت شد — خروج.", extra={"fields": {"event": "service_stopped"}})
    return 0


def main(argv=None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 2
    if args.command == "validate":
        return cmd_validate(args)
    if args.command == "run":
        return cmd_run(args)
    parser.print_help()
    return 2

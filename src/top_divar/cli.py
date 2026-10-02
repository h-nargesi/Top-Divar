import argparse
import asyncio
import signal
import sys

from top_divar import __version__
from top_divar.config import (
    ConfigFileError,
    load_env,
    load_yaml_file,
    validate_config,
)
from top_divar.core import PollScheduler, PollingSettings, poll_search, score_pending_ads
from top_divar.divar.fetcher import DivarFetcher
from top_divar.divar.queue import DivarRequestQueue
from top_divar.notify import (
    DeliverySweeper,
    EmailNotifier,
    NotifySettings,
    TelegramNotifier,
    email_sender,
    plan_delivery_rows,
    telegram_sender,
)
from top_divar.shared.logging import get_logger, setup_logging
from top_divar.storage import DEFAULT_DB_PATH, SqliteRepository, StorageError


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
        help="اجرای سرویس (مرحلهٔ ۶: پایش، امتیاز مطلق و ارسال)",
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
    try:
        repository = SqliteRepository(DEFAULT_DB_PATH)
    except StorageError as exc:
        log.error(
            "بازکردن پایگاه داده ناموفق بود: %s",
            exc,
            extra={"fields": {"event": "storage_open_failed"}},
        )
        return 1
    searches = [
        search
        for search in raw.get("searches", [])
        if isinstance(search, dict) and search.get("enabled", True)
    ]
    searches_by_id = {
        search["id"]: search for search in searches if isinstance(search.get("id"), str)
    }
    settings = PollingSettings.from_config(raw)
    queue = DivarRequestQueue(
        search_min_interval=settings.search_min_interval,
        detail_min_interval=settings.detail_min_interval,
    )
    fetcher = DivarFetcher(queue=queue)

    env = load_env(args.env)
    notify_settings = NotifySettings.from_config(raw)
    sweeper = None
    if notify_settings.channels:
        senders = {}
        if notify_settings.telegram_enabled:
            senders["telegram"] = telegram_sender(
                TelegramNotifier(
                    env.get("TELEGRAM_BOT_TOKEN", ""),
                    proxy=env.get("HTTPS_PROXY") or None,
                )
            )
        if notify_settings.email_enabled:
            smtp = notify_settings.email.smtp
            senders["email"] = email_sender(
                EmailNotifier(smtp, env.get(smtp.password_env))
            )
        sweeper = DeliverySweeper(
            repository,
            senders,
            notify_settings,
            searches_by_id=searches_by_id,
        )
        log.info(
            "ارسال اطلاع‌رسانی فعال است؛ کانال‌ها: %s.",
            "، ".join(senders),
            extra={
                "fields": {
                    "event": "notify_enabled",
                    "channels": sorted(senders),
                    "retry_interval_seconds": notify_settings.retry_interval,
                    "sweep_max_sends": notify_settings.sweep_max_sends,
                }
            },
        )
    else:
        log.info(
            "هیچ کانال اطلاع‌رسانی فعالی نیست — امتیازها فقط ذخیره می‌شوند.",
            extra={"fields": {"event": "notify_disabled"}},
        )

    async def _plan_delivery(row: dict) -> None:
        """ردیف‌های delivery قبل از ارسال (مرحلهٔ ۶ — ADR-0010)."""
        try:
            await plan_delivery_rows(repository, notify_settings, row["id"])
        except Exception as exc:  # noqa: BLE001 - شکست برنامه‌ریزی دور بعد جبران نمی‌شود
            log.error(
                "ساخت ردیف تحویل برای آگهی %s شکست خورد: %s",
                row.get("token"),
                exc,
                extra={
                    "fields": {
                        "event": "delivery_planning_failed",
                        "token": row.get("token"),
                    }
                },
            )

    async def _sweep_quietly() -> None:
        try:
            await sweeper.sweep_once()
        except Exception as exc:  # noqa: BLE001 - جارو نباید سرویس را بخواباند
            log.error(
                "دور جاروی تحویل شکست خورد: %s",
                exc,
                extra={"fields": {"event": "delivery_sweep_failed"}},
            )

    async def _score_pending() -> None:
        """مرحلهٔ دوم خط لوله: امتیازدهی دستهٔ در انتظار (مرحلهٔ ۵).

        شکست این دور کشنده نیست — ردیف‌ها pending می‌مانند و دور بعدی
        (یا آشتی‌سازی startup) دوباره می‌گیردشان. بعد از امتیاز، آگهی‌های
        ممتاز ردیف تحویل می‌گیرند و همان‌جا یک دور ارسال فوری می‌رود.
        """
        try:
            await score_pending_ads(repository, raw, on_notable=_plan_delivery)
        except Exception as exc:  # noqa: BLE001 - حلقهٔ پایش نباید بخوابد
            log.error(
                "امتیازدهی دسته شکست خورد؛ در دور بعد دوباره تلاش می‌شود: %s",
                exc,
                extra={"fields": {"event": "scoring_batch_failed"}},
            )
        if sweeper is not None:
            await _sweep_quietly()

    async def _poll(search: dict) -> None:
        try:
            await poll_search(fetcher, repository, search, settings)
        finally:
            # اول ذخیره با وضعیت در انتظار، بعد امتیاز دسته — حتی اگر poll
            # وسط راه شکست خورد، ذخیره‌شده‌ها امتیاز می‌گیرند
            await _score_pending()

    scheduler = PollScheduler(searches, settings, _poll)

    async def _sweep_loop() -> None:
        """جاروی دوره‌ای ردیف‌های pending (ADR-0010 — هر retry_interval)."""
        while True:
            await asyncio.sleep(notify_settings.retry_interval)
            await _sweep_quietly()

    background = [_sweep_loop()] if sweeper is not None else []

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
        "پایگاه داده آماده است.",
        extra={
            "fields": {
                "event": "storage_ready",
                "path": str(DEFAULT_DB_PATH),
                "schema_version": repository.schema_version,
            }
        },
    )
    log.info(
        "پایش دیوار فعال است (مرحلهٔ ۶ — امتیاز مطلق و ارسال)؛ ثبت‌نام بات و دستورها مال مرحلهٔ ۷ است.",
        extra={
            "fields": {
                "event": "phase6_delivery",
                "default_interval_seconds": settings.default_interval,
                "jitter_seconds": settings.jitter,
                "max_consecutive_errors": settings.max_consecutive_errors,
                "max_pages_per_poll": settings.max_pages_per_poll,
                "notify_on_bump": settings.notify_on_bump,
                "fetch_post_detail": settings.fetch_post_detail,
            }
        },
    )

    def _on_reload() -> None:
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
                "کانفیگ با SIGHUP دوباره خوانده و تأیید شد (اعمال زندهٔ تغییرها مال مرحلهٔ ۷ است).",
                extra={"fields": {"event": "config_reloaded"}},
            )
        else:
            log.error(
                "کانفیگ جدید نامعتبر است — کانفیگ قبلی سر جایش می‌ماند.",
                extra={"fields": {"event": "config_reload_rejected"}},
            )
            for error in new_report.errors:
                log.error(error.message)

    exit_code = 0
    try:
        asyncio.run(
            _run_service(
                scheduler, log, _on_reload, _score_pending, background=background
            )
        )
    except Exception as exc:  # noqa: BLE001 - خطای غیرمنتظره باید سرویس را بخواباند
        log.error(
            "خطای غیرمنتظره سرویس: %s",
            exc,
            extra={"fields": {"event": "service_crashed", "error": str(exc)}},
        )
        exit_code = 1
    finally:
        repository.close()
    log.info(
        "سیگنال توقف دریافت شد — خروج.",
        extra={"fields": {"event": "service_stopped", "exit_code": exit_code}},
    )
    return exit_code


async def _run_service(
    scheduler: PollScheduler, log, on_reload, on_startup=None, background=()
) -> None:
    stop = asyncio.Event()
    loop = asyncio.get_running_loop()

    def _request_stop() -> None:
        stop.set()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, _request_stop)
    if hasattr(signal, "SIGHUP"):
        loop.add_signal_handler(signal.SIGHUP, on_reload)
    tasks = [asyncio.create_task(coro) for coro in background]
    if on_startup is not None:
        # آشتی‌سازی startup: pendingهای باقی‌مانده از اجرای قبل امتیاز می‌گیرند
        # و ردیف‌های تحویل معلق در اولین دور جارو ارسال می‌شوند
        await on_startup()
    log.info(
        "در انتظار سیگنال هستیم (SIGHUP = اعتبارسنجی دوبارهٔ کانفیگ، SIGINT/SIGTERM = توقف).",
        extra={"fields": {"event": "waiting_for_signals"}},
    )
    try:
        await scheduler.run(stop)
    finally:
        for task in tasks:
            task.cancel()
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)


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

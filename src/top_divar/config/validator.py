from dataclasses import dataclass, field

from top_divar.config.durations import DurationError, format_duration, parse_duration

KNOWN_TOP_LEVEL_KEYS = {
    "searches",
    "scoring",
    "notify",
    "polling",
    "history",
}

KNOWN_SEARCH_KEYS = {
    "id",
    "label",
    "enabled",
    "interval",
    "city_ids",
    "place_ids",
    "sort",
    "form_data",
    "scoring_ref",
}

DEPRECATED_SEARCH_KEYS = {
    "districts": "فهرست نام محله در سطح جستجو حذف شده؛ جغرافیا فقط از کلید بومی form_data.districts با شناسهٔ عددی.",
    "allow_unknown_district": "گیت نوتیف جغرافیایی حذف شده و این کلید دیگر معنایی ندارد.",
}

KNOWN_FORM_DATA_KEYS = {
    "category",
    "price",
    "price_per_square",
    "size",
    "rooms",
    "building-age",
    "floor",
    "elevator",
    "parking",
    "warehouse",
    "rebuilt",
    "districts",
    "recent_ads",
    "bbox",
}

WIDGET_TYPES = {
    "str",
    "number_range",
    "boolean",
    "repeated_string",
    "repeated_float",
}

ALLOWED_SCORING_FIELDS = {
    "price",
    "price_per_square",
    "size",
    "rooms",
    "construction_year",
    "building_age",
    "floor",
    "total_floors",
    "has_parking",
    "has_elevator",
    "has_warehouse",
    "district",
    "city",
    "title",
    "is_promoted",
}

ALLOWED_OPS = {
    "==",
    "!=",
    "<",
    "<=",
    ">",
    ">=",
    "in",
    "contains_any",
}

KNOWN_SCORING_BLOCK_KEYS = {"min_score", "on_missing_field", "rules", "relative"}

KNOWN_POLLING_KEYS = {
    "search_min_interval",
    "detail_min_interval",
    "min_interval",
    "default_interval",
    "jitter",
    "backoff",
    "max_consecutive_errors",
    "max_pages_per_poll",
    "notify_on_bump",
    "fetch_post_detail",
}

KNOWN_NOTIFY_KEYS = {"channels", "retry_interval", "telegram", "email"}
KNOWN_TELEGRAM_KEYS = {"backfill_days"}
KNOWN_EMAIL_KEYS = {"smtp", "to"}
KNOWN_SMTP_KEYS = {"host", "port", "encryption", "username", "password_env", "from"}
KNOWN_HISTORY_KEYS = {"purge_margin_days"}

KNOWN_CHANNELS = {"telegram", "email"}
KNOWN_SMTP_ENCRYPTIONS = {"starttls", "tls", "none"}

SYSTEM_WINDOW_DAYS_MAX = 30
DEFAULT_BACKFILL_DAYS = 7
DEFAULT_MIN_INTERVAL = "5m"
DEFAULT_DEFAULT_INTERVAL = "5m"
DEFAULT_SEARCH_MIN_INTERVAL = "30s"
DEFAULT_DETAIL_MIN_INTERVAL = "30s"
POLLING_RATE_LIMIT_WARN_SECONDS = 5.0

SEARCH_ID_ALLOWED_CHARS = set(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"
)


@dataclass(frozen=True)
class Issue:
    level: str
    code: str
    message: str


@dataclass
class ValidationReport:
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


class _Collector:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, code: str, message: str):
        self.errors.append(Issue("error", code, message))

    def warning(self, code: str, message: str):
        self.warnings.append(Issue("warning", code, message))

    def report(self) -> ValidationReport:
        return ValidationReport(errors=self.errors, warnings=self.warnings)


def _is_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _is_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _unknown_keys(c: _Collector, where: str, mapping: dict, known: set, code: str):
    for key in mapping:
        if key not in known:
            c.warning(code, f"کلید ناشناخته در {where}: «{key}»")


def _parse_duration_key(
    c: _Collector, where: str, mapping: dict, key: str, default: str
):
    value = mapping.get(key, default)
    try:
        return parse_duration(value, what=f"{where}.{key}")
    except DurationError as exc:
        c.error("invalid_duration", str(exc))
        return None


def _validate_widget_shape(c: _Collector, search_id: str, key: str, widget):
    if not isinstance(widget, dict) or len(widget) != 1:
        c.error(
            "form_data_bad_value",
            f"form_data جستجوی «{search_id}» کلید «{key}»: ساختار مقدار باید یک ویجت تکی مثل {{number_range: {{...}}}} باشد.",
        )
        return
    widget_type, body = next(iter(widget.items()))
    if widget_type not in WIDGET_TYPES:
        c.error(
            "form_data_bad_value",
            f"form_data جستجوی «{search_id}» کلید «{key}»: نوع ویجت ناشناخته «{widget_type}».",
        )
        return
    if not isinstance(body, dict):
        c.error(
            "form_data_bad_value",
            f"form_data جستجوی «{search_id}» کلید «{key}»: بدنهٔ ویجت «{widget_type}» باید mapping باشد.",
        )
        return
    if widget_type == "str":
        if not isinstance(body.get("value"), str):
            c.error(
                "form_data_bad_value",
                f"form_data جستجوی «{search_id}» کلید «{key}»: ویجت str باید value رشته‌ای داشته باشد.",
            )
    elif widget_type == "boolean":
        if not isinstance(body.get("value"), bool):
            c.error(
                "form_data_bad_value",
                f"form_data جستجوی «{search_id}» کلید «{key}»: ویجت boolean باید value درست/نادرست داشته باشد.",
            )
    elif widget_type == "number_range":
        minimum = body.get("minimum")
        maximum = body.get("maximum")
        if minimum is None and maximum is None:
            c.error(
                "form_data_bad_value",
                f"form_data جستجوی «{search_id}» کلید «{key}»: ویجت number_range بدون minimum/maximum است.",
            )
        for side, value in (("minimum", minimum), ("maximum", maximum)):
            if value is not None and not _is_number(value) and not isinstance(value, str):
                c.error(
                    "form_data_bad_value",
                    f"form_data جستجوی «{search_id}» کلید «{key}»: {side} ویجت number_range باید رشته یا عدد باشد.",
                )
    elif widget_type == "repeated_string":
        value = body.get("value")
        if (
            not isinstance(value, list)
            or not value
            or not all(isinstance(item, str) for item in value)
        ):
            c.error(
                "form_data_bad_value",
                f"form_data جستجوی «{search_id}» کلید «{key}»: ویجت repeated_string باید value به‌صورت لیست غیرخالی از رشته باشد.",
            )
    elif widget_type == "repeated_float":
        value = body.get("value")
        if not isinstance(value, list) or not all(_is_number(item) for item in value):
            c.error(
                "form_data_bad_value",
                f"form_data جستجوی «{search_id}» کلید «{key}»: ویجت repeated_float باید value به‌صورت لیست عدد باشد.",
            )


def _validate_searches(c: _Collector, searches, min_interval_seconds):
    if not isinstance(searches, list) or not searches:
        c.error(
            "schema_error",
            "بخش searches لازم است و باید لیست غیرخالی از جستجوها باشد.",
        )
        return set()
    seen_ids = set()
    for index, search in enumerate(searches, start=1):
        if not isinstance(search, dict):
            c.error(
                "schema_error",
                f"جستجوی شمارهٔ {index} باید mapping باشد.",
            )
            continue
        for key, reason in DEPRECATED_SEARCH_KEYS.items():
            if key in search:
                c.error(
                    "deprecated_search_key",
                    f"کلید منسوخ «{key}» در جستجوی شمارهٔ {index} — {reason}",
                )
        search_id = search.get("id")
        if not isinstance(search_id, str) or not search_id:
            c.error(
                "schema_error",
                f"جستجوی شمارهٔ {index}: کلید id لازم است و باید رشته باشد.",
            )
            search_id = f"#{index}"
        elif not set(search_id) <= SEARCH_ID_ALLOWED_CHARS:
            c.error(
                "schema_error",
                f"شناسهٔ جستجو «{search_id}» فقط می‌تواند حرف انگلیسی، رقم، «.», «_» و «-» داشته باشد.",
            )
        elif search_id in seen_ids:
            c.error("duplicate_search_id", f"شناسهٔ جستجوی تکراری: «{search_id}».")
        else:
            seen_ids.add(search_id)
        _unknown_keys(
            c,
            f"جستجوی «{search_id}»",
            {k: v for k, v in search.items() if k not in DEPRECATED_SEARCH_KEYS},
            KNOWN_SEARCH_KEYS,
            "unknown_search_key",
        )
        label = search.get("label")
        if label is not None and not isinstance(label, str):
            c.error(
                "schema_error",
                f"جستجوی «{search_id}»: label باید رشته باشد.",
            )
        enabled = search.get("enabled")
        if enabled is not None and not isinstance(enabled, bool):
            c.error(
                "schema_error",
                f"جستجوی «{search_id}»: enabled باید درست/نادرست باشد.",
            )
        interval = search.get("interval")
        interval_seconds = None
        if interval is not None:
            try:
                interval_seconds = parse_duration(
                    interval, what=f"interval جستجوی «{search_id}»"
                )
            except DurationError as exc:
                c.error("invalid_duration", str(exc))
            else:
                if (
                    min_interval_seconds is not None
                    and interval_seconds < min_interval_seconds
                ):
                    c.error(
                        "interval_below_min",
                        f"جستجوی «{search_id}»: interval ({format_duration(interval_seconds)}) کمتر از کف polling.min_interval ({format_duration(min_interval_seconds)}) است.",
                    )
        city_ids = search.get("city_ids")
        if not isinstance(city_ids, list) or not city_ids:
            c.error(
                "schema_error",
                f"جستجوی «{search_id}»: city_ids لازم است (مثل [\"1\"] برای تهران).",
            )
        elif not all(isinstance(item, (str, int)) and not isinstance(item, bool) for item in city_ids):
            c.error(
                "schema_error",
                f"جستجوی «{search_id}»: عضوهای city_ids باید رشته یا عدد باشند.",
            )
        place_ids = search.get("place_ids")
        if place_ids is not None:
            if not isinstance(place_ids, list) or not all(
                isinstance(item, (str, int)) and not isinstance(item, bool)
                for item in place_ids
            ):
                c.error(
                    "schema_error",
                    f"جستجوی «{search_id}»: place_ids باید لیستی از رشته/عدد باشد.",
                )
        sort = search.get("sort")
        if sort is not None and sort != "sort_date":
            c.error(
                "schema_error",
                f"جستجوی «{search_id}»: مقدار sort فقط «sort_date» پشتیبانی می‌شود («{sort}»).",
            )
        form_data = search.get("form_data")
        if not isinstance(form_data, dict) or not form_data:
            c.error(
                "schema_error",
                f"جستجوی «{search_id}»: form_data لازم است و باید mapping غیرخالی باشد.",
            )
        else:
            for key, widget in form_data.items():
                if key not in KNOWN_FORM_DATA_KEYS:
                    c.warning(
                        "unknown_form_data_key",
                        f"کلید ناشناخته در form_data جستجوی «{search_id}»: «{key}» (فیلتر جدید دیوار؟ همان‌طور عبور داده می‌شود).",
                    )
                    continue
                _validate_widget_shape(c, search_id, key, widget)
        scoring_ref = search.get("scoring_ref")
        if scoring_ref is not None and not isinstance(scoring_ref, str):
            c.error(
                "schema_error",
                f"جستجوی «{search_id}»: scoring_ref باید رشته باشد.",
            )
    return seen_ids


def _validate_tier(
    c: _Collector, block_name: str, rule_index: int, tier_index: int, tier
):
    where = f"قاعدهٔ {rule_index} پلهٔ {tier_index} بلوک امتیاز «{block_name}»"
    if not isinstance(tier, dict):
        c.error("schema_error", f"{where}: پله باید mapping باشد.")
        return
    op = tier.get("op")
    if op not in ALLOWED_OPS:
        c.error(
            "invalid_operator",
            f"{where}: عملگر نامعتبر «{op!r}»؛ عملگرهای مجاز: ==، !=، <، <=، >، >=، in، contains_any.",
        )
    if "value" not in tier:
        c.error("schema_error", f"{where}: مقدار value لازم است.")
    if not _is_number(tier.get("points")):
        c.error("schema_error", f"{where}: points باید عدد باشد.")


def _validate_scoring(c: _Collector, scoring):
    block_names = set()
    if scoring is None:
        return block_names, None
    if not isinstance(scoring, dict):
        c.error("schema_error", "بخش scoring باید mapping باشد.")
        return block_names, None
    relative_window_days_max = None
    relative_active = False
    for block_name, block in scoring.items():
        if not isinstance(block_name, str) or not block_name:
            c.error("schema_error", "نام بلوک امتیاز باید رشته غیرخالی باشد.")
            continue
        block_names.add(block_name)
        if not isinstance(block, dict):
            c.error(
                "schema_error",
                f"بلوک امتیاز «{block_name}» باید mapping باشد.",
            )
            continue
        _unknown_keys(
            c,
            f"بلوک امتیاز «{block_name}»",
            block,
            KNOWN_SCORING_BLOCK_KEYS,
            "unknown_scoring_key",
        )
        if not _is_number(block.get("min_score")):
            c.error(
                "schema_error",
                f"بلوک امتیاز «{block_name}»: min_score لازم است و باید عدد باشد.",
            )
        on_missing = block.get("on_missing_field")
        if on_missing is not None and on_missing != "skip":
            c.error(
                "on_missing_field_invalid",
                f"بلوک امتیاز «{block_name}»: on_missing_field فقط مقدار «skip» مجاز است (مقدار فعلی: «{on_missing}»).",
            )
        rules = block.get("rules", [])
        if rules is None:
            rules = []
        if not isinstance(rules, list):
            c.error(
                "schema_error",
                f"بلوک امتیاز «{block_name}»: rules باید لیست باشد.",
            )
            rules = []
        for rule_index, rule in enumerate(rules, start=1):
            where = f"قاعدهٔ {rule_index} بلوک امتیاز «{block_name}»"
            if not isinstance(rule, dict):
                c.error("schema_error", f"{where}: قاعده باید mapping باشد.")
                continue
            rule_field = rule.get("field")
            if not isinstance(rule_field, str) or not rule_field:
                c.error(
                    "schema_error",
                    f"{where}: کلید field لازم است و باید رشته باشد.",
                )
            elif rule_field not in ALLOWED_SCORING_FIELDS:
                c.error(
                    "unknown_scoring_field",
                    f"{where}: فیلد ناشناخته «{rule_field}»؛ فیلدهای مجاز: {', '.join(sorted(ALLOWED_SCORING_FIELDS))}.",
                )
            if "tiers" in rule:
                tiers = rule["tiers"]
                if not isinstance(tiers, list) or not tiers:
                    c.error(
                        "schema_error",
                        f"{where}: tiers باید لیست غیرخالی باشد.",
                    )
                else:
                    for tier_index, tier in enumerate(tiers, start=1):
                        _validate_tier(c, block_name, rule_index, tier_index, tier)
            else:
                op = rule.get("op")
                if op not in ALLOWED_OPS:
                    c.error(
                        "invalid_operator",
                        f"{where}: عملگر نامعتبر «{op!r}»؛ عملگرهای مجاز: ==، !=، <، <=، >، >=، in، contains_any.",
                    )
                if "value" not in rule:
                    c.error("schema_error", f"{where}: مقدار value لازم است.")
                if not _is_number(rule.get("points")):
                    c.error("schema_error", f"{where}: points باید عدد باشد.")
        relative = block.get("relative")
        if relative is not None:
            if not isinstance(relative, dict):
                c.error(
                    "schema_error",
                    f"بلوک امتیاز «{block_name}»: relative باید mapping باشد.",
                )
            else:
                enabled = relative.get("enabled")
                if enabled is not None and not isinstance(enabled, bool):
                    c.error(
                        "schema_error",
                        f"بلوک امتیاز «{block_name}»: relative.enabled باید درست/نادرست باشد.",
                    )
                if enabled is True:
                    relative_active = True
                    window_days_max = relative.get("window_days_max")
                    if window_days_max is not None:
                        if not _is_int(window_days_max) or window_days_max < 1:
                            c.error(
                                "schema_error",
                                f"بلوک امتیاز «{block_name}»: relative.window_days_max باید عدد صحیح مثبت باشد.",
                            )
                        else:
                            relative_window_days_max = window_days_max
    window_days_max = (
        relative_window_days_max
        if relative_active and relative_window_days_max is not None
        else SYSTEM_WINDOW_DAYS_MAX
    )
    return block_names, window_days_max


def _validate_scoring_refs(c: _Collector, searches, scoring_block_names):
    if isinstance(searches, list):
        for index, search in enumerate(searches, start=1):
            if not isinstance(search, dict):
                continue
            search_id = search.get("id") if isinstance(search.get("id"), str) else f"#{index}"
            ref = search.get("scoring_ref") or "default"
            if not isinstance(ref, str):
                continue
            if ref not in scoring_block_names:
                c.error(
                    "scoring_ref_not_found",
                    f"جستجوی «{search_id}»: scoring_ref «{ref}» به بلوکی اشاره می‌کند که در scoring وجود ندارد.",
                )


def _validate_polling(c: _Collector, polling):
    if polling is None:
        polling = {}
    if not isinstance(polling, dict):
        c.error("schema_error", "بخش polling باید mapping باشد.")
        return None, None, None, None
    _unknown_keys(c, "polling", polling, KNOWN_POLLING_KEYS, "unknown_polling_key")
    search_min = _parse_duration_key(
        c, "polling", polling, "search_min_interval", DEFAULT_SEARCH_MIN_INTERVAL
    )
    detail_min = _parse_duration_key(
        c, "polling", polling, "detail_min_interval", DEFAULT_DETAIL_MIN_INTERVAL
    )
    min_interval = _parse_duration_key(
        c, "polling", polling, "min_interval", DEFAULT_MIN_INTERVAL
    )
    default_interval = _parse_duration_key(
        c, "polling", polling, "default_interval", DEFAULT_DEFAULT_INTERVAL
    )
    _parse_duration_key(c, "polling", polling, "jitter", "30s")
    if min_interval is not None and default_interval is not None:
        if default_interval < min_interval:
            c.error(
                "default_interval_below_min",
                f"polling.default_interval ({format_duration(default_interval)}) کمتر از کف polling.min_interval ({format_duration(min_interval)}) است.",
            )
    for key, value in (("search_min_interval", search_min), ("detail_min_interval", detail_min)):
        if value is not None and value < POLLING_RATE_LIMIT_WARN_SECONDS:
            c.warning(
                "polling_min_interval_too_small",
                f"polling.{key} ({format_duration(value)}) کمتر از ۵ ثانیه است — ریسک rate limit سمت دیوار.",
            )
    max_consecutive = polling.get("max_consecutive_errors")
    if max_consecutive is not None and (not _is_int(max_consecutive) or max_consecutive < 1):
        c.error(
            "schema_error",
            "polling.max_consecutive_errors باید عدد صحیح مثبت باشد.",
        )
    max_pages = polling.get("max_pages_per_poll")
    if max_pages is not None and (not _is_int(max_pages) or max_pages < 1):
        c.error(
            "schema_error",
            "polling.max_pages_per_poll باید عدد صحیح مثبت باشد.",
        )
    for key in ("notify_on_bump", "fetch_post_detail"):
        value = polling.get(key)
        if value is not None and not isinstance(value, bool):
            c.error(
                "schema_error",
                f"polling.{key} باید درست/نادرست باشد.",
            )
    backoff = polling.get("backoff")
    if backoff is not None and backoff != "exponential":
        c.warning(
            "unknown_backoff",
            f"polling.backoff مقدار «{backoff}» شناخته نشد؛ فقط exponential پیاده‌سازی شده است.",
        )
    return search_min, detail_min, min_interval, default_interval


def _validate_notify(c: _Collector, notify, env, window_days_max):
    if notify is None:
        return
    if not isinstance(notify, dict):
        c.error("schema_error", "بخش notify باید mapping باشد.")
        return
    _unknown_keys(c, "notify", notify, KNOWN_NOTIFY_KEYS, "unknown_notify_key")
    if "retry_interval" in notify:
        try:
            parse_duration(notify["retry_interval"], what="notify.retry_interval")
        except DurationError as exc:
            c.error("invalid_duration", str(exc))
    channels = notify.get("channels", [])
    if channels is None:
        channels = []
    if not isinstance(channels, list) or not all(
        isinstance(item, str) for item in channels
    ):
        c.error("schema_error", "notify.channels باید لیستی از نام کانال‌ها باشد.")
        channels = []
    for channel in channels:
        if channel not in KNOWN_CHANNELS:
            c.error(
                "unknown_channel",
                f"کانال ناشناخته در notify.channels: «{channel}»؛ کانال‌های مجاز: telegram، email.",
            )
    telegram = notify.get("telegram")
    if telegram is not None:
        if not isinstance(telegram, dict):
            c.error("schema_error", "notify.telegram باید mapping باشد.")
        else:
            _unknown_keys(
                c, "notify.telegram", telegram, KNOWN_TELEGRAM_KEYS, "unknown_notify_key"
            )
            backfill = telegram.get("backfill_days", DEFAULT_BACKFILL_DAYS)
            if not _is_int(backfill) or backfill < 0:
                c.error(
                    "schema_error",
                    "notify.telegram.backfill_days باید عدد صحیح غیرمنفی باشد.",
                )
            elif window_days_max is not None and backfill > window_days_max:
                c.error(
                    "backfill_exceeds_window",
                    f"notify.telegram.backfill_days ({backfill}) بزرگ‌تر از window_days_max ({window_days_max}) است.",
                )
    email = notify.get("email")
    if email is not None:
        if not isinstance(email, dict):
            c.error("schema_error", "notify.email باید mapping باشد.")
            email = None
    if email is not None:
        _unknown_keys(c, "notify.email", email, KNOWN_EMAIL_KEYS, "unknown_notify_key")
        to = email.get("to")
        if to is not None:
            if not isinstance(to, list) or not all(isinstance(item, str) for item in to):
                c.error("schema_error", "notify.email.to باید لیستی از نشانی ایمیل باشد.")
            else:
                for address in to:
                    if "@" not in address:
                        c.error(
                            "schema_error",
                            f"notify.email.to: نشانی ایمیل «{address}» معتبر به نظر نمی‌رسد.",
                        )
        smtp = email.get("smtp")
        if smtp is not None:
            if not isinstance(smtp, dict):
                c.error("schema_error", "notify.email.smtp باید mapping باشد.")
            else:
                _unknown_keys(
                    c, "notify.email.smtp", smtp, KNOWN_SMTP_KEYS, "unknown_notify_key"
                )
                if "host" not in smtp or not isinstance(smtp.get("host"), str) or not smtp.get("host"):
                    c.error(
                        "schema_error",
                        "notify.email.smtp.host لازم است و باید رشته باشد.",
                    )
                port = smtp.get("port")
                if port is not None and (not _is_int(port) or port < 1):
                    c.error(
                        "schema_error",
                        "notify.email.smtp.port باید عدد صحیح مثبت باشد.",
                    )
                encryption = smtp.get("encryption", "starttls")
                if encryption not in KNOWN_SMTP_ENCRYPTIONS:
                    c.error(
                        "schema_error",
                        f"notify.email.smtp.encryption مقدار نامعتبر «{encryption}»؛ مقادیر مجاز: starttls، tls، none.",
                    )
                elif encryption == "none":
                    c.warning(
                        "smtp_encryption_none",
                        "notify.email.smtp.encryption=none فقط برای آزمایش محلی است؛ در تولید استفاده نشود.",
                    )
                password_env = smtp.get("password_env")
                if password_env is not None and not isinstance(password_env, str):
                    c.error(
                        "schema_error",
                        "notify.email.smtp.password_env باید رشته (نام متغیر محیطی) باشد.",
                    )
    if "telegram" in channels:
        for var in ("TELEGRAM_BOT_TOKEN", "TELEGRAM_BOT_PASSWORD"):
            if not _env_has(env, var):
                c.error(
                    "missing_env",
                    f"کانال telegram فعال است ولی {var} در محیط/.env تنظیم نشده است.",
                )
    if "email" in channels:
        password_env = "SMTP_PASSWORD"
        if (
            email is not None
            and isinstance(email.get("smtp"), dict)
            and isinstance(email["smtp"].get("password_env"), str)
        ):
            password_env = email["smtp"]["password_env"]
        if not _env_has(env, password_env):
            c.error(
                "missing_env",
                f"کانال email فعال است ولی {password_env} در محیط/.env تنظیم نشده است.",
            )
        if email is None or not isinstance(email.get("to"), list) or not email.get("to"):
            c.error(
                "schema_error",
                "کانال email فعال است ولی notify.email.to خالی/غایب است.",
            )
        elif email.get("smtp") is None:
            c.error(
                "schema_error",
                "کانال email فعال است ولی بلوک notify.email.smtp وجود ندارد.",
            )


def _env_has(env: dict, name: str) -> bool:
    value = env.get(name)
    return value is not None and str(value).strip() != ""


def _validate_history(c: _Collector, history):
    if history is None:
        return
    if not isinstance(history, dict):
        c.error("schema_error", "بخش history باید mapping باشد.")
        return
    _unknown_keys(c, "history", history, KNOWN_HISTORY_KEYS, "unknown_history_key")
    margin = history.get("purge_margin_days")
    if margin is not None:
        if not _is_number(margin):
            c.error(
                "schema_error",
                "history.purge_margin_days باید عدد باشد.",
            )
        elif margin < 0:
            c.error(
                "purge_margin_negative",
                f"history.purge_margin_days نمی‌تواند منفی باشد ({margin}).",
            )


def _validate_env_layer(c: _Collector, env):
    for var in ("TELEGRAM_BOT_TOKEN", "TELEGRAM_OPS_CHAT_ID"):
        if not _env_has(env, var):
            c.warning(
                "ops_env_missing",
                f"{var} تنظیم نشده — پیام‌های هشدار اپراتور (OnFailure/Watchdog/خطای متوالی دیوار) مقصدی ندارند.",
            )


def validate_config(raw: dict, env: dict = None) -> ValidationReport:
    c = _Collector()
    if env is None:
        env = {}
    if not isinstance(raw, dict):
        c.error("schema_error", "کانفیگ باید در سطح بالا یک mapping باشد.")
        return c.report()
    _unknown_keys(c, "سطح بالای کانفیگ", raw, KNOWN_TOP_LEVEL_KEYS, "unknown_top_level_key")
    _, _, min_interval, _ = _validate_polling(c, raw.get("polling"))
    searches = raw.get("searches")
    _validate_searches(c, searches, min_interval)
    scoring_block_names, window_days_max = _validate_scoring(c, raw.get("scoring"))
    _validate_scoring_refs(c, searches, scoring_block_names)
    _validate_notify(c, raw.get("notify"), env, window_days_max)
    _validate_history(c, raw.get("history"))
    _validate_env_layer(c, env)
    return c.report()

"""موتور امتیاز مطلق (مرحلهٔ ۵) — configuration.md بخش ۲ و ADR-0005.

- قواعد کانفیگ `{field, op, value, points}` + پله‌ای (tiers؛ فقط پلهٔ اول
  برقرار امتیاز می‌دهد) + امتیاز منفی (جریمه)
- فیلد **غایب** (منبع ندارد) → کل قاعده skip می‌شود؛ فیلد با **null صریح**
  (مثل قیمت «توافقی») → فقط `== null`/`!= null` ارزیابی می‌شود و بقیه
  عملگرها skip می‌شوند
- عملگرها: ==، !=، <، <=، >، >=، in (عضویت دقیق)، contains_any (تطبیق
  contains نرمال‌شده — برای title/district)
- شرط پیام: فقط `score >= min_score` (notable)؛ شکست امتیاز برای متن
  پیام آماده می‌شود (نام: امتیاز با جداکنندهٔ «·»)
- قواعد نسبی، بازارزیابی و همتا ساخته نمی‌شوند (فاز بعد)

ورودی موتور یک dict «فیلد → مقدار» است: کلیدِ نبودن یعنی غایب، مقدارِ
None یعنی null صریح. تبدیل ردیف پایگاه به این شکل با `fields_from_ad_row`
است (تمایز توافقی از پاکت raw_json).
"""

import json
from dataclasses import dataclass

from top_divar.config.validator import ALLOWED_OPS, ALLOWED_SCORING_FIELDS
from top_divar.divar.normalization import normalize_text, parse_price_text
from top_divar.shared.logging import get_logger

_log = get_logger("core.scoring")

DEFAULT_BLOCK_NAME = "default"

FIELD_LABELS = {
    "price": "قیمت",
    "price_per_square": "قیمت‌متری",
    "size": "متراژ",
    "rooms": "اتاق",
    "construction_year": "ساخت",
    "building_age": "عمر",
    "floor": "طبقه",
    "total_floors": "طبقات",
    "has_parking": "پارکینگ",
    "has_elevator": "آسانسور",
    "has_warehouse": "انباری",
    "district": "محله",
    "city": "شهر",
    "title": "عنوان",
    "is_promoted": "نردبان",
}

_OP_SYMBOLS = {
    "==": "=",
    "!=": "≠",
    "<": "<",
    "<=": "≤",
    ">": ">",
    ">=": "≥",
}

_PERSIAN_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

_BOOL_FIELDS = frozenset(
    {"has_parking", "has_elevator", "has_warehouse", "is_promoted"}
)

_COMPARATORS = {
    "<": lambda a, b: a < b,
    "<=": lambda a, b: a <= b,
    ">": lambda a, b: a > b,
    ">=": lambda a, b: a >= b,
}


@dataclass(frozen=True)
class RuleMatch:
    """یک قاعدهٔ برقرار برای شکست امتیاز (بخش ۳.۳)."""

    field: str
    op: str
    value: object
    points: int
    label: str


@dataclass(frozen=True)
class ScoreResult:
    block: str
    total: int
    min_score: float
    matched: tuple

    @property
    def notable(self) -> bool:
        """شرط پیام: فقط امتیاز بزرگ‌تر یا مساوی حد (فیلتر محله نیست)."""
        return self.total >= self.min_score

    def breakdown_json(self) -> str:
        """شکست امتیاز به JSON برای ذخیره در ردیف آگهی."""
        payload = [
            {"label": match.label, "points": match.points}
            for match in self.matched
        ]
        return json.dumps(payload, ensure_ascii=False)


@dataclass(frozen=True)
class _Condition:
    op: str
    value: object
    points: object


@dataclass(frozen=True)
class ScoringRule:
    field: str
    conditions: tuple  # پله‌ها به‌ترتیب؛ فقط اولین پلهٔ برقرار امتیاز می‌دهد

    def evaluate(self, fields: dict):
        """ارزیابی روی فیلدهای آگهی → (RuleMatch, points) یا None (skip/برقرار نبودن)."""
        if self.field not in fields:
            # فیلد غایب → کل قاعده skip (on_missing_field فقط skip است)
            return None
        actual = fields[self.field]
        for condition in self.conditions:
            outcome = _match(condition.op, condition.value, actual)
            if outcome is None:
                # این پله skip شد (مثل عملگر عددی روی null صریح) → پلهٔ بعد
                continue
            if outcome:
                label = _rule_label(self.field, condition.op, condition.value)
                return RuleMatch(
                    field=self.field,
                    op=condition.op,
                    value=condition.value,
                    points=condition.points,
                    label=label,
                )
            # پله برقرار نبود → پلهٔ بعد (برای tiers آبشاری)
        return None


@dataclass(frozen=True)
class ScoringBlock:
    """یک بلوک scoring کانفیگ (مثل default) بعد از اعتبارسنجی."""

    name: str
    min_score: float
    rules: tuple

    @classmethod
    def from_config(cls, name: str, raw) -> "ScoringBlock":
        if not isinstance(raw, dict):
            raw = {}
        min_score = raw.get("min_score")
        if not _is_number(min_score):
            min_score = 0.0
        rules = []
        for rule in raw.get("rules") or []:
            parsed = _parse_rule(rule)
            if parsed is not None:
                rules.append(parsed)
        return cls(name=name, min_score=min_score, rules=tuple(rules))

    def evaluate(self, fields: dict) -> ScoreResult:
        total = 0
        matched = []
        for rule in self.rules:
            match = rule.evaluate(fields)
            if match is None:
                continue
            matched.append(match)
            total += match.points
        return ScoreResult(
            block=self.name,
            total=total,
            min_score=self.min_score,
            matched=tuple(matched),
        )


def load_scoring_blocks(scoring) -> dict:
    """بلوک‌های scoring کانفیگ → {نام: ScoringBlock}؛ اعتبارسنجی مال validator است."""
    blocks = {}
    if not isinstance(scoring, dict):
        return blocks
    for name, block in scoring.items():
        if isinstance(name, str) and name:
            blocks[name] = ScoringBlock.from_config(name, block)
    return blocks


def _parse_rule(rule):
    if not isinstance(rule, dict):
        return None
    field = rule.get("field")
    if not isinstance(field, str) or not field:
        _log.warning(
            "قاعدهٔ امتیاز بدون field معتبر نادیده گرفته شد: %r",
            rule,
            extra={"fields": {"event": "scoring_rule_dropped"}},
        )
        return None
    conditions = []
    if "tiers" in rule:
        tiers = rule["tiers"]
        if isinstance(tiers, list):
            conditions = [_parse_condition(tier) for tier in tiers]
    else:
        conditions = [_parse_condition(rule)]
    parsed = [condition for condition in conditions if condition is not None]
    if not parsed:
        _log.warning(
            "قاعدهٔ امتیاز فیلد «%s» پله/عملگر معتبر ندارد و نادیده گرفته شد.",
            field,
            extra={"fields": {"event": "scoring_rule_dropped", "field": field}},
        )
        return None
    return ScoringRule(field=field, conditions=tuple(parsed))


def _parse_condition(raw):
    if not isinstance(raw, dict):
        return None
    op = raw.get("op")
    if op not in ALLOWED_OPS:
        return None
    points = raw.get("points")
    if not _is_number(points):
        return None
    return _Condition(op=op, value=raw.get("value"), points=points)


def _is_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _loose_equal(actual, expected) -> bool:
    if isinstance(actual, bool) or isinstance(expected, bool):
        return isinstance(actual, bool) and isinstance(expected, bool) and actual == expected
    if _is_number(actual) and _is_number(expected):
        return actual == expected
    if isinstance(actual, str) and isinstance(expected, str):
        return normalize_text(actual) == normalize_text(expected)
    return actual == expected


def _match(op: str, expected, actual):
    """ارزیابی یک عملگر → True / False / None (skip)."""
    if actual is None:
        # null صریح (توافقی): فقط == null / != null ارزیابی می‌شود
        if op == "==" and expected is None:
            return True
        if op == "!=" and expected is None:
            return False
        return None
    if expected is None:
        if op == "==":
            return False
        if op == "!=":
            return True
        return None
    if op == "==":
        return _loose_equal(actual, expected)
    if op == "!=":
        return not _loose_equal(actual, expected)
    if op in _COMPARATORS:
        if not _is_number(actual) or not _is_number(expected):
            return None
        return _COMPARATORS[op](actual, expected)
    if op == "in":
        if not isinstance(expected, (list, tuple, set)):
            return None
        return any(_loose_equal(actual, item) for item in expected)
    if op == "contains_any":
        if not isinstance(actual, str) or not isinstance(expected, (list, tuple, set)):
            return None
        haystack = normalize_text(actual)
        return any(
            isinstance(item, str) and normalize_text(item) in haystack
            for item in expected
        )
    return None


def _to_persian_digits(text: str) -> str:
    return text.translate(_PERSIAN_DIGITS)


def _format_number(value) -> str:
    """عدد قاعده → نمایش فشردهٔ فارسی برای برچسب (۱۳.۵B، ۲۸۰M، ۵)."""
    if not _is_number(value):
        return _to_persian_digits(str(value))
    magnitude = abs(value)
    if magnitude >= 1_000_000_000:
        scaled, suffix = value / 1_000_000_000, "B"
    elif magnitude >= 1_000_000:
        scaled, suffix = value / 1_000_000, "M"
    else:
        scaled, suffix = value, ""
    if isinstance(scaled, float) and scaled.is_integer():
        scaled = int(scaled)
    elif isinstance(scaled, float):
        scaled = round(scaled, 1)
    return _to_persian_digits(str(scaled)) + suffix


def _rule_label(field: str, op: str, value) -> str:
    """نام فشردهٔ قاعده برای شکست امتیاز (بخش ۳.۳)."""
    name = FIELD_LABELS.get(field, field)
    if value is None:
        if op == "==":
            return f"{name} توافقی"
        return f"{name} غیرتوافقی"
    if isinstance(value, bool):
        if op == "==":
            return name if value else f"بدون {name}"
        return f"بدون {name}" if value else name
    if op in ("in", "contains_any"):
        if isinstance(value, (list, tuple, set)):
            items = "، ".join(
                item if isinstance(item, str) else _format_number(item)
                for item in value
            )
            return f"{name} ∈ {{{items}}}"
        return name
    symbol = _OP_SYMBOLS.get(op, op)
    formatted = _format_number(value) if _is_number(value) else str(value)
    return f"{name}{symbol}{formatted}"


def format_breakdown(result: ScoreResult) -> str:
    """شکست امتیاز فشرده برای پیام: «نام: امتیاز · نام: امتیاز» (بخش ۳.۳)."""
    parts = [
        f"{match.label}: {_to_persian_digits(str(match.points))}"
        for match in result.matched
    ]
    return " · ".join(parts)


def fields_from_ad_row(row: dict) -> dict:
    """ردیف پایگاه → فیلدهای موتور امتیاز.

    کلیدِ غایب = فیلد غایب (قاعده skip)؛ کلید با مقدار None = null صریح
    (فقط قیمت «توافقی» این شکل را می‌گیرد — از پاکت raw_json).
    """
    fields = {}
    for name in ALLOWED_SCORING_FIELDS:
        value = row.get(name)
        if value is None:
            continue
        fields[name] = bool(value) if name in _BOOL_FIELDS else value
    if "price" not in fields and _price_explicitly_null(row):
        fields["price"] = None
    return fields


def _price_explicitly_null(row: dict) -> bool:
    raw = row.get("raw_json")
    if not isinstance(raw, str) or not raw:
        return False
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return False
    if not isinstance(payload, dict):
        return False
    if isinstance(payload.get("price_agreed"), bool):
        return payload["price_agreed"]
    # ردیف‌های قدیمی‌تر (مرحلهٔ ۳/۴): از کارت search درمی‌آوریم
    card = payload.get("search_card")
    data = card.get("data") if isinstance(card, dict) else None
    if not isinstance(data, dict):
        return False
    _, agreed = parse_price_text(data.get("middle_description_text"))
    return bool(agreed)

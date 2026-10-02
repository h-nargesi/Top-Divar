import re

_UNITS = {"s": 1.0, "m": 60.0, "h": 3600.0, "d": 86400.0}
_PATTERN = re.compile(r"^(\d+(?:\.\d+)?)\s*([smhd])?$")


class DurationError(ValueError):
    pass


def parse_duration(value, *, what: str = "مدت‌زمان") -> float:
    if isinstance(value, bool):
        raise DurationError(f"{what} نمی‌تواند بولی باشد.")
    if isinstance(value, (int, float)):
        seconds = float(value)
    elif isinstance(value, str):
        text = value.strip()
        if text.startswith("±") or text.startswith("+"):
            text = text[1:].strip()
        match = _PATTERN.match(text)
        if match is None:
            raise DurationError(
                f"{what} «{value}» قالب درستی ندارد؛ نمونه‌های درست: 30s، 5m، 1h، 7d"
            )
        seconds = float(match.group(1)) * _UNITS[match.group(2) or "s"]
    else:
        raise DurationError(
            f"{what} «{value!r}» قالب درستی ندارد؛ نمونه‌های درست: 30s، 5m، 1h، 7d"
        )
    if seconds < 0:
        raise DurationError(f"{what} نمی‌تواند منفی باشد («{value}»).")
    return seconds


def format_duration(seconds: float) -> str:
    if seconds >= 86400 and seconds % 86400 == 0:
        return f"{int(seconds // 86400)}d"
    if seconds >= 3600 and seconds % 3600 == 0:
        return f"{int(seconds // 3600)}h"
    if seconds >= 60 and seconds % 60 == 0:
        return f"{int(seconds // 60)}m"
    if seconds == int(seconds):
        return f"{int(seconds)}s"
    return f"{seconds}s"

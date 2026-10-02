import pytest

from top_divar.config.durations import DurationError, format_duration, parse_duration


@pytest.mark.parametrize(
    "value,expected",
    [
        ("30s", 30.0),
        ("5m", 300.0),
        ("1h", 3600.0),
        ("7d", 604800.0),
        ("90", 90.0),
        (300, 300.0),
        (1.5, 1.5),
        ("±30s", 30.0),
        (" 5m ", 300.0),
        ("2.5m", 150.0),
    ],
)
def test_parse_duration_accepts_valid_values(value, expected):
    assert parse_duration(value) == expected


@pytest.mark.parametrize(
    "value",
    ["fast", "5x", "m5", "", "5 s 3", None, [300], True, "-5m"],
)
def test_parse_duration_rejects_invalid_values(value):
    with pytest.raises(DurationError):
        parse_duration(value)


@pytest.mark.parametrize(
    "seconds,expected",
    [
        (30.0, "30s"),
        (300.0, "5m"),
        (3600.0, "1h"),
        (86400.0, "1d"),
        (90.0, "90s"),
        (3700.0, "3700s"),
    ],
)
def test_format_duration(seconds, expected):
    assert format_duration(seconds) == expected

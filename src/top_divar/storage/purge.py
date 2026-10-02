from top_divar.config.validator import SYSTEM_WINDOW_DAYS_MAX

DEFAULT_PURGE_MARGIN_DAYS = 7


def resolve_window_days_max(scoring) -> int:
    relative_max = None
    active = False
    if isinstance(scoring, dict):
        for block in scoring.values():
            if not isinstance(block, dict):
                continue
            relative = block.get("relative")
            if not isinstance(relative, dict) or relative.get("enabled") is not True:
                continue
            active = True
            value = relative.get("window_days_max")
            if (
                isinstance(value, int)
                and not isinstance(value, bool)
                and value >= 1
            ):
                relative_max = value
    if active and relative_max is not None:
        return relative_max
    return SYSTEM_WINDOW_DAYS_MAX


def derive_purge_after_days(raw_config) -> int:
    config = raw_config if isinstance(raw_config, dict) else {}
    window_days_max = resolve_window_days_max(config.get("scoring"))
    margin = DEFAULT_PURGE_MARGIN_DAYS
    history = config.get("history")
    if isinstance(history, dict):
        value = history.get("purge_margin_days", DEFAULT_PURGE_MARGIN_DAYS)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            margin = value
    return int(window_days_max + margin)

import datetime

from top_divar.storage.errors import StorageError


def to_utc_datetime(value, *, what: str = "زمان") -> datetime.datetime:
    if isinstance(value, datetime.datetime):
        moment = value
    elif isinstance(value, str):
        text = value.strip()
        if text.endswith(("Z", "z")):
            text = text[:-1] + "+00:00"
        try:
            moment = datetime.datetime.fromisoformat(text)
        except ValueError as exc:
            raise StorageError(
                f"{what} «{value}» قالب ISO درستی ندارد؛ نمونهٔ درست: 2026-09-22T17:19:00+00:00"
            ) from exc
    else:
        raise StorageError(f"{what} باید رشتهٔ ISO یا datetime باشد («{value!r}»).")
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=datetime.timezone.utc)
    return moment.astimezone(datetime.timezone.utc)


def canonical_utc(value, *, what: str = "زمان") -> str:
    return to_utc_datetime(value, what=what).isoformat()


def utc_now() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def utc_now_iso() -> str:
    return utc_now().isoformat()

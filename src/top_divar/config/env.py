import os
from pathlib import Path

from dotenv import dotenv_values


def load_env(env_path=".env") -> dict:
    values = {}
    file_path = Path(env_path)
    if file_path.is_file():
        raw = dotenv_values(file_path)
        values = {key: val for key, val in raw.items() if val is not None}
    effective = dict(values)
    effective.update(dict(os.environ))
    return effective


def env_file_exists(env_path=".env") -> bool:
    return Path(env_path).is_file()


def has_value(env: dict, name: str) -> bool:
    value = env.get(name)
    return value is not None and str(value).strip() != ""

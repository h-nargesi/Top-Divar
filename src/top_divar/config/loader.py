from pathlib import Path

import yaml
from yaml.constructor import ConstructorError
from yaml.resolver import BaseResolver


class ConfigFileError(Exception):
    pass


class StrictLoader(yaml.SafeLoader):
    pass


def _construct_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ConstructorError(
                None,
                None,
                f"کلید تکراری در YAML: «{key}»",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


def _format_mark(error: yaml.YAMLError) -> str:
    mark = getattr(error, "problem_mark", None) or getattr(error, "context_mark", None)
    if mark is None:
        return ""
    return f" (خط {mark.line + 1}، ستون {mark.column + 1})"


def load_yaml_file(path) -> dict:
    file_path = Path(path)
    if not file_path.is_file():
        raise ConfigFileError(f"فایل کانفیگ «{path}» پیدا نشد.")
    try:
        text = file_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ConfigFileError(f"خواندن فایل کانفیگ «{path}» ممکن نشد: {exc}") from exc
    try:
        data = yaml.load(text, Loader=StrictLoader)
    except yaml.YAMLError as exc:
        reason = getattr(exc, "problem", None) or str(exc)
        raise ConfigFileError(
            f"خطای YAML در «{path}»{_format_mark(exc)}: {reason}"
        ) from exc
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ConfigFileError(
            f"کانفیگ «{path}» باید در سطح بالا یک mapping (کلید: مقدار) باشد."
        )
    return data

import json
from typing import Any


def _prettify_json_value(
        value: Any,
        indent: int = 2,
        sort_keys: bool = False,
) -> str:
    """
    Formats a JSON-like value into a clean, vertical layout:
    - with line breaks
    - with indentation
    - without escaping Cyrillic characters

    Supports:
    - str with JSON inside
    - dict
    - list

    Raises:
        ValueError: if JSON is not valid
        TypeError: if not supports at all
    """
    if isinstance(value, str):
        value = value.strip()
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as e:
            raise ValueError(f"Passed string is invalid JSON: {e}") from e
    elif isinstance(value, (dict, list)):
        parsed = value
    else:
        raise TypeError(
            f"Unsupported type for prettify JSON: {type(value).__name__}. "
            f"Expect str, dict or list."
        )

    return json.dumps(
        parsed,
        indent=indent,
        ensure_ascii=False,
        sort_keys=sort_keys,
    )


def prettify_json(
        raw_json: str,
        indent: int = 2,
        sort_keys: bool = False,
) -> dict:
    """
    Formats a JSON string into a well-indented, vertical layout.

    Use this tool when you need to:
    - display raw JSON from the server in a readable format
    - make a nested structure readable
    - display JSON with line breaks and indentation

    Args:
        raw_json: Raw JSON as a string.
        indent: Number of spaces for indentation. Usually 2 or 4.
        sort_keys: Whether to sort keys alphabetically.

    Returns:
        dict:
            {
              "status": "success" | "error",
              "pretty_json": "...",
              "indent": 2,
              "sort_keys": false
            }
    """
    try:
        pretty = _prettify_json_value(
            value=raw_json,
            indent=indent,
            sort_keys=sort_keys,
        )
        return {
            "status": "success",
            "pretty_json": pretty,
            "indent": indent,
            "sort_keys": sort_keys,
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": str(e),
        }

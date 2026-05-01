import json
import logging
import re
from typing import Any

logger = logging.getLogger(__name__)

# ── Compiled fence pattern ────────────────────────────────────────────────────

_FENCE = re.compile(r"```(?:json)?\s*(.*?)\s*```", re.DOTALL)

# ── Schema ────────────────────────────────────────────────────────────────────

# risk_level is intentionally absent — it defaults to "Medium" rather than raising.
_REQUIRED_KEYS: frozenset[str] = frozenset({
    "test_id", "scenario", "preconditions", "steps", "expected_result",
})


# ── Internal helper ───────────────────────────────────────────────────────────

def _strip_fences(text: str) -> str:
    """Return the content inside the first markdown code fence, or *text* stripped."""
    match = _FENCE.search(text)
    return match.group(1).strip() if match else text.strip()


# ── Public API ────────────────────────────────────────────────────────────────

def parse(response_text: str) -> list[dict[str, Any]]:
    """Parse and validate Claude's test-case JSON response.

    Strips markdown fences, decodes JSON, validates structure and required keys,
    and normalises ``risk_level`` to title case. The returned list is ready for
    ``excel_formatter.write()``.

    Args:
        response_text: Raw text returned by the Claude API.

    Returns:
        A list of test-case dicts, each containing exactly:
        ``test_id``, ``scenario``, ``preconditions``, ``steps``,
        ``expected_result``, ``risk_level``.

    Raises:
        ValueError: If the text is not valid JSON after fence-stripping,
                    if the top-level value is not a list, if any list item
                    is not a dict, or if a required key is absent from an item.
    """
    raw = _strip_fences(response_text)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Response is not valid JSON after stripping markdown fences: {exc}"
        ) from exc

    if not isinstance(data, list):
        raise ValueError(
            f"Expected a JSON array from Claude, got {type(data).__name__}"
        )

    result: list[dict[str, Any]] = []
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(
                f"Item at index {i} is not a JSON object (got {type(item).__name__})"
            )

        missing = _REQUIRED_KEYS - item.keys()
        if missing:
            raise ValueError(
                f"Item at index {i} is missing required key(s): {sorted(missing)}"
            )

        result.append({
            "test_id":        item["test_id"],
            "scenario":       item["scenario"],
            "preconditions":  item["preconditions"],
            "steps":          item["steps"],
            "expected_result": item["expected_result"],
            "risk_level":     str(item.get("risk_level", "Medium")).strip().title(),
        })

    logger.info("Parsed %d test case(s) from Claude response", len(result))
    return result

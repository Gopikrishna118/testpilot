import json
import logging
import re
from typing import Any

logger = logging.getLogger(__name__)

# ── Compiled fence pattern ────────────────────────────────────────────────────

_FENCE = re.compile(r"```(?:json)?\s*(.*?)\s*```", re.DOTALL)

# ── Schema ────────────────────────────────────────────────────────────────────

# priority/test_type/traceability/notes/module are optional — Claude may omit them.
_REQUIRED_KEYS: frozenset[str] = frozenset({
    "test_id", "scenario", "preconditions", "test_steps", "expected_result",
})


# ── Internal helper ───────────────────────────────────────────────────────────

_ARRAY = re.compile(r"(\[.*\])", re.DOTALL)

def _strip_fences(text: str) -> str:
    """Extract JSON array from Claude response.

    Priority: 1) inside a code fence, 2) bare text, 3) first [...] found anywhere.
    Strategy 3 catches preamble/postamble text that slips past the prompt constraints.
    """
    # 1. Inside a markdown code fence
    match = _FENCE.search(text)
    if match:
        return match.group(1).strip()
    # 2. Looks like it starts with the array directly
    stripped = text.strip()
    if stripped.startswith("["):
        return stripped
    # 3. Scan for the outermost [...] in case Claude added preamble
    match = _ARRAY.search(text)
    if match:
        logger.warning("Extracted JSON array from mixed response (preamble present)")
        return match.group(1).strip()
    return stripped


# ── Public API ────────────────────────────────────────────────────────────────

def parse(response_text: str) -> list[dict[str, Any]]:
    """Parse and validate Claude's test-case JSON response."""
    logger.info(
        "Claude raw response | len=%d chars | preview=%r",
        len(response_text),
        response_text[:200],
    )

    raw = _strip_fences(response_text)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        logger.error(
            "JSON parse failure | stripped_len=%d | stripped_preview=%r",
            len(raw),
            raw[:500],
        )
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
            "module":         item.get("module", ""),
            "scenario":       item["scenario"],
            "preconditions":  item["preconditions"],
            "test_steps":     item["test_steps"],
            "expected_result": item["expected_result"],
            "priority":       str(item.get("priority", "Medium")).strip().title(),
            "test_type":      item.get("test_type", ""),
            "traceability":   item.get("traceability", ""),
            "notes":          item.get("notes", ""),
        })

    logger.info("Parsed %d test case(s) from Claude response", len(result))
    return result

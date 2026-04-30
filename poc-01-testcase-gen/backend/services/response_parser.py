import json
import logging
import re
from typing import Any

logger = logging.getLogger(__name__)

_JSON_BLOCK = re.compile(r"```(?:json)?\s*(\[.*?\])\s*```", re.DOTALL)


class ResponseParser:
    @staticmethod
    def parse(raw: str) -> list[dict[str, Any]]:
        match = _JSON_BLOCK.search(raw)
        json_str = match.group(1) if match else raw.strip()

        try:
            data = json.loads(json_str)
        except json.JSONDecodeError:
            logger.error("Claude returned non-JSON output (first 200 chars): %s", raw[:200])
            raise ValueError("Claude returned malformed JSON — cannot parse test cases")

        if isinstance(data, dict) and "error" in data:
            raise ValueError(f"Claude signalled error: {data['error']} — {data.get('detail', '')}")

        if not isinstance(data, list):
            raise ValueError(f"Expected JSON array, got {type(data).__name__}")

        return data

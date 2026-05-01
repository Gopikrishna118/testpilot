from pathlib import Path

# ── Master prompt — loaded once at import time ────────────────────────────────

_MASTER_PROMPT_PATH: Path = (
    Path(__file__).resolve().parents[3] / "docs" / "prompts" / "testcase-gen-master.md"
)

try:
    _MASTER_PROMPT: str = _MASTER_PROMPT_PATH.read_text(encoding="utf-8")
except FileNotFoundError as exc:
    raise FileNotFoundError(
        f"Master prompt not found: {_MASTER_PROMPT_PATH}. "
        "Ensure docs/prompts/testcase-gen-master.md exists at the project root."
    ) from exc

# ── Input-type framing instructions ──────────────────────────────────────────

_FRAMING: dict[str, str] = {
    "confluence": (
        "The following is a Confluence page extract containing user stories "
        "and acceptance criteria."
    ),
    "jira": (
        "The following is a JIRA story including title, description, "
        "and acceptance criteria."
    ),
    "brd": (
        "The following is a section from a Business Requirements Document (BRD)."
    ),
    "text": (
        "The following is manually entered requirements text."
    ),
    "file": (
        "The following content was extracted from an uploaded file "
        "(PDF/DOCX/XLSX/TXT/XML)."
    ),
}


# ── Public API ────────────────────────────────────────────────────────────────

def build(input_type: str, content: str) -> str:
    """Assemble the full prompt for the test-case generation API call.

    Combines the master prompt (loaded at import time) with an input-type-specific
    framing sentence and the caller-supplied content block.

    Args:
        input_type: One of ``"confluence"``, ``"jira"``, ``"brd"``, ``"text"``,
                    ``"file"``.
        content:    The sanitised user input to embed. Must not be empty.

    Returns:
        ``master_prompt + "\\n\\n" + framing + "\\n\\n" + content``

    Raises:
        ValueError: If *content* is empty or whitespace-only.
        ValueError: If *input_type* is not one of the five recognised values.
    """
    if not content or not content.strip():
        raise ValueError("content must not be empty")

    if input_type not in _FRAMING:
        raise ValueError(
            f"Unknown input_type: {input_type!r}. "
            f"Valid values: {list(_FRAMING)}"
        )

    return f"{_MASTER_PROMPT}\n\n{_FRAMING[input_type]}\n\n{content}"

from pathlib import Path

from models.request import InputType

_PROMPT_FILE = (
    Path(__file__).resolve().parents[4] / "docs" / "prompts" / "testcase-gen-master.md"
)


class PromptBuilder:
    _template: str | None = None

    @classmethod
    def _load(cls) -> str:
        if cls._template is None:
            cls._template = _PROMPT_FILE.read_text(encoding="utf-8")
        return cls._template

    @classmethod
    def build(cls, input_type: InputType, content: str) -> str:
        template = cls._load()
        user_block = f"INPUT_TYPE: {input_type.value}\nCONTENT:\n{content}"
        return f"{template}\n\n---\n\n{user_block}"

from enum import Enum

from pydantic import BaseModel, field_validator


class InputType(str, Enum):
    confluence = "confluence"
    jira_story = "jira_story"
    brd = "brd"
    freetext = "freetext"


class GenerateRequest(BaseModel):
    input_type: InputType
    content: str

    @field_validator("content")
    @classmethod
    def content_not_empty(cls, v: str) -> str:
        stripped = v.strip()
        if not stripped:
            raise ValueError("content must not be empty")
        if len(stripped) > 10_000:
            raise ValueError("content exceeds 10 000 character limit")
        return stripped

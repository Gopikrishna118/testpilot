from pydantic import BaseModel


class GenerateResponse(BaseModel):
    file_path: str
    count: int
    message: str = "AI-GENERATED — requires human review before use."

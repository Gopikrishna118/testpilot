from functools import lru_cache

from core.config import settings
from services.claude_client import ClaudeClient


@lru_cache(maxsize=1)
def get_claude_client() -> ClaudeClient:
    return ClaudeClient(
        api_key=settings.anthropic_api_key,
        model=settings.claude_model,
        max_retries=settings.max_retries,
    )

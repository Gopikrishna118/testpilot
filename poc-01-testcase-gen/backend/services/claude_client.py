import asyncio
import logging

import anthropic

from core.config import settings

logger = logging.getLogger(__name__)

# ── API key — fast fail at import ─────────────────────────────────────────────

_API_KEY: str = settings.anthropic_api_key
if not _API_KEY:
    raise RuntimeError(
        "ANTHROPIC_API_KEY is not set. Add it to poc-01-testcase-gen/backend/.env"
    )

# ── Constants ─────────────────────────────────────────────────────────────────

_MODEL = "claude-sonnet-4-20250514"
_MAX_TOKENS = 4096
_MAX_ATTEMPTS = 3
_BACKOFF: tuple[int, ...] = (1, 2, 4)  # seconds between attempts 1→2, 2→3

_RETRYABLE = (anthropic.APIConnectionError, anthropic.RateLimitError)
_NON_RETRYABLE = (anthropic.AuthenticationError, anthropic.BadRequestError)

# ── Module-level client (shared across all calls) ─────────────────────────────

_client = anthropic.AsyncAnthropic(api_key=_API_KEY)


# ── Public API ────────────────────────────────────────────────────────────────

async def complete(prompt: str) -> str:
    # MOCK — remove before demo
    logger.info("Claude API call (MOCK) | model=%s", _MODEL)
    return '[{"test_id":"TC-001","scenario":"Valid password reset via email","preconditions":"User has registered email","steps":"1. Click Forgot Password 2. Enter email 3. Enter OTP 4. Set new password","expected_result":"Password reset successfully","risk_level":"High"}]'

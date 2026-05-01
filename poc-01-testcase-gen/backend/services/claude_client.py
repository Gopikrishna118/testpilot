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

_MODEL = settings.claude_model
_MAX_TOKENS = 8192
_MAX_ATTEMPTS = 3
_BACKOFF: tuple[int, ...] = (1, 2, 4)  # seconds between attempts 1→2, 2→3

_RETRYABLE = (anthropic.APIConnectionError, anthropic.RateLimitError)
_NON_RETRYABLE = (anthropic.AuthenticationError, anthropic.BadRequestError)

# ── Module-level client (shared across all calls) ─────────────────────────────

_client = anthropic.AsyncAnthropic(api_key=_API_KEY)


# ── Public API ────────────────────────────────────────────────────────────────

async def complete(prompt: str) -> str:
    last_error: Exception | None = None

    for attempt in range(1, _MAX_ATTEMPTS + 1):
        logger.info("Claude API call | attempt=%d/%d model=%s", attempt, _MAX_ATTEMPTS, _MODEL)
        try:
            message = await _client.messages.create(
                model=_MODEL,
                max_tokens=_MAX_TOKENS,
                messages=[{"role": "user", "content": prompt}],
            )

            if not message.content or not message.content[0].text:
                raise RuntimeError("Empty response from Claude")

            return message.content[0].text

        except _NON_RETRYABLE:
            raise

        except _RETRYABLE as exc:
            last_error = exc
            if attempt < _MAX_ATTEMPTS:
                wait = _BACKOFF[attempt - 1]
                logger.warning(
                    "Claude API retry | attempt=%d/%d error=%s waiting=%ds",
                    attempt, _MAX_ATTEMPTS, type(exc).__name__, wait,
                )
                await asyncio.sleep(wait)

    raise RuntimeError(f"Claude API failed after {_MAX_ATTEMPTS} attempts: {last_error}")

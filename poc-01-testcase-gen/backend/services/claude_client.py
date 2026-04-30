import asyncio
import logging

from anthropic import AsyncAnthropic, APIStatusError, APITimeoutError

logger = logging.getLogger(__name__)


class ClaudeClient:
    def __init__(self, api_key: str, model: str, max_retries: int = 2) -> None:
        self._client = AsyncAnthropic(api_key=api_key)
        self._model = model
        self._max_retries = max_retries

    async def complete(self, prompt: str) -> str:
        for attempt in range(self._max_retries + 1):
            try:
                message = await self._client.messages.create(
                    model=self._model,
                    max_tokens=4096,
                    messages=[{"role": "user", "content": prompt}],
                )
                return message.content[0].text
            except APITimeoutError:
                if attempt == self._max_retries:
                    raise
                wait = 2**attempt
                logger.warning("Anthropic timeout — retry %d/%d in %ds", attempt + 1, self._max_retries, wait)
                await asyncio.sleep(wait)
            except APIStatusError as exc:
                logger.error("Anthropic API error %s: %s", exc.status_code, exc.message)
                raise

import logging

from fastapi import APIRouter, Depends, HTTPException

from core.config import settings
from core.dependencies import get_claude_client
from models.request import GenerateRequest
from models.response import GenerateResponse
from services.claude_client import ClaudeClient
from services.excel_formatter import ExcelFormatter
from services.prompt_builder import PromptBuilder
from services.response_parser import ResponseParser
from services.sanitizer import Sanitizer

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("", response_model=GenerateResponse)
async def generate_test_cases(
    payload: GenerateRequest,
    claude: ClaudeClient = Depends(get_claude_client),
) -> GenerateResponse:
    san = Sanitizer.scrub(payload.content)
    if san.pii_detected:
        logger.warning("PII detected in input | redactions=%d", len(san.redactions))
        raise HTTPException(
            status_code=400,
            detail={
                "error": "PII_DETECTED",
                "message": "Input contains sensitive patterns. Use synthetic data only.",
                "redaction_count": len(san.redactions),
            },
        )

    prompt = PromptBuilder.build(payload.input_type, san.text)
    raw_response = await claude.complete(prompt)
    test_cases = ResponseParser.parse(raw_response)
    output_path = ExcelFormatter.write(test_cases, settings.output_dir)

    logger.info("Generated %d test cases | output=%s", len(test_cases), output_path)
    return GenerateResponse(file_path=output_path, count=len(test_cases))

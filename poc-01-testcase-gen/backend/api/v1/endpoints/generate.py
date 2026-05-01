import logging
import os
from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, HTTPException

from core.config import settings
from models.request import GenerateRequest
from models.response import GenerateResponse
from services.claude_client import complete
from services.excel_formatter import format as write_excel
from services.prompt_builder import build
from services.response_parser import parse
from services.sanitizer import Sanitizer

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("", response_model=GenerateResponse)
async def generate_test_cases(payload: GenerateRequest) -> GenerateResponse:
    # 1. PII gate — reject before anything reaches the Claude API
    san = Sanitizer.scrub(payload.content)
    if san.pii_detected:
        logger.warning("PII detected | redaction_count=%d", len(san.redactions))
        raise HTTPException(
            status_code=400,
            detail={
                "error": "PII_DETECTED",
                "message": "Input contains sensitive patterns. Use synthetic data only.",
                "redaction_count": len(san.redactions),
            },
        )

    # 2. Build prompt — .value unwraps enum to the string framing key
    prompt = build(payload.input_type.value, payload.content)

    # 3. Call Claude
    raw = await complete(prompt)

    # 4. Parse and validate response
    test_cases = parse(raw)

    # 5. Write Excel — ensure output dir exists, then pass full path
    Path(settings.output_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(settings.output_dir, f"testcases_{timestamp}.xlsx")
    write_excel(test_cases, output_path)

    logger.info("Generated %d test case(s) | file=%s", len(test_cases), os.path.basename(output_path))
    return GenerateResponse(file_path=output_path, count=len(test_cases))

import logging
import os
from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse

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


@router.post("/debug", response_class=PlainTextResponse)
async def debug_raw(payload: GenerateRequest) -> str:
    """Return the raw Claude response with no parsing — for pipeline debugging only."""
    san = Sanitizer.scrub(payload.content)
    if san.pii_detected:
        raise HTTPException(status_code=400, detail="PII_DETECTED")
    prompt = build(payload.input_type.value, payload.content)
    raw = await complete(prompt)
    logger.info("DEBUG raw response | len=%d", len(raw))
    return raw


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
    try:
        test_cases = parse(raw)
    except ValueError as exc:
        logger.error("Parse failed | error=%s", exc)
        raise HTTPException(status_code=500, detail={"error": "PARSE_FAILED", "message": str(exc)}) from exc

    # 5. Write Excel — ensure output dir exists, then pass full path
    Path(settings.output_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(settings.output_dir, f"testcases_{timestamp}.xlsx")
    write_excel(test_cases, output_path)

    logger.info("Generated %d test case(s) | file=%s", len(test_cases), os.path.basename(output_path))
    return GenerateResponse(file_path=output_path, count=len(test_cases))

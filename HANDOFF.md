---
file: HANDOFF.md
project: testpilot
session_end: 2026-05-01
sprint_day: D3 of 10
last_commit: 5ef94df
---

# HANDOFF — TestPilot Session Context

> Read this before doing anything. It contains the exact state of the codebase at
> end-of-session and the precise next action to take.

---

## Where We Are

**Sprint:** Day 3 of 10 | 2026-05-01
**Active work:** `poc-01-testcase-gen` backend — service layer
**Git state:** Clean. Last commit `5ef94df` — "Day 3 checkpoint: 5/7 backend files complete"

**5 done, 2 pending:**

| # | File | Status |
|---|------|--------|
| 1 | `shared/utils/sanitizer.py` | ✅ Committed |
| 2 | `poc-01/backend/services/prompt_builder.py` | ✅ Committed |
| 3 | `poc-01/backend/services/claude_client.py` | ✅ Committed |
| 4 | `poc-01/backend/services/response_parser.py` | ✅ Committed |
| 5 | `poc-01/backend/services/excel_formatter.py` | ✅ Committed |
| 6 | `poc-01/backend/api/v1/endpoints/generate.py` | 🔴 **Must rewrite — see §Next Action** |
| 7 | Smoke test + commit | 🔴 Pending |

---

## Next Action — Step 6: Rewrite `generate.py`

**File:** `poc-01-testcase-gen/backend/api/v1/endpoints/generate.py`

The file exists but was written against the old class-based stubs. Every service import
and every call site is now wrong. It must be rewritten against the new module-level APIs.

### The 6 breaking mismatches

**1. Sanitizer — class → module-level functions**

```python
# OLD (still in generate.py)
from services.sanitizer import Sanitizer
san = Sanitizer.scrub(payload.content)
if san.pii_detected: ...

# NEW — import from shared, catch PIIDetectedError
from shared.utils.sanitizer import detect, PIIDetectedError
# OR stay local: from services.sanitizer import detect, PIIDetectedError
# (services/sanitizer.py is still the OLD class version — update it too, or
#  just import from shared/ if PYTHONPATH is configured to include project root)
```

**2. PromptBuilder — classmethod → module-level function, input_type is now a plain str**

```python
# OLD
from services.prompt_builder import PromptBuilder
prompt = PromptBuilder.build(payload.input_type, san.text)

# NEW — module-level build(), pass .value to unwrap the enum
from services.prompt_builder import build as build_prompt
prompt = build_prompt(payload.input_type.value, content)
```

**3. ClaudeClient — class + DI → module-level async function**

```python
# OLD
from services.claude_client import ClaudeClient
from core.dependencies import get_claude_client
async def generate_test_cases(payload, claude: ClaudeClient = Depends(get_claude_client)):
    raw = await claude.complete(prompt)

# NEW — no DI needed, import and call directly
from services.claude_client import complete as claude_complete
raw = await claude_complete(prompt)
```

**4. ResponseParser — classmethod → module-level function**

```python
# OLD
from services.response_parser import ResponseParser
test_cases = ResponseParser.parse(raw_response)

# NEW
from services.response_parser import parse as parse_response
test_cases = parse_response(raw)
```

**5. ExcelFormatter — classmethod + output_dir → module-level function + output_path**

```python
# OLD — auto-generated filename inside write()
from services.excel_formatter import ExcelFormatter
output_path = ExcelFormatter.write(test_cases, settings.output_dir)

# NEW — caller constructs the full path (format() does not timestamp)
from services.excel_formatter import format as format_excel
import os
from datetime import datetime, timezone
timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
output_path = os.path.join(settings.output_dir, f"testcases_{timestamp}.xlsx")
result_path = format_excel(test_cases, output_path)
```

**6. PIIDetectedError — replaces the old pii_detected bool check**

```python
# OLD
san = Sanitizer.scrub(payload.content)
if san.pii_detected:
    raise HTTPException(400, ...)

# NEW — detect() raises directly if PII found
try:
    detect(payload.content)          # returns [] if clean
except PIIDetectedError as exc:
    raise HTTPException(
        status_code=400,
        detail={
            "error": "PII_DETECTED",
            "message": "Input contains sensitive patterns. Use synthetic data only.",
            "redaction_count": len(exc.detections),
        },
    )
```

### Target shape for the rewritten generate.py

```python
import logging
import os
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException

from core.config import settings
from models.request import GenerateRequest
from models.response import GenerateResponse
from services.claude_client import complete as claude_complete
from services.excel_formatter import format as format_excel
from services.prompt_builder import build as build_prompt
from services.response_parser import parse as parse_response
from shared.utils.sanitizer import PIIDetectedError, detect

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("", response_model=GenerateResponse)
async def generate_test_cases(payload: GenerateRequest) -> GenerateResponse:
    # 1. PII gate
    try:
        detect(payload.content)
    except PIIDetectedError as exc:
        logger.warning("PII detected | count=%d", len(exc.detections))
        raise HTTPException(
            status_code=400,
            detail={
                "error": "PII_DETECTED",
                "message": "Input contains sensitive patterns. Use synthetic data only.",
                "redaction_count": len(exc.detections),
            },
        )

    # 2. Build prompt
    prompt = build_prompt(payload.input_type.value, payload.content)

    # 3. Call Claude
    raw = await claude_complete(prompt)

    # 4. Parse response
    test_cases = parse_response(raw)

    # 5. Write Excel
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(settings.output_dir, f"testcases_{timestamp}.xlsx")
    format_excel(test_cases, output_path)

    logger.info("Generated %d test cases | output=%s", len(test_cases), os.path.basename(output_path))
    return GenerateResponse(file_path=output_path, count=len(test_cases))
```

> **Note on `shared/` imports:** `from shared.utils.sanitizer import ...` requires the project
> root on `PYTHONPATH`. When running `uvicorn` from `poc-01/backend/`, add:
> `PYTHONPATH=../../.. uvicorn main:app --reload`
> Or copy-import from `services/sanitizer.py` (the local file needs the same rewrite first).

---

## Service API Surface (reference for generate.py author)

```python
# shared/utils/sanitizer.py
def detect(text: str) -> list[dict]:      # raises PIIDetectedError if PII found
def redact(text: str) -> str              # returns clean text (no raise)
class PIIDetectedError(Exception):
    detections: list[dict]                # [{type, value, start, end}]

# services/prompt_builder.py
def build(input_type: str, content: str) -> str
# input_type: "confluence" | "jira" | "brd" | "text" | "file"
# raises ValueError for unknown type or empty content

# services/claude_client.py
async def complete(prompt: str) -> str
# model: claude-sonnet-4-20250514, max_tokens: 4096
# 3 attempts, backoff 1s/2s/4s on APIConnectionError + RateLimitError
# raises RuntimeError after 3 failed attempts
# raises anthropic.AuthenticationError / BadRequestError immediately (no retry)

# services/response_parser.py
def parse(response_text: str) -> list[dict]
# strips ```json fences, validates keys, normalises risk_level to title case
# required keys per item: test_id, scenario, preconditions, steps, expected_result
# risk_level defaults to "Medium" if absent

# services/excel_formatter.py
def format(test_cases: list[dict], output_path: str) -> str
# caller must ensure output dir exists (raises IOError if not)
# returns output_path unchanged
# raises ValueError if test_cases is empty
```

---

## core/dependencies.py — Now Unused

`get_claude_client()` in `core/dependencies.py` was the DI factory for the old
`ClaudeClient` class. Since `claude_client.py` is now a module-level function,
this factory is dead code. Safe to delete or leave — it does not cause errors.

---

## Smoke Test (run after generate.py is written)

```bash
# From poc-01-testcase-gen/backend/
cp .env.example .env        # fill ANTHROPIC_API_KEY first
PYTHONPATH=../../.. uvicorn main:app --reload

# In a second terminal:
# Health check
curl http://localhost:8000/api/v1/health

# Generate test cases (synthetic input)
curl -X POST http://localhost:8000/api/v1/generate \
  -H "Content-Type: application/json" \
  -d '{
    "input_type": "jira",
    "content": "As a retail banking customer, I want to reset my password so that I can regain account access. AC: given valid email, when reset requested, then OTP sent within 30s."
  }'
```

Expected: `200 {"file_path": "...", "count": 8, "message": "AI-GENERATED..."}`

---

## After Smoke Test — Commit Command

```bash
git add poc-01-testcase-gen/backend/api/v1/endpoints/generate.py
git commit -m "Day 3 complete: poc-01 backend E2E wired and smoke-tested"
```

---

## Key Project Facts (for a fresh session)

| Fact | Value |
|------|-------|
| Repo | `C:\Projects\testpilot` |
| Active PoC backend | `poc-01-testcase-gen/backend/` — run uvicorn from here |
| Model | `claude-sonnet-4-20250514` |
| Pitch target | Rajesh Kumar, QA Manager, 12 engineers, Day 10 (2026-05-08) |
| Security rule | All inputs are synthetic — sanitizer gate before every Claude call |
| `.env` | Must exist in `poc-01-testcase-gen/backend/` — never committed |
| Context files | `CLAUDE.md`, `PROGRESS.md`, `project-knowledge/PROJECT_INSTRUCTIONS.md` |

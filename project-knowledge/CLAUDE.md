# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Summary

TestPilot is a 10-day PoC sprint (2026-04-29 → 2026-05-08) demonstrating Claude Sonnet 4.6 augmenting QA workflows in a banking domain. It consists of 4 independent PoC tools, each with its own FastAPI backend and Next.js 14 frontend, sharing common utilities.

| PoC | What it does |
|-----|-------------|
| `poc-01-testcase-gen` | Confluence/JIRA/BRD text → structured Excel test cases |
| `poc-02-defect-creator` | Freetext defect description → JIRA ticket via REST API |
| `poc-03-selenium-to-playwright` | Legacy Selenium scripts → Playwright TypeScript |
| `poc-04-ui-vision` | Banking UI screenshots → JSON test scenarios (vision API) |

---

## Current Sprint Status

**Sprint:** Day 2 of 10 | 2026-04-30

### Day 1 — Done (2026-04-29)
- 46 files scaffolded across all 4 PoCs + `shared/`
- Repo renamed `qa-forge` → `testpilot` across all docs
- Commits: `d2186ae` (initial scaffold), `086ff9b` (rename)

### Day 2 — In Progress (2026-04-30)

| Work Item | Status |
|-----------|--------|
| Security bundle (`SECURITY.md`, `THREAT_MODEL.md`, `DATA_HANDLING.md`, `.env.example`) | Drafted in chat — **NOT YET committed** |
| ROI Excel (`testpilot_roi.xlsx`) | Built — needs to be saved to `docs/` |
| `poc-01` backend skeleton | Drafted in chat — **NOT YET written to repo** |

### Day 3 — Next (2026-05-01)
- Commit all Day 2 work
- Build Next.js frontend scaffold for `poc-01`
- Build Confluence input adapter for `poc-01`

---

## Development Commands

Each PoC backend follows the same pattern (substitute `poc-01-testcase-gen` as needed):

```bash
# Backend (Python)
cd poc-01-testcase-gen/backend
python -m venv .venv && source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # then fill in ANTHROPIC_API_KEY
uvicorn main:app --reload

# Frontend (Next.js)
cd poc-01-testcase-gen/frontend
npm install
npm run dev

# Lint / type-check
cd poc-01-testcase-gen/frontend
npm run lint
npx tsc --noEmit
```

`.env` variables used by every backend:

```
ANTHROPIC_API_KEY=sk-ant-...
CLAUDE_MODEL=claude-sonnet-4-6
OUTPUT_DIR=./outputs
MAX_RETRIES=2
```

---

## Architecture

### Shared data flow (all PoCs)

```
User input → shared/utils/sanitizer (PII scrub) → Prompt builder
  → Claude Sonnet 4.6 (Anthropic SDK) → Response parser → Output formatter
  → outputs/<name>_<timestamp>.(xlsx|json|ts)
```

**The sanitizer must run before every Anthropic API call.** See `SECURITY.md §5` for the regex rules it enforces (PAN, Aadhaar, Indian account numbers, email, phone, card).

### Planned file layout per PoC backend

```
backend/
  main.py                    # FastAPI app, CORS
  config.py                  # Env vars, model name, output path
  routers/generate.py        # POST /api/generate
  services/
    prompt_builder.py        # Injects input into master prompt template
    claude_client.py         # Anthropic SDK wrapper + retry/backoff
    response_parser.py       # Extracts JSON from Claude response
    excel_formatter.py       # JSON → .xlsx via openpyxl  (PoC-01 only)
```

### Shared utilities (`shared/utils/`)

| Module | Purpose |
|--------|---------|
| `sanitizer.py` | PII regex scrubbing — mandatory gate before any API call |
| `logger.py` | Structured logging (request, response, errors) |
| `error_handler.py` | Anthropic API error codes + exponential backoff retry |
| `config.py` | Central env-var loading |

### Prompts (`docs/prompts/`)

Each PoC has one versioned master prompt file (`testcase-gen-master.md`, `defect-creator-master.md`, `selenium-to-pw-master.md`, `ui-vision-master.md`). The prompt builder reads these at runtime and injects user input. When iterating on prompts, update the file and bump the version in the frontmatter.

---

## Key Constraints

- **Synthetic data only.** Never pass real customer data, PAN, Aadhaar, account numbers, or internal Finastra content to the API. See `SECURITY.md` for the full list.
- **Model:** `claude-sonnet-4-6` is the default (ADR-001). Escalate to `claude-opus-4-7` only for complex multi-file reasoning tasks.
- **No database in PoC** (ADR-002). All outputs are files written to `outputs/`. Production persistence is out of scope for this sprint.
- **No cloud infra.** All PoCs run locally. Production routing through an InfoSec-approved gateway (Bedrock or Anthropic Enterprise) is a post-PoC requirement (see `DECISIONS.md` ADR-004 TODO).
- **`.env` must never be committed.** It is in `.gitignore`. Check before every push.

---

## Tech Stack Versions

| Layer | Version |
|-------|---------|
| Python | 3.11.x |
| FastAPI | 0.111+ |
| `anthropic` SDK | 0.28+ |
| Node.js | 20.x LTS |
| Next.js | 14.x (App Router) |
| TypeScript | 5.x strict mode |
| Tailwind CSS | 3.x |
| `openpyxl` | for Excel output (PoC-01) |

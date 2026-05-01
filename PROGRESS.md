---
file: PROGRESS.md
project: testpilot
updated: 2026-05-01
sprint_day: 3 of 10
---

# PROGRESS — TestPilot Sprint Tracker

> Single source of truth for what's done, what's in flight, and what's next.
> Update at every session checkpoint.

---

## Sprint Snapshot

| Field | Value |
|-------|-------|
| Sprint day | D3 of 10 |
| Active PoC | poc-01-testcase-gen |
| Session status | 🟡 In progress — 5/7 backend files complete |
| Next action | `generate.py` endpoint — wires all services |
| Next milestone | testcase-gen E2E working (target: D3 end or D4) |

---

## PoC-01 Backend — Service Layer (5 / 7)

| # | File | Status | Key behaviours |
|---|------|--------|----------------|
| 1 | `shared/utils/sanitizer.py` | ✅ Done | `detect()` raises `PIIDetectedError`; `redact()` returns clean text; 7 patterns; Luhn check; overlap resolution (longest wins) |
| 2 | `services/prompt_builder.py` | ✅ Done | Master prompt loaded at import; 5 input-type framings (`confluence`, `jira`, `brd`, `text`, `file`); `ValueError` on unknown type |
| 3 | `services/claude_client.py` | ✅ Done | `complete(prompt)` async; model `claude-sonnet-4-20250514`; 3 attempts, 1 s / 2 s / 4 s backoff; retry on `APIConnectionError` + `RateLimitError` only |
| 4 | `services/response_parser.py` | ✅ Done | Strips markdown fences; validates 5 required keys per item; `risk_level` defaults to `"Medium"`, normalised to title case |
| 5 | `services/excel_formatter.py` | ✅ Done | `format(test_cases, output_path)`; 6-col xlsx; header `#1F3864`; alternating fills; risk-level cell colouring; auto-fit widths (max 60) |
| 6 | `api/v1/endpoints/generate.py` | 🔴 Pending | Wire sanitizer → prompt_builder → claude_client → response_parser → excel_formatter |
| 7 | Smoke test + commit | 🔴 Pending | `uvicorn main:app --reload`; `GET /health`; `POST /api/v1/generate` with synthetic input |

### Integration wiring (target shape for generate.py)

```
POST /api/v1/generate
  │  payload: {input_type, content}
  ├─ sanitizer.detect(content)        # raises 400 if PII found
  ├─ prompt_builder.build(input_type, content)
  ├─ claude_client.complete(prompt)   # async, retries
  ├─ response_parser.parse(response)  # validates schema
  └─ excel_formatter.format(cases, output_path)
       └─ returns output_path → 200 {file_path, count}
```

---

## Full Sprint Status

| Day | Date | Focus | Status |
|-----|------|-------|--------|
| D1 | 2026-04-29 | Scaffold + foundation docs | ✅ Done |
| D2 | 2026-04-30 | Security bundle + poc-01 skeleton + project-knowledge | ✅ Done |
| D3 | 2026-05-01 | poc-01 service layer | 🟡 In Progress |
| D4 | 2026-05-02 | poc-01 demo prep + 90-sec video | 🔴 Pending |
| D5 | 2026-05-03 | poc-02 JIRA Defect Creator | 🔴 Pending |
| D6 | 2026-05-04 | poc-02 polish + demo | 🔴 Pending |
| D7 | 2026-05-05 | poc-03 Selenium → Playwright | 🔴 Pending |
| D8 | 2026-05-06 | poc-04 UI Vision | 🔴 Pending |
| D9 | 2026-05-07 | Pitch deck + ROI consolidation | 🔴 Pending |
| D10 | 2026-05-08 | Rehearse + pitch | 🔴 Pending |

---

## Blockers

None current.

---

## Decisions Made This Session

| Decision | Rationale |
|----------|-----------|
| `complete()` is a module-level function, not a class method | Simpler; no DI needed; consistent with prompt_builder and response_parser |
| `detect()` raises, `redact()` cleans | Clear separation: validate vs. sanitise; callers choose the right tool |
| `format()` takes `output_path`, not `output_dir` | Caller controls filename + location; formatter has no timestamp side-effects |
| `risk_level` defaults to `"Medium"` in parser, not formatter | Parser is the schema gate; formatter should receive clean data |

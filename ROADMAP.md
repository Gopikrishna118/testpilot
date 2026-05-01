---
file: ROADMAP.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# ROADMAP — TestPilot 10-Day PoC Sprint

## 10-Day Plan

| Day | Date | Hours | Focus | End-of-Day Output | Status |
|-----|------|-------|-------|-------------------|--------|
| D1 | 2026-04-29 | 3h | Foundation + scaffold + finish testcase-gen baseline | Project structure + initial commit | ✅ Done |
| D2 | 2026-04-30 | 4h | testcase-gen core flow (Confluence → Excel) | Happy path E2E | ✅ Done |
| D3 | 2026-05-01 | 4h | testcase-gen polish + JIRA/BRD inputs + error handling | 3 input types working | 🟡 In Progress |
| D4 | 2026-05-02 | 3h | testcase-gen demo prep | 90-sec video + 1-pager | 🔴 Pending |
| D5 | 2026-05-03 | 4h | JIRA Defect Creator build | Description → JIRA ticket via API | 🔴 Pending |
| D6 | 2026-05-04 | 3h | JIRA Defect Creator polish + demo | Video + slide | 🔴 Pending |
| D7 | 2026-05-05 | 4h | Selenium → Playwright concept PoC | 1 conversion working | 🔴 Pending |
| D8 | 2026-05-06 | 4h | UI Vision concept PoC | Screenshot → test cases | 🔴 Pending |
| D9 | 2026-05-07 | 3h | Pitch deck + ROI consolidation | 8-10 slide deck | 🔴 Pending |
| D10 | 2026-05-08 | 2h | Rehearse + buffer | Pitch-ready | 🔴 Pending |

**Total planned hours:** 34h across 10 days

---

## Today's Progress

> **TODO (Gopi):** Update this section at the end of each working day. Record planned vs. actual, any blockers, and carry-overs.

**Current Day:** D3 — 2026-05-01

**Completed today:**
- [x] `shared/utils/sanitizer.py` — detect + redact, 7 patterns, Luhn, overlap resolution
- [x] `poc-01/backend/services/prompt_builder.py` — module-level load, 5 input-type framings
- [x] `poc-01/backend/services/claude_client.py` — async complete(), 3-attempt backoff, selective retry
- [x] `poc-01/backend/services/response_parser.py` — fence-strip, key validation, risk_level normalisation
- [x] `poc-01/backend/services/excel_formatter.py` — 6-col xlsx, risk colouring, auto-fit widths
- [ ] `poc-01/backend/api/v1/endpoints/generate.py` — pending
- [ ] Smoke test + Day 3 commit — pending

**Blockers:** None

**Carry-over to D4:** generate.py + smoke test if not completed this session

---

## Hours Tracker

| Metric | Value |
|--------|-------|
| Total planned hours | 34h |
| Hours elapsed | ~7h (D1: 3h + D2: 4h) + D3 in progress |
| Hours remaining | ~27h |
| Days elapsed | 2 complete + D3 in progress |
| Days remaining | 7 |

---

## Milestone Summary

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| All 4 PoCs scaffolded | 2026-04-29 | ✅ Done |
| testcase-gen E2E working | 2026-04-30 | 🟡 In Progress — generate.py pending |
| testcase-gen demo video recorded | 2026-05-02 | 🔴 Pending |
| Defect creator demo video recorded | 2026-05-04 | 🔴 Pending |
| Selenium→Playwright conversion working | 2026-05-05 | 🔴 Pending |
| UI Vision working | 2026-05-06 | 🔴 Pending |
| Pitch deck completed | 2026-05-07 | 🔴 Pending |
| Pitch rehearsed + ready | 2026-05-08 | 🔴 Pending |

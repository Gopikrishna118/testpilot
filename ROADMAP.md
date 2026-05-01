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
| D3 | 2026-05-01 | 4h | testcase-gen polish + JIRA/BRD inputs + error handling | 3 input types working | ✅ Done |
| D4 | 2026-05-01 | 5h | testcase-gen: real API, enterprise UI, download endpoint, demo video | E2E live + demo recorded | ✅ Done |
| D5 | 2026-05-02 | 4h | JIRA Defect Creator build | Description → JIRA ticket via API | 🔴 Pending |
| D6 | 2026-05-04 | 3h | JIRA Defect Creator polish + demo | Video + slide | 🔴 Pending |
| D7 | 2026-05-05 | 4h | Selenium → Playwright concept PoC | 1 conversion working | 🔴 Pending |
| D8 | 2026-05-06 | 4h | UI Vision concept PoC | Screenshot → test cases | 🔴 Pending |
| D9 | 2026-05-07 | 3h | Pitch deck + ROI consolidation | 8-10 slide deck | 🔴 Pending |
| D10 | 2026-05-08 | 2h | Rehearse + buffer | Pitch-ready | 🔴 Pending |

**Total planned hours:** 34h across 10 days

---

## Today's Progress

**Current Day:** D4 — 2026-05-01 ✅ Done

**Completed today:**
- [x] Mock removed from `claude_client.py`; real API key wired
- [x] Fixed `CLAUDE_MODEL` env var bug (display string baked into `.env`)
- [x] `_MAX_TOKENS` raised 4096 → 8192 (was truncating large responses)
- [x] Prompt hardened with CRITICAL JSON-only output rules
- [x] `response_parser.py` hardened — 3-strategy extractor, logging, 10-field schema
- [x] `excel_formatter.py` expanded to 10-column output
- [x] `GET /api/v1/download` endpoint with path-traversal security guard
- [x] Enterprise UI (`static/index.html`) — dark navy/gold, stat cards, collapsible cards
- [x] `outputs/` gitignored, removed from history
- [x] Demo video recorded (90-second testcase-gen)

**Blockers:** None

**Carry-over to D5:** None — poc-01 is complete and demo-ready

---

## Hours Tracker

| Metric | Value |
|--------|-------|
| Total planned hours | 34h |
| Hours elapsed | ~16h (D1: 3h, D2: 4h, D3: 4h, D4: 5h) |
| Hours remaining | ~18h |
| Days elapsed | 4 complete |
| Days remaining | 6 |

---

## Milestone Summary

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| All 4 PoCs scaffolded | 2026-04-29 | ✅ Done |
| testcase-gen E2E working | 2026-04-30 | ✅ Done — live with real API key |
| testcase-gen demo video recorded | 2026-05-01 | ✅ Done |
| Defect creator demo video recorded | 2026-05-04 | 🔴 Pending |
| Selenium→Playwright conversion working | 2026-05-05 | 🔴 Pending |
| UI Vision working | 2026-05-06 | 🔴 Pending |
| Pitch deck completed | 2026-05-07 | 🔴 Pending |
| Pitch rehearsed + ready | 2026-05-08 | 🔴 Pending |

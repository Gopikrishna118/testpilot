---
file: METRICS.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# METRICS — TestPilot Success Criteria & ROI

---

## 1. PoC Success Criteria

All items must be met before pitching to manager.

- [ ] **TODO confirm** — All 4 PoCs run on demo input without crashing
- [ ] **TODO confirm** — testcase-gen generates 8+ test cases per input
- [ ] **TODO confirm** — JIRA defect creator successfully creates ticket via API
- [ ] **TODO confirm** — Selenium → Playwright converts 1 valid, executable script
- [ ] **TODO confirm** — UI Vision generates 5+ test scenarios from a screenshot
- [ ] **TODO confirm** — Each PoC has a 90-second demo video recorded
- [ ] **TODO confirm** — Pitch deck completed with 8–10 slides
- [ ] **TODO confirm** — ROI sheet has measured baseline numbers (not estimates)
- [ ] **TODO confirm** — Security document reviewed and signed off by Gopi
- [ ] **TODO confirm** — All commits follow conventional commit format (`type(scope): message`)

---

## 2. Pitch Success Criteria

| Tier | Definition | What it means |
|------|-----------|----------------|
| **Minimum** | Manager says "keep exploring" verbally | PoC phase extended; no budget yet |
| **Target** | Pilot budget approved; 2–4 week pilot with 1–2 QA team members | Small allocation; build production-grade v1 |
| **Stretch** | Formal proposal escalation to QA lead / Director | Cross-team adoption roadmap initiated |

---

## 3. ROI Baseline

> **TODO (Gopi):** Measure these numbers on Day 2 (2026-04-30) using a stopwatch on a real (sanitized) work task. Do NOT estimate — managers will ask "how did you measure this?"

| Activity | Current Manual Time | Notes |
|----------|--------------------|----|
| Write test cases for 1 typical user story | TODO — measure on Day 2 | Include time for format + review |
| Raise 1 JIRA defect ticket (full description) | TODO — measure on Day 2 | |
| Migrate 1 Selenium test to Playwright | TODO — measure on Day 2 | |
| Create test cases from UI screenshot (exploratory) | TODO — measure on Day 2 | |

---

## 4. ROI Math Template

Fill in after Day 2 baseline measurements.

| Variable | Value |
|----------|-------|
| Manual time per test-case task (X hrs) | **TODO** |
| Tool-assisted time per task (Y hrs) | **TODO** (measure after PoC works) |
| Time saved per task (Z = X − Y) | **TODO** |
| Test-case tasks per QA per sprint | **TODO** |
| Number of QAs in team | **TODO** |
| Sprints per year | **TODO** (typically 26 for 2-week sprints) |
| **Annual hours saved per QA** | Z × tasks/sprint × sprints/year |
| **Annual hours saved for team** | Annual per QA × number of QAs |
| Avg QA hourly cost (₹) | **TODO (Gopi)** — use blended rate or skip for internal pitch |
| **Estimated annual value (₹)** | Annual hours saved × hourly cost |

> **Note:** Even without the cost calculation, "X hours saved per sprint per QA" is a powerful number for an internal pitch.

---

## 5. Quality Metrics

> **TODO (Gopi):** Define how you will measure the quality of AI-generated outputs (not just speed).

| Metric | How to Measure | Target |
|--------|---------------|--------|
| Test case accuracy rate | Human review: % of AI cases usable without modification | > 70% for PoC |
| Defect ticket completeness | All mandatory JIRA fields populated | 100% |
| Playwright script executability | Script runs without syntax/runtime errors | 100% for demo case |
| UI Vision relevance rate | % of generated scenarios relevant to the screen shown | > 60% for PoC |

---

## 6. Usage Metrics (PoC Phase)

Track these during the sprint to demonstrate real usage:

| Metric | Target |
|--------|--------|
| Total Claude API calls made | Log all |
| Estimated API cost (USD) | Track in Anthropic dashboard |
| Number of demo runs | ≥ 2 per PoC |
| Prompt iterations per PoC | Log in `docs/prompts/` |

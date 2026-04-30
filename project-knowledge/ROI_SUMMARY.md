---
file: ROI_SUMMARY.md
source: METRICS.md + banking QA benchmarks (actuals pending Day 2 stopwatch measurement)
generated: 2026-04-30
status: TEMPLATE — replace [MEASURE] values before pitch
---

# ROI SUMMARY — TestPilot

> **Action required (Gopi):** Replace every `[MEASURE]` cell with your stopwatch-measured times
> from a real (sanitized) task on Day 2–3. Managers will ask "how did you measure this?"
> Estimates without measurement are not credible in a banking pitch.

---

## 1. Per-PoC Time Savings

| PoC | Manual Baseline | AI-Assisted | Time Saved | Source |
|-----|----------------|-------------|-----------|--------|
| Test Case Generator | [MEASURE] hrs/story | [MEASURE] hrs/story | [MEASURE] hrs | Stopwatch on Day 2–3 |
| JIRA Defect Creator | [MEASURE] min/ticket | [MEASURE] min/ticket | [MEASURE] min | Stopwatch on Day 5–6 |
| Selenium → Playwright | [MEASURE] hrs/script | [MEASURE] hrs/script | [MEASURE] hrs | Stopwatch on Day 7 |
| UI Vision | [MEASURE] hrs/screen | [MEASURE] hrs/screen | [MEASURE] hrs | Stopwatch on Day 8 |

**Reference benchmarks (replace with actuals):**

| PoC | Industry Benchmark (Manual) | Typical AI Reduction |
|-----|-----------------------------|---------------------|
| Test Case Generator | 2–4 hrs per user story | 60–75% reduction |
| JIRA Defect Creator | 30–45 min per ticket | 70–80% reduction |
| Selenium → Playwright | 2–4 hrs per script | 50–70% reduction |
| UI Vision | 1–2 hrs per screen (exploratory) | 60–75% reduction |

---

## 2. Annual Hours Saved — Calculation Template

Fill in after Day 2 baseline measurement and team size confirmed with manager.

| Variable | Formula | Your Value |
|----------|---------|-----------|
| QA team size | — | [MEASURE: ask manager] |
| Test-case stories per sprint | — | [MEASURE: from JIRA sprint board] |
| Sprints per year | — | 26 (2-week sprints) |
| **Hours saved — test cases/year** | (manual − AI) × stories/sprint × 26 | **[CALCULATE]** |
| Defect tickets per QA per sprint | — | [MEASURE] |
| **Hours saved — defects/year** | (manual − AI) × tickets/sprint × 26 | **[CALCULATE]** |
| Selenium scripts migrated/year | — | [MEASURE: backlog size] |
| **Hours saved — migration** | (manual − AI) × scripts | **[CALCULATE]** |
| **Total annual hours saved (team)** | Sum of above × team size | **[CALCULATE]** |

---

## 3. Financial Value

> Skip the ₹ calculation if uncomfortable sharing internal rates. "X hours saved per sprint" is
> sufficient for an internal pitch. Add cost only if manager specifically asks.

| Variable | Value |
|----------|-------|
| Blended QA hourly rate (₹) | [FILL: use cost-to-company ÷ 2080, or skip] |
| Annual hours saved (team total) | [FROM §2] |
| **Estimated annual value (₹)** | hours × rate |
| **Estimated annual value (USD)** | ₹ value ÷ 83 |
| Claude API cost estimate (USD/year) | ~$50–200/year at current usage (verify from Anthropic dashboard) |
| **Net ROI** | Value − API cost |

---

## 4. Quality Metrics (to measure during sprint)

| Metric | Target for PoC | How to Measure |
|--------|---------------|----------------|
| Test case accuracy (usable without edit) | > 70% | Count accepted / total generated in demo run |
| Defect ticket completeness | 100% all JIRA fields | Manual check |
| Playwright script executability | 100% for demo case | Run `npx playwright test` |
| UI Vision relevance rate | > 60% | Review generated scenarios vs screen content |

---

## 5. Pitch-Ready One-Liners

> Use these in the deck. Replace `[X]` with actuals.

- "Test case generation: from [X] hours to [Y] minutes per story — [Z]% faster."
- "Our QA team of [N] engineers could reclaim [X] hours per sprint for higher-value testing."
- "At [X] hours saved per year, TestPilot pays for itself in API costs within the first week."
- "All outputs are draft-only — human review is mandatory. AI augments the engineer, not replaces them."

---

## 6. Assumptions Log

Document assumptions here so the manager can challenge them:

| Assumption | Basis | Risk if Wrong |
|-----------|-------|---------------|
| 2-week sprints (26/year) | Standard Finastra cadence | Adjust if different |
| AI-assisted time = observed PoC demo time | PoC measurement | Production may be slower/faster |
| Team adopts tool at 80% compliance | Estimate | Low adoption = lower savings |
| Anthropic API cost ~$50–200/year | Based on ~5K tokens/request × 500 requests/year | Scale usage changes cost |

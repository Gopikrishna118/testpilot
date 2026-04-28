---
file: ROI-SHEET.md
project: qa-forge
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# ROI-SHEET — QA-Forge Return on Investment

> **Instructions:** Fill in all TODO cells on Day 2 (2026-04-30) by timing yourself on real (sanitized) tasks with a stopwatch. Do not estimate — use measured values. This sheet will be the backbone of Slide 7 in the pitch.

---

## ROI Summary Table

| Activity | Manual Time | Tool-Assisted Time | Time Saved | Per QA / Year | Full Team / Year |
|----------|------------|-------------------|------------|--------------|-----------------|
| Writing test cases (per user story) | TODO hrs | TODO hrs | TODO hrs | TODO hrs | TODO hrs |
| Raising a JIRA defect ticket (per defect) | TODO min | TODO min | TODO min | TODO hrs | TODO hrs |
| Migrating 1 Selenium script to Playwright | TODO hrs | TODO hrs | TODO hrs | TODO hrs | TODO hrs |
| Creating test scenarios from UI screenshot | TODO hrs | TODO hrs | TODO hrs | TODO hrs | TODO hrs |
| **TOTAL** | — | — | — | **TODO hrs** | **TODO hrs** |

---

## Measurement Methodology

> **TODO (Gopi):** Describe how you measured the "Manual Time" column. Example:
> - Timed yourself writing test cases for Story #[TODO] on 2026-04-30
> - Used stopwatch from "start reading story" to "Excel saved and ready for review"
> - Did NOT include review time (measuring creation only)

---

## Key Assumptions

| Assumption | Value | Source |
|------------|-------|--------|
| User stories per QA per sprint | TODO | TODO (Gopi): count from last 2 sprints in JIRA) |
| Defects raised per QA per sprint | TODO | TODO (Gopi): count from JIRA) |
| Selenium scripts to migrate (backlog) | TODO | TODO (Gopi): count from test repo) |
| Number of QA engineers in team | TODO | TODO (Gopi) |
| Working sprints per year | TODO | Typically 26 for 2-week sprints |
| Average QA hourly cost (₹) | TODO | TODO (Gopi): use blended rate or omit for internal pitch) |

---

## Annual Hours Saved Calculation

```
Hours saved per test-case task     = Manual − Tool-assisted
Tasks per QA per sprint            = TODO
Sprints per year                   = TODO
Annual hours saved per QA          = Saved × Tasks/sprint × Sprints/year
Annual hours saved (whole team)    = Per QA × Team size
```

**Calculated annual hours saved (team):** TODO hrs

---

## Investment Required

| Item | Estimated Cost | Notes |
|------|---------------|-------|
| Claude API credits / month | TODO USD | Estimate from Anthropic pricing after PoC usage data |
| Internal dev time (build production v1) | TODO weeks | TODO (Gopi): estimate once PoC complete) |
| InfoSec / legal review | TODO days | Depends on Finastra process |
| Ongoing maintenance | TODO hrs/month | Prompt updates, API version upgrades |

---

## Payback Period

> **TODO (Gopi):** Calculate after filling in savings and investment.

```
Investment (dev time)  = TODO hrs
Monthly team savings   = TODO hrs
Payback period         = Investment / Monthly savings = TODO months
```

---

## Comparable Tool Costs (Context)

> **TODO (Gopi):** Research 1–2 commercial alternatives to give context (e.g., Testim, Mabl, Tricentis pricing). Shows the build-vs-buy framing. Keep this factual and current.

| Tool | Pricing Model | Estimated Annual Cost | Notes |
|------|-------------|----------------------|-------|
| TODO | TODO | TODO USD | |
| TODO | TODO | TODO USD | |
| QA-Forge (this PoC) | Claude API + internal dev | TODO USD | Built for Finastra-specific workflows |

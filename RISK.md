---
file: RISK.md
project: qa-forge
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# RISK — QA-Forge Risk Register

> Update this register whenever a new risk is identified or a risk status changes. Review at the start of each sprint day.

---

## Risk Register

| ID | Risk | Likelihood | Impact | Mitigation | Owner | Status |
|----|------|-----------|--------|------------|-------|--------|
| R-01 | Claude hallucinates incorrect test step content | H | M | Mandatory human review step; all Excel outputs labeled "AI-GENERATED — REQUIRES REVIEW"; add anti-hallucination guards to prompts | Gopi | Open |
| R-02 | PII leak via prompt to external API | L | Critical | Synthetic data only policy enforced; sanitization layer mandatory before every API call; developer checklist in SECURITY.md | Gopi | Open |
| R-03 | Anthropic API downtime breaks live demo | M | H | Pre-record demo videos as fallback; always show recording if live API fails; test API connectivity 30 min before any demo | Gopi | Open |
| R-04 | InfoSec rejects external API usage post-demo | M | Critical | Architect production version for Bedrock-compatible deployment from Day 1; document migration path; frame PoC as "personal account experiment" | Gopi | Open |
| R-05 | JIRA REST API auth fails during defect creator demo | M | H | Use sandbox JIRA instance; test auth on Day 5 morning; have pre-populated ticket screenshot as static fallback | Gopi | Open |
| R-06 | Selenium-to-Playwright produces invalid/non-runnable script | H | M | Validate converted script by executing in local test env before demo; choose simple, deterministic Selenium test as demo input | Gopi | Open |
| R-07 | UI Vision misreads banking UI elements in screenshot | H | M | Use clean, high-contrast synthetic mockup (not a real screen); avoid dense tables and small fonts; test prompt iterations Day 8 morning | Gopi | Open |
| R-08 | Manager rejects PoC due to no measurable ROI baseline | M | H | Measure current manual effort (stopwatch) on Day 2 before building; document raw numbers in METRICS.md ROI Baseline section | Gopi | Open |

---

## Likelihood / Impact Key

| Rating | Likelihood Meaning | Impact Meaning |
|--------|--------------------|----------------|
| L (Low) | Unlikely under normal conditions | Minor inconvenience, easily recovered |
| M (Medium) | Could happen; seen in similar projects | Delay or rework; demo degraded |
| H (High) | Likely without mitigation | PoC fails or pitch rejected |
| Critical | N/A | Compliance breach or data incident |

---

## Closed Risks

> None yet. Move resolved risks here with resolution note and close date.

---

## Risk Review Log

| Date | Risk ID | Update | Reviewer |
|------|---------|--------|----------|
| 2026-04-29 | All | Initial register created | Gopi |

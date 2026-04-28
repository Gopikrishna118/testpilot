---
file: PITCH-DECK.md
project: qa-forge
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# PITCH-DECK — QA-Forge Manager Presentation

> **Usage:** Use this as your slide outline. Each "## Slide N" section maps to one presentation slide. Transfer content to PowerPoint/Google Slides on Day 9.

---

## Slide 1: Title

**Headline:** QA-Forge: AI-Augmented QA Toolkit

**Subtitle:** A 10-Day PoC Sprint — Claude Sonnet 4.6 × Finastra QA Workflows

**Presenter:** Gopi | QA Engineer | Finastra
**Date:** 2026-05-08

---

## Slide 2: The Problem

> **TODO (Gopi):** Fill in your 3 real pain points from daily QA work. Be specific — use numbers where possible (hours, tickets, stories per sprint).

1. **Pain Point 1:** TODO — e.g., "Writing test cases for a single user story takes X hours of manual effort, blocking sprint velocity."
2. **Pain Point 2:** TODO — e.g., "Defect tickets are inconsistently structured, leading to Y% re-open rate and back-and-forth with developers."
3. **Pain Point 3:** TODO — e.g., "Our legacy Selenium suite takes Z weeks to migrate per module to Playwright — we're falling behind."

---

## Slide 3: The Solution — 4 PoCs at a Glance

| # | PoC | What it does | Time saved (est.) |
|---|-----|-------------|-------------------|
| 🧪 1 | **Test Case Generator** | Confluence/JIRA/BRD → Excel test cases in seconds | TODO (Gopi) |
| 🐛 2 | **JIRA Defect Creator** | Freetext description → complete JIRA ticket via API | TODO (Gopi) |
| 🔄 3 | **Selenium → Playwright** | Legacy Selenium scripts converted automatically | TODO (Gopi) |
| 👁 4 | **UI Vision** | Banking UI screenshot → test scenarios | TODO (Gopi) |

**Common thread:** Claude Sonnet 4.6 · Synthetic data only · Human review always · Production-ready architecture designed from Day 1

---

## Slide 4: Demo 1 — Test Case Generator

**Hook:** "I pasted a user story. In 8 seconds, I got 12 structured test cases ready for Excel."

**Live demo or video:** TODO (Gopi) — record 60-sec screen capture on Day 4
> [LINK TO DEMO VIDEO — TODO]

**Input used:** Synthetic KYC onboarding user story
**Output shown:** Excel file with Test ID, Scenario, Steps, Expected Result, Priority columns

**Impact:** TODO (Gopi) — X hours saved per story × Y stories per sprint

---

## Slide 5: Demo 2 — JIRA Defect Creator

**Hook:** "I described a bug in plain English. Claude structured it into a complete JIRA ticket and created it via API."

**Live demo or video:** TODO (Gopi) — record 60-sec screen capture on Day 6
> [LINK TO DEMO VIDEO — TODO]

**Input used:** Synthetic payment failure defect description
**Output shown:** JIRA ticket with Summary, Description, Steps to Reproduce, Severity, Priority, Labels

**Impact:** TODO (Gopi) — X min saved per defect × Y defects per sprint

---

## Slide 6: Demos 3 & 4 — Selenium → Playwright + UI Vision

### 🔄 Selenium → Playwright
**Hook:** "Our 3-year-old Selenium test converted to Playwright in under 10 seconds."

**Live demo or video:** TODO (Gopi) — record 60-sec screen capture on Day 7
> [LINK TO DEMO VIDEO — TODO]

### 👁 UI Vision
**Hook:** "I showed Claude a mockup of our loan application screen. It generated 8 test scenarios I hadn't thought of."

**Live demo or video:** TODO (Gopi) — record 60-sec screen capture on Day 8
> [LINK TO DEMO VIDEO — TODO]

---

## Slide 7: ROI + Risk + Security Posture

### ROI
> TODO (Gopi) — fill from METRICS.md after Day 2 baseline measurement

| Activity | Manual | AI-Assisted | Saved |
|----------|--------|-------------|-------|
| Test cases per story | X hrs | Y hrs | Z hrs |
| Defect ticket creation | X min | Y min | Z min |
| **Annual team savings** | — | — | **TODO hrs / ₹TODO** |

### Risk
- All outputs require human review (hallucination guard)
- Synthetic data only — zero PII exposure
- Production version routes through InfoSec-approved gateway

### Security
- No real customer data used · Sanitization layer · SECURITY.md on file

---

## Slide 8: The Ask

> **TODO (Gopi):** Choose one ask based on manager's likely appetite. Pick the one you believe in most and be ready to defend it.

**Option A — Minimum:** "Let me continue exploring for 2 more weeks with a second QA team member."

**Option B — Target:** "Approve a 4-week pilot: I build v1 of testcase-gen for the team, with proper InfoSec review and a shared Anthropic account."

**Option C — Stretch:** "Escalate to QA Lead: formal proposal for AI-augmented QA tooling as a team capability investment for FY2026."

---

## Appendix

- Full RISK.md available for InfoSec questions
- SECURITY.md documents data handling posture
- All code available for internal review: [link to repo — TODO]
- DECISIONS.md explains all major architecture choices

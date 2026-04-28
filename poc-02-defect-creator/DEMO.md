---
file: DEMO.md
project: qa-forge
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# DEMO — PoC 02: JIRA Defect Creator

---

## 90-Second Demo Script

**Hook (0–10s):**
> "Raising a complete JIRA defect — with proper steps, severity, and environment — takes [TODO: X minutes] when done right. Most of the time we cut corners. Let me show you a better way."

**Problem (10–20s):**
> "Here's a synthetic payment failure I found in testing. Two sentences in plain English. I'm going to paste this into QA-Forge."

**Demo Action (20–60s):**
> [Paste description → click Create Defect → watch processing indicator]
> "Claude is structuring the summary, writing reproducible steps, inferring severity, adding the component. Now it's calling the JIRA API."

**Result (60–75s):**
> [JIRA opens in browser — ticket visible] "Ticket [TODO: KEY-XXX] is live. [Scroll through fields.] Complete summary. Three-step reproduction path. Severity: High. Component: Payments. Ready for triage."

**Impact (75–90s):**
> "From plain English to a complete JIRA ticket in [TODO: Y seconds]. No developer asking 'how do I reproduce this?' [TODO: X minutes] saved per defect × [TODO: N defects/sprint]."

---

## Demo Setup Checklist

> Complete on Day 6 morning (2026-05-04) before recording.

- [ ] Backend FastAPI server running locally
- [ ] JIRA sandbox project created and accessible
- [ ] `JIRA_API_TOKEN`, `JIRA_BASE_URL`, `JIRA_EMAIL`, `JIRA_PROJECT_KEY` set in `.env`
- [ ] JIRA auth tested: manually POST a test issue via `curl` or Postman
- [ ] Synthetic defect description ready in `samples/`
- [ ] JIRA project board open in browser (for live result reveal)
- [ ] Screen recording software ready
- [ ] API connectivity tested within 30 minutes of demo

---

## Demo Input

> **TODO (Gopi):** Paste the synthetic defect description. Store in `samples/payment-failure-defect.txt`.

**Input:** [Reference: `samples/payment-failure-defect.txt`]

---

## Expected Output

> **TODO (Gopi):** Document expected JIRA ticket fields. What should the Summary, Description, Steps, Severity, Priority, Labels, Component look like?

**Expected ticket:** [Reference: `samples/expected-jira-ticket-reference.json`]

---

## Fallback Plan

If JIRA API fails:
1. Show the pre-generated JSON payload (`samples/expected-jira-ticket-reference.json`)
2. Say: *"The JIRA connection dropped — here's the structured ticket that QA-Forge generated. In a live session, this would be in JIRA right now."*

If Claude API fails:
1. Show a pre-saved screenshot of a created JIRA ticket
2. Walk through the fields as if live

---

## Demo Recording Instructions

> Record on Day 6 (2026-05-04).

1. Record the full 90-second script
2. Save as `poc-02-defect-creator-demo.mp4`
3. Store in `samples/` and add link to PITCH-DECK.md Slide 5

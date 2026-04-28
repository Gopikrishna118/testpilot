---
file: FAQ.md
project: qa-forge
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# FAQ — Anticipated Manager Questions

> **Instructions:** Prepare a concise, confident answer for every question below before the pitch. Practise answering out loud. The most important ones to nail: Q1, Q2, Q5, Q6, Q8.

---

## Q1. How is data security handled?

> **TODO (Gopi):** Prepare answer. Key points to cover: synthetic data only, sanitization layer, SECURITY.md document on file, production version via approved gateway. Reference SECURITY.md Section 8 for approval status.

---

## Q2. What if Claude gives wrong test cases?

> **TODO (Gopi):** Prepare answer. Key points: mandatory human review step, all outputs labeled "AI-GENERATED", hallucination is a known risk (R-01 in RISK.md), AI is a first-draft accelerator not a replacement, quality metrics in METRICS.md.

---

## Q3. How much will this cost in Claude API credits?

> **TODO (Gopi):** Prepare answer with actual numbers after PoC usage. Check Anthropic dashboard for token usage. Reference the cost column in ROI-SHEET.md.

---

## Q4. Why not use existing tools like Testim, Mabl, or Tricentis?

> **TODO (Gopi):** Prepare answer. Key angles: those tools are generic; this is built for Finastra's specific domain and JIRA/Confluence stack; cost comparison from ROI-SHEET.md; ownership and customisability.

---

## Q5. Has InfoSec approved this?

> **TODO (Gopi):** Prepare honest answer. Key points: PoC uses personal Claude Pro account with synthetic data only; InfoSec review is the next step post-PoC; production version designed for Bedrock/approved gateway from Day 1; see SECURITY.md Section 8.

---

## Q6. What's the ROI?

> **TODO (Gopi):** Prepare answer with measured numbers from ROI-SHEET.md. Lead with the hours saved per sprint, not money. "X hours saved per QA per sprint × Y QAs = Z hours/sprint back to the team."

---

## Q7. How long to productionise?

> **TODO (Gopi):** Prepare estimate. Consider: InfoSec approval timeline, gateway setup, production hardening, user training, ongoing support. Break into phases.

---

## Q8. Who maintains this after you build it?

> **TODO (Gopi):** Prepare answer. Options: Gopi as tool owner, shared team responsibility, a dedicated automation engineer. Maintenance items: prompt updates, API SDK upgrades, adding new PoC types.

---

## Q9. What banking regulations does this comply with?

> **TODO (Gopi):** Prepare answer. Relevant regulations to reference: DPDP Act 2023 (India), RBI data localisation guidelines, Finastra internal data policies. Key point: PoC is synthetic-data-only; compliance review is part of production approval gate.

---

## Q10. Can other QAs use this without training?

> **TODO (Gopi):** Prepare answer. Current state: requires some technical setup. Target state for production: web UI, any QA can use without coding knowledge. Estimate onboarding time for production version.

---

## Q11. What happens when Anthropic changes the API?

> **TODO (Gopi):** Prepare answer. Key points: Anthropic publishes deprecation notices in advance; model version is pinned in config; architecture designed around the SDK abstraction layer; maintenance cost is low (update model ID, re-test prompts).

---

## Q12. Do we need separate Claude licenses or seats?

> **TODO (Gopi):** Prepare answer. PoC uses API (pay-per-token, no seats). Production options: Anthropic API billing (per-token, team account), or Claude Enterprise (seat-based). Reference ADR-001 in DECISIONS.md for model choice rationale.

---

## Q13. How do you measure the quality of AI-generated test cases?

> **TODO (Gopi):** Prepare answer. Reference METRICS.md Section 5 (Quality Metrics). Proposed metric: % of AI-generated test cases accepted without modification after human review. Baseline to measure in pilot.

---

## Q14. Can this integrate with our existing CI/CD pipeline?

> **TODO (Gopi):** Prepare answer. Current state: standalone tool, file-based output. Future integration points: JIRA webhook triggers, Confluence page sync, Excel output to ALM. Production architecture would include CI/CD hooks. This is a post-pilot roadmap item.

---

## Q15. What's the rollback plan if it fails in production?

> **TODO (Gopi):** Prepare answer. Key points: the tool is additive (manual process still exists, nothing is removed); rollback = stop using the tool; no data corruption risk (outputs are files, not in-place edits); human review gate means no bad output reaches JIRA without approval.

---
file: PROMPT-LIBRARY.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-29
status: DRAFT
---

# PROMPT-LIBRARY — TestPilot Master Prompt Index

> All prompts are versioned. Use `vMAJOR.MINOR` format. Bump MINOR for refinements that don't change output schema. Bump MAJOR for structural changes to input/output format or role.

---

## Prompt Index

| Prompt File | PoC | Current Version | Status | Last Updated |
|-------------|-----|-----------------|--------|-------------|
| [testcase-gen-master.md](./testcase-gen-master.md) | poc-01-testcase-gen | v1.0 | DRAFT | 2026-04-29 |
| [defect-creator-master.md](./defect-creator-master.md) | poc-02-defect-creator | v1.0 | DRAFT | 2026-04-29 |
| [selenium-to-pw-master.md](./selenium-to-pw-master.md) | poc-03-selenium-to-playwright | v1.0 | DRAFT | 2026-04-29 |
| [ui-vision-master.md](./ui-vision-master.md) | poc-04-ui-vision | v1.0 | DRAFT | 2026-04-29 |

---

## Versioning Convention

```
v1.0   — Initial working prompt
v1.1   — Refinement (output format tweak, added example, sharpened rule)
v1.2   — Refinement (anti-hallucination guard added or updated)
v2.0   — Breaking change (new input schema, different output structure, role change)
```

---

## Prompt Change Log

| Date | Prompt File | Version | Change Description | Reason |
|------|------------|---------|-------------------|--------|
| 2026-04-29 | testcase-gen-master.md | v1.0 | Initial scaffold created | Day 1 scaffold |
| 2026-04-29 | defect-creator-master.md | v1.0 | Initial scaffold created | Day 1 scaffold |
| 2026-04-29 | selenium-to-pw-master.md | v1.0 | Initial scaffold created | Day 1 scaffold |
| 2026-04-29 | ui-vision-master.md | v1.0 | Initial scaffold created | Day 1 scaffold |

---

## Prompt Design Principles

1. **Role first** — Always start with a precise role statement so Claude understands its persona.
2. **Context second** — Provide domain context (banking QA) before the instruction.
3. **Format explicit** — Specify output format (JSON schema, Excel columns, script structure) exactly.
4. **Rules as constraints** — List what Claude must NOT do; hallucination guards go here.
5. **Examples** — At least one positive example per prompt for one-shot learning.
6. **Test iteration** — Log every significant prompt change in the Change Log above.

---

## Shared Prompt Fragments

> **TODO (Gopi):** Extract reusable prompt fragments here once patterns emerge across prompts (e.g., standard anti-hallucination footer, standard banking-domain context block).

```
# Standard Anti-Hallucination Footer (TODO — refine and add to all prompts)
IMPORTANT RULES:
- If you are not certain about a value, write "NEEDS REVIEW" — never invent data.
- Do not generate real account numbers, PAN, Aadhaar, or customer names.
- All outputs are drafts requiring mandatory human review before use.
```

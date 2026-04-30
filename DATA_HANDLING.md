---
file: DATA_HANDLING.md
project: testpilot
owner: Gopi
created: 2026-04-30
last_review: 2026-04-30
status: ACTIVE
regulations: India DPDP Act 2023 | GDPR (where applicable) | OWASP ASVS V7
---

# DATA HANDLING — TestPilot

> Governs how data is collected, processed, stored, and deleted across all 4 PoCs.
> **PoC constraint:** All data is synthetic. No personal data is collected or processed.

---

## 1. Data Inventory

| Data Type | Source | Classification | Sent to Claude? | Stored? | Retention |
|-----------|--------|---------------|-----------------|---------|-----------|
| User-supplied QA input text | QA engineer (synthetic) | INTERNAL | Yes (after sanitization) | No — in-memory only | None |
| Claude API response (raw) | Anthropic API | INTERNAL | — | No — in-memory only | None |
| Generated Excel test cases | FastAPI → openpyxl | INTERNAL | No | Yes — `outputs/` | 30 days then delete |
| Generated JSON / .ts outputs | FastAPI | INTERNAL | No | Yes — `outputs/` | 30 days then delete |
| Application logs | FastAPI logger | INTERNAL | No | stdout / optional file | 7 days |
| `ANTHROPIC_API_KEY` | Developer `.env` | RESTRICTED | No (header only) | `.env` local only | Rotate after sprint |

---

## 2. Processing Purposes and Legal Basis

| Processing Activity | Purpose | Legal Basis (DPDP 2023 §4) | Legal Basis (GDPR Art. 6) |
|--------------------|---------|-----------------------------|--------------------------|
| Sending synthetic text to Anthropic API | Generate test case drafts | Legitimate interest — internal productivity tool; no personal data | Art. 6(1)(f) — legitimate interests |
| Writing output files to `outputs/` | Provide downloadable results | Legitimate interest — internal productivity tool | Art. 6(1)(f) — legitimate interests |
| Logging request metadata | Debugging and audit | Legitimate interest — operational necessity | Art. 6(1)(f) — legitimate interests |

> **Note:** No personal data is processed. DPDP 2023 and GDPR apply only to personal data. The PoC is designed to operate entirely outside personal data scope. This analysis is included for production planning.

---

## 3. Third-Party Data Processors

| Processor | Role | Data Shared | Location | DPA Required? |
|-----------|------|------------|----------|---------------|
| Anthropic (api.anthropic.com) | LLM inference | Synthetic QA text inputs + system prompts | United States | Yes — before production |
| None (PoC is local) | — | — | — | — |

**Cross-border transfer (DPDP 2023 §16):** The Anthropic API is hosted in the US. Sending data to Anthropic constitutes a cross-border transfer under DPDP 2023. For the PoC, this is acceptable because:
1. Only synthetic data is transferred (no personal data)
2. Developer is using a personal Claude Pro account

**Production requirement:** Route via InfoSec-approved gateway (AWS Bedrock in an approved region, or Anthropic Enterprise with a signed DPA).

---

## 4. Data Subject Rights

> No personal data is collected in the PoC. The table below applies to the production version.

| Right | DPDP 2023 Reference | GDPR Reference | Production Implementation Required |
|-------|--------------------|-----------------|------------------------------------|
| Right to access | §11 | Art. 15 | API endpoint to retrieve processed records by user ID |
| Right to correction | §12 | Art. 16 | Allow re-generation with corrected input |
| Right to erasure | §13 | Art. 17 | Delete output files on request; Anthropic API retention policy applies |
| Right to nominate | §14 | — | Not applicable (employee tool) |
| Right to grievance | §13(6) | Art. 77 | Designated contact for data complaints |

---

## 5. Retention Schedule

| Data | Retention Period | Deletion Method |
|------|-----------------|-----------------|
| Excel / JSON / .ts outputs in `outputs/` | 30 days after generation | Automated `cron` delete or manual purge |
| Application logs | 7 days | Log rotation |
| `.env` (API key) | Duration of sprint | Delete after sprint ends; rotate key with Anthropic |
| Git history | Indefinitely | Must never contain API keys or real data |

---

## 6. Data Protection Impact Assessment (DPIA) — Pre-Production Requirement

A full DPIA (GDPR Art. 35 / DPDP 2023 guidance) is required before production deployment. Key questions:

| Question | PoC Answer | Production Required Action |
|----------|------------|---------------------------|
| Is personal data processed? | No — synthetic only | Confirm with InfoSec; document guarantees |
| Is data sent outside India? | Yes — Anthropic API in US | Obtain Anthropic DPA; evaluate Bedrock India region |
| Is there systematic profiling? | No | Confirm scope has not changed |
| Is there high-risk processing? | No — no financial decisions made by AI | Document that AI output is draft only, requires human review |
| Is there a Data Protection Officer? | Unknown for Finastra India | Identify DPO; inform of AI tooling |

---

## 7. Logging Standards (OWASP ASVS V7)

Logs **must not** contain:

- Raw user input (pre-sanitization text)
- Claude API raw responses
- `ANTHROPIC_API_KEY` or any credential
- Full file paths of output files (log filename only)

Logs **must** contain:

- Timestamp (ISO 8601 UTC)
- Request ID (UUID)
- `input_type` value
- Sanitization result: `pii_detected: true/false`, `redaction_count: N`
- Claude API response status code
- Output filename (not full path)
- Any error codes with non-sensitive context

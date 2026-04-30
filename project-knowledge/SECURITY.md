---
file: SECURITY.md
project: testpilot
owner: Gopi
created: 2026-04-29
last_review: 2026-04-30
status: ACTIVE
controls: OWASP ASVS v4.0 L1 | NIST CSF | India DPDP Act 2023
---

# SECURITY — TestPilot Compliance & Data Handling

> **CRITICAL:** This document governs all data handling decisions across all 4 PoCs.
> All inputs are synthetic. No real customer, employee, or transaction data may be used.

---

## 1. Data Classification

| Class | Label | Banking Examples | TestPilot Handling |
|-------|-------|-----------------|-------------------|
| Public | PUBLIC | Published API docs, product brochures | May be used as-is |
| Internal | INTERNAL | Internal process docs, generic test templates | Use after review |
| Confidential | CONFIDENTIAL | Customer accounts, PAN, Aadhaar, KYC, transaction IDs | **NEVER** — replace with synthetic |
| Restricted | RESTRICTED | Prod credentials, API keys, HSM material, encryption keys | **NEVER** — `.env` only, never commit |

---

## 2. Data Flow

```
User Input (synthetic only)
  → Sanitization Layer (regex PII scrub + validation)
  → PII detected? YES → Reject 400 + log sanitization event
                  NO  → Anthropic API (Claude Sonnet 4.6)
                         → Output (Excel / JSON / .ts script)
                            → Human Review (mandatory before use)
```

---

## 3. What IS Sent to Claude API

- Synthetic user story text (no real names, accounts)
- Synthetic BRD / Confluence content (fabricated scenarios)
- Sanitized Selenium scripts (no real URLs, no credentials)
- Synthetic UI screenshots (mockups only, no production screens)
- Structural prompts and formatting instructions

---

## 4. What Is NEVER Sent to Claude API

| Data Type | Pattern | Example |
|-----------|---------|---------|
| Indian bank account numbers | 9–18 digit numeric | `012345678901` |
| PAN card | `[A-Z]{5}[0-9]{4}[A-Z]` | `ABCDE1234F` |
| Aadhaar | 12-digit (with optional spaces/dashes) | `1234 5678 9012` |
| Email addresses | standard email format | `user@bank.com` |
| Indian mobile numbers | `+91` prefix or `[6-9]\d{9}` | `+91 9876543210` |
| Credit / debit card | 13–16 digit numeric | `4111111111111111` |
| SWIFT / BIC codes | `[A-Z]{6}[A-Z0-9]{2,5}` | `HDFCINBBXXX` |
| Real JIRA tickets with PII | any | — |
| Production source code with secrets | any | — |
| API keys / passwords / tokens | any | — |

---

## 5. Sanitization Rules (`shared/utils/sanitizer.py`)

All inputs pass through the sanitizer **before** any Claude API call. The sanitizer raises `PII_DETECTED` and rejects the request if any pattern matches.

| Pattern | Regex | Action |
|---------|-------|--------|
| Indian bank account | `\b\d{9,18}\b` | Replace → `[ACCT-REDACTED]`, reject |
| PAN card | `[A-Z]{5}[0-9]{4}[A-Z]{1}` | Replace → `[PAN-REDACTED]`, reject |
| Aadhaar | `\b\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b` | Replace → `[AADHAAR-REDACTED]`, reject |
| Email | `[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}` | Replace → `[EMAIL-REDACTED]`, reject |
| Indian mobile | `(\+91[\s\-]?)?[6-9]\d{9}` | Replace → `[PHONE-REDACTED]`, reject |
| Credit/debit card | `\b(?:\d[ \-]?){13,16}\b` | Replace → `[CARD-REDACTED]`, reject |
| SWIFT BIC | `[A-Z]{6}[A-Z0-9]{2,5}` | Flag → `[SWIFT-REVIEW]`, reject |
| IFSC code | `[A-Z]{4}0[A-Z0-9]{6}` | Flag → `[IFSC-REVIEW]`, manual review |

> Refine patterns with InfoSec before production. IBAN and Finastra-specific identifiers to be added.

---

## 6. OWASP ASVS v4.0 Control Alignment (Level 1)

| ASVS Control | ID | Implementation |
|---|---|---|
| Architecture, design, and threat modeling | V1.1 | See THREAT_MODEL.md |
| Input validation | V5.1 | Sanitizer + Pydantic validators on all inputs |
| Output encoding | V5.3 | JSON schema validation on Claude response before Excel write |
| API security | V9.1 | HTTPS-only for Anthropic API calls; SDK enforces TLS 1.2+ |
| Sensitive data in logs | V7.1 | Logger must never log raw user input or Claude responses |
| Secrets management | V2.10 | API keys in `.env` only; `.gitignore` enforced |
| File upload | V12.1 | Max input size enforced at FastAPI layer (10 KB text limit) |
| Dependency security | V14.2 | Pin all versions in `requirements.txt`; review before prod |

---

## 7. NIST CSF Alignment

| Function | Category | TestPilot Control |
|----------|----------|-------------------|
| Identify | Asset Management | Data classification table (§1); .env secret inventory |
| Protect | Data Security | Sanitizer gate; HTTPS; no PII in logs |
| Protect | Protective Technology | Pydantic input validation; output schema validation |
| Detect | Anomalies & Events | Structured logger; sanitization events logged with timestamp |
| Respond | Response Planning | Incident response procedure (§9) |
| Recover | Recovery Planning | Outputs are files; no DB rollback needed for PoC |

---

## 8. India DPDP Act 2023 & GDPR Alignment

| Requirement | Applicable Law | Status |
|---|---|---|
| Lawful purpose for processing | DPDP 2023 §4 | Processing is internal QA productivity — no customer data processed |
| Data minimisation | GDPR Art. 5(1)(c) | Only synthetic data; no personal data collected |
| Cross-border transfer assessment | DPDP 2023 §16 | Anthropic API in US — PoC uses personal account; production requires approved gateway |
| Data breach notification | DPDP 2023 §8 | See §9 incident response |
| Data Protection Impact Assessment | GDPR Art. 35 | DPIA required before production rollout; see DATA_HANDLING.md |

---

## 9. Incident Response

| Scenario | Immediate Action | Notify Within | Escalation |
|----------|-----------------|---------------|-----------|
| Suspected PII sent to API | Rotate `ANTHROPIC_API_KEY`; preserve logs | 1 hour | Manager → InfoSec lead |
| API key committed to git | `git filter-branch` or BFG to purge; rotate key | Immediately | Manager → InfoSec lead |
| Unauthorized access to outputs | Identify scope; delete compromised files | 4 hours | Manager → Data Protection contact |
| Real data found in PoC input | Stop all PoC usage; audit previous runs | 1 hour | Manager → InfoSec → DPO if applicable |

> Identify contacts before pitch: Direct manager, InfoSec team lead, DPO (if applicable under DPDP 2023).

---

## 10. API Provider

| Item | Detail |
|------|--------|
| Provider | Anthropic (api.anthropic.com) |
| Model | Claude Sonnet 4.6 (`claude-sonnet-4-6`) |
| SDK | `anthropic` Python package ≥ 0.28.0 |
| TLS | 1.2+ enforced by SDK |
| Data retention | Verify at docs.anthropic.com — confirm before pitch |
| PoC account | Personal Claude Pro (Gopi) — PoC only |
| Production path | InfoSec-approved gateway (AWS Bedrock or Anthropic Enterprise) |

---

## 11. Developer Pre-Run Checklist

- [ ] All inputs are 100% synthetic — no real customer, transaction, or employee data
- [ ] `.env` present and **not** staged in git (`git status` check)
- [ ] Sanitizer is active — verify via `/health` endpoint response
- [ ] No screenshots of real Finastra production screens in `poc-04`
- [ ] All outputs labeled **"AI-GENERATED — REQUIRES HUMAN REVIEW"** before sharing
- [ ] `requirements.txt` pinned versions reviewed for known CVEs before demo

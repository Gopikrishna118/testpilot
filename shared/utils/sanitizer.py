"""
shared/utils/sanitizer.py — PII detection and redaction for TestPilot.

Detects and redacts seven categories of sensitive data found in banking-domain
QA inputs before they reach external AI APIs.

Public interface
----------------
detect(text)      — Validate: raises PIIDetectedError if PII is present,
                    returns [] when the input is clean.
redact(text)      — Clean: returns text with all PII replaced by
                    [REDACTED-<TYPE>] tokens.
PIIDetectedError  — Exception whose ``detections`` attribute carries the full
                    match list so callers can inspect what was found.

Overlap resolution
------------------
When two patterns match overlapping spans, the longest span is kept. For spans
of equal length, the leftmost is retained. Substitutions in redact() are applied
right-to-left so that earlier character positions remain stable.

Known limitations
-----------------
- Unicode homoglyphs (e.g. Cyrillic 'а' vs Latin 'a') are NOT normalised before
  matching. Inputs containing visually identical Unicode substitutes can evade
  all patterns here. Normalise to NFKC and replace known lookalikes upstream
  when the source is untrusted rich text.
- SWIFT/BIC and IBAN patterns err on the side of false positives: any sequence
  of uppercase letters and digits that matches the structural format is flagged,
  even if not a genuine code.
- Phone detection for Indian numbers treats any 10-digit string starting with
  6–9 as a mobile number (with or without +91 prefix), which may produce false
  positives on account reference numbers in that range.
- Credit card detection is the only pattern that applies a semantic check
  (Luhn algorithm); all others are structural regex only.
"""

from __future__ import annotations

import logging
import re
from typing import Any

logger = logging.getLogger(__name__)

# ── Compiled patterns (module-level for performance) ─────────────────────────

_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    (
        "CREDIT_CARD",
        # 16 digits, optional space/hyphen separators every 4 digits.
        # Luhn check applied after match — see _find_matches().
        re.compile(r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"),
    ),
    (
        "AADHAAR",
        # 12 digits in groups of 4, optional space or hyphen between groups.
        re.compile(r"\b\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b"),
    ),
    (
        "PAN",
        # Indian Permanent Account Number: ABCDE1234F (5 alpha, 4 digit, 1 alpha).
        re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"),
    ),
    (
        "EMAIL",
        re.compile(r"\b[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}\b"),
    ),
    (
        "PHONE",
        re.compile(
            # Indian mobile: optional +91 prefix, then 10 digits starting with 6–9.
            r"(?:\+91[\s\-]?)?[6-9]\d{9}"
            r"|"
            # International E.164: + followed by 7–15 digits.
            r"\+[1-9]\d{6,14}"
        ),
    ),
    (
        "SWIFT_BIC",
        # 4-char bank code + 2-char country + 2-char location + optional 3-char branch.
        re.compile(r"\b[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}(?:[A-Z0-9]{3})?\b"),
    ),
    (
        "IBAN",
        # 2-letter country code + 2 check digits + 11–30 alphanumeric BBAN (total 15–34).
        re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b"),
    ),
]


# ── Custom exception ──────────────────────────────────────────────────────────

class PIIDetectedError(Exception):
    """Raised by :func:`detect` when one or more PII patterns match.

    Attributes:
        detections: List of match dicts, each containing
                    ``type`` (str), ``value`` (str), ``start`` (int), ``end`` (int).
    """

    def __init__(self, detections: list[dict[str, Any]]) -> None:
        self.detections = detections
        types = sorted({d["type"] for d in detections})
        super().__init__(
            f"PII detected — {len(detections)} match(es): {', '.join(types)}"
        )


# ── Internal helpers ──────────────────────────────────────────────────────────

def _luhn_valid(value: str) -> bool:
    """Return True if *value* (digits only) satisfies the Luhn mod-10 algorithm."""
    digits = [int(c) for c in value if c.isdigit()]
    digits.reverse()
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def _resolve_overlaps(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return *candidates* with overlapping spans removed.

    Retains the longest span; for equal-length ties, the leftmost is kept.
    """
    # Primary sort: longest span first. Secondary: leftmost start.
    ranked = sorted(
        candidates,
        key=lambda m: (-(m["end"] - m["start"]), m["start"]),
    )
    accepted: list[dict[str, Any]] = []
    for candidate in ranked:
        overlaps_existing = any(
            candidate["start"] < kept["end"] and candidate["end"] > kept["start"]
            for kept in accepted
        )
        if not overlaps_existing:
            accepted.append(candidate)
    return sorted(accepted, key=lambda m: m["start"])


def _find_matches(text: str) -> list[dict[str, Any]]:
    """Scan *text* with all patterns and return resolved, position-sorted matches."""
    candidates: list[dict[str, Any]] = []
    for pii_type, pattern in _PATTERNS:
        for m in pattern.finditer(text):
            if pii_type == "CREDIT_CARD" and not _luhn_valid(m.group()):
                continue
            candidates.append({
                "type": pii_type,
                "value": m.group(),
                "start": m.start(),
                "end": m.end(),
            })
    return _resolve_overlaps(candidates)


# ── Public API ────────────────────────────────────────────────────────────────

def detect(text: str) -> list[dict[str, Any]]:
    """Validate *text* for PII and raise if any is found.

    Scans for seven pattern types: CREDIT_CARD (Luhn-validated), AADHAAR,
    PAN, EMAIL, PHONE (Indian and international), SWIFT_BIC, and IBAN.

    Each detection event is logged at WARNING level showing type and character
    position only — the matched value is never written to the log.

    Args:
        text: Input string to scan. ``None`` or empty string returns ``[]``
              without raising.

    Returns:
        An empty list when no PII is found.

    Raises:
        PIIDetectedError: If one or more patterns match. The exception's
            ``detections`` attribute contains the full list of matches.
    """
    if not text:
        return []

    matches = _find_matches(text)
    if not matches:
        return []

    for m in matches:
        logger.warning(
            "PII detected | type=%s start=%d end=%d",
            m["type"], m["start"], m["end"],
        )
    raise PIIDetectedError(matches)


def redact(text: str) -> str:
    """Replace all PII in *text* with ``[REDACTED-<TYPE>]`` tokens.

    Applies the same seven-pattern scan as :func:`detect` but returns cleaned
    text instead of raising. Overlapping spans are resolved before substitution
    (longest wins). Replacements are applied right-to-left so that unprocessed
    character positions remain stable throughout the pass.

    Each redaction is logged at WARNING level showing type and position only —
    the original value is never written to the log.

    Args:
        text: Input string to clean. ``None`` or empty string is returned
              unchanged without raising.

    Returns:
        The input string with all detected PII replaced by ``[REDACTED-<TYPE>]``
        tokens, or the original string if no PII was found.
    """
    if not text:
        return text

    matches = _find_matches(text)
    if not matches:
        return text

    for m in matches:
        logger.warning(
            "PII redacted | type=%s start=%d end=%d",
            m["type"], m["start"], m["end"],
        )

    result = text
    for m in reversed(matches):
        result = result[: m["start"]] + f"[REDACTED-{m['type']}]" + result[m["end"] :]
    return result

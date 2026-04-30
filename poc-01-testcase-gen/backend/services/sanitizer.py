"""
PII sanitizer for TestPilot.
Mirrors shared/utils/sanitizer.py — consolidate into the shared package once
a proper PYTHONPATH / editable install is set up for production.
"""
import re
from dataclasses import dataclass, field

_REPLACEMENTS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\b\d{9,18}\b"), "[ACCT-REDACTED]"),
    (re.compile(r"[A-Z]{5}[0-9]{4}[A-Z]{1}"), "[PAN-REDACTED]"),
    (re.compile(r"\b\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b"), "[AADHAAR-REDACTED]"),
    (re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"), "[EMAIL-REDACTED]"),
    (re.compile(r"(\+91[\s\-]?)?[6-9]\d{9}"), "[PHONE-REDACTED]"),
    (re.compile(r"\b(?:\d[ \-]?){13,16}\b"), "[CARD-REDACTED]"),
    (re.compile(r"[A-Z]{6}[A-Z0-9]{2,5}"), "[SWIFT-REVIEW]"),
]
_IFSC = re.compile(r"[A-Z]{4}0[A-Z0-9]{6}")


@dataclass
class SanitizationResult:
    text: str
    redactions: list[str] = field(default_factory=list)
    ifsc_flags: list[str] = field(default_factory=list)
    pii_detected: bool = False


class Sanitizer:
    @staticmethod
    def scrub(text: str) -> SanitizationResult:
        clean = text
        redactions: list[str] = []

        for pattern, replacement in _REPLACEMENTS:
            matches = pattern.findall(clean)
            if matches:
                redactions.extend(str(m) for m in matches)
            clean = pattern.sub(replacement, clean)

        ifsc_flags = _IFSC.findall(clean)

        return SanitizationResult(
            text=clean,
            redactions=redactions,
            ifsc_flags=ifsc_flags,
            pii_detected=bool(redactions),
        )

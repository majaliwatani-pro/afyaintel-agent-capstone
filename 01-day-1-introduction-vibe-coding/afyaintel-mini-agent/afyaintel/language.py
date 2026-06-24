from __future__ import annotations

SWAHILI_MARKERS = {
    "naomba",
    "tafadhali",
    "dawa",
    "akiba",
    "hali",
    "kipimo",
    "imeisha",
    "zilizobaki",
    "karibu",
    "ripoti",
    "kituo",
    "nini",
    "nisaidie",
    "kwa kiswahili",
    "homa",
    "mgonjwa",
    "muda wa matumizi",
    "chini ya kiwango",
}


def detect_language(text: str) -> str:
    normalized = text.lower()
    score = sum(marker in normalized for marker in SWAHILI_MARKERS)
    return "sw" if score > 0 else "en"

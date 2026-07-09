"""Text normalization and token-span utilities for UzbekTaggerBERT."""

from __future__ import annotations

import re
from typing import List, Tuple


# Common apostrophe variants found in Uzbek Latin text.
APOSTROPHE_MAP = {
    "‘": "ʻ",
    "’": "ʻ",
    "`": "ʻ",
    "´": "ʻ",
    "ʼ": "ʻ",
    "ʻ": "ʻ",
}


def normalize_uzbek_text(text: str) -> str:
    """Normalize common apostrophe variants in Uzbek Latin text.

    The function intentionally keeps the text lightweight and transparent.
    It can be extended with Cyrillic-to-Latin transliteration or domain-specific
    normalization rules in later versions.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    normalized = text
    for old, new in APOSTROPHE_MAP.items():
        normalized = normalized.replace(old, new)

    # Normalize excessive whitespace while preserving token boundaries.
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def word_spans(text: str) -> List[Tuple[str, int, int]]:
    """Return tokens with character spans.

    The tokenizer keeps Uzbek words containing apostrophes as one token, and
    separates punctuation marks as independent tokens. This is useful for
    mapping Transformer subword predictions back to original words.
    """
    pattern = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿЀ-ӿ0-9]+(?:[ʻ'’-][A-Za-zÀ-ÖØ-öø-ÿЀ-ӿ0-9]+)*|[^\w\s]", re.UNICODE)
    return [(m.group(0), m.start(), m.end()) for m in pattern.finditer(text)]


def overlap_size(a_start: int, a_end: int, b_start: int, b_end: int) -> int:
    """Return the overlap length of two character spans."""
    return max(0, min(a_end, b_end) - max(a_start, b_start))

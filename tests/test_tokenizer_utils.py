"""Text normalization and span utility tests."""

from uzbek_tagger_bert.tokenizer_utils import normalize_uzbek_text, overlap_size, word_spans


def test_normalize_apostrophes():
    text = "O'rgan O‘rgan Oʼrgan Oʻrgan G‘afur ma’no"
    normalized = normalize_uzbek_text(text)
    assert "O'rgan" in normalized
    assert "Gʻafur" in normalized
    assert "maʻno" in normalized


def test_word_spans_keeps_uzbek_words():
    text = normalize_uzbek_text("O‘rgan yaxshi odatdir.")
    spans = word_spans(text)
    tokens = [item[0] for item in spans]
    assert len(tokens) >= 4
    assert tokens[-1] == "."


def test_overlap_size():
    assert overlap_size(0, 5, 2, 7) == 3
    assert overlap_size(0, 5, 5, 9) == 0
    assert overlap_size(10, 20, 0, 30) == 10

"""Output-format tests that do not require model download."""

from uzbek_tagger_bert.tagger import UzbekTaggerBERT


def test_to_slash_without_model_initialization():
    tagger = UzbekTaggerBERT.__new__(UzbekTaggerBERT)
    tagged = [
        {"token": "Bugun", "pos": "ADV", "start": 0, "end": 5},
        {"token": "talabalar", "pos": "NOUN", "start": 6, "end": 15},
        {"token": ".", "pos": "PUNCT", "start": 15, "end": 16},
    ]
    assert tagger.to_slash(tagged) == "Bugun/ADV talabalar/NOUN ./PUNCT"


def test_to_conll_without_model_initialization():
    tagger = UzbekTaggerBERT.__new__(UzbekTaggerBERT)
    tagged = [
        {"token": "Bugun", "pos": "ADV", "start": 0, "end": 5},
        {"token": "talabalar", "pos": "NOUN", "start": 6, "end": 15},
    ]
    assert tagger.to_conll(tagged) == "Bugun\tADV\ntalabalar\tNOUN"


def test_to_json_without_model_initialization():
    tagger = UzbekTaggerBERT.__new__(UzbekTaggerBERT)
    tagged = [{"token": "Bugun", "pos": "ADV", "start": 0, "end": 5}]
    assert tagger.to_json(tagged) == tagged

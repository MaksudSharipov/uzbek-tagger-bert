"""POS label-map tests."""

from uzbek_tagger_bert.label_map import POS_DESCRIPTIONS, POS_LABELS


def test_pos_label_count():
    assert len(POS_LABELS) == 16


def test_required_labels_exist():
    required = {"NOUN", "VERB", "ADJ", "ADV", "PRON", "PROPN", "NUM", "PUNCT"}
    assert required.issubset(set(POS_LABELS))


def test_descriptions_cover_labels():
    for label in POS_LABELS:
        assert label in POS_DESCRIPTIONS
        assert isinstance(POS_DESCRIPTIONS[label], str)
        assert POS_DESCRIPTIONS[label]

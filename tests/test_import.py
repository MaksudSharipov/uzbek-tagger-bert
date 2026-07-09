"""Import tests for UzbekTaggerBERT."""

import uzbek_tagger_bert


def test_package_imports():
    assert hasattr(uzbek_tagger_bert, "UzbekTaggerBERT")
    assert hasattr(uzbek_tagger_bert, "UzbekPOSTagger")
    assert hasattr(uzbek_tagger_bert, "POS_LABELS")


def test_version_exists():
    assert isinstance(uzbek_tagger_bert.__version__, str)
    assert len(uzbek_tagger_bert.__version__) > 0

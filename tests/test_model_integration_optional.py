"""Optional integration test for the real Hugging Face model.

This test is skipped by default because it downloads the Transformer model.
Run it manually with:

    RUN_MODEL_TESTS=1 pytest tests/test_model_integration_optional.py
"""

import os

import pytest


@pytest.mark.skipif(
    os.environ.get("RUN_MODEL_TESTS") != "1",
    reason="Real model test is disabled by default. Set RUN_MODEL_TESTS=1 to run.",
)
def test_real_model_basic_prediction():
    from uzbek_tagger_bert import UzbekTaggerBERT

    tagger = UzbekTaggerBERT()
    output = tagger("U yuz burib ketdi va yuz soat ishladi.")
    assert isinstance(output, str)
    assert "yuz/" in output

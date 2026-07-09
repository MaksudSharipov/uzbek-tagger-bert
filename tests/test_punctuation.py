"""Tests for punctuation post-processing override."""

from unittest.mock import MagicMock
import torch
from uzbek_tagger_bert.tagger import UzbekTaggerBERT


def test_punctuation_override_without_model():
    # Instantiate without calling __init__ (no model loading)
    tagger = UzbekTaggerBERT.__new__(UzbekTaggerBERT)
    tagger.max_length = 256
    tagger.device = "cpu"
    tagger.id2label = {0: "NOUN"}
    
    # Mock tokenizer
    tagger.tokenizer = MagicMock()
    mock_encoded = MagicMock()
    # mock offset mapping for pop("offset_mapping")[0].tolist()
    mock_encoded.pop.return_value = torch.tensor([[[0, 0]] * 20])
    mock_encoded.items.return_value = []
    tagger.tokenizer.return_value = mock_encoded
    
    # Mock model logits
    tagger.model = MagicMock()
    mock_output = MagicMock()
    mock_output.logits = torch.zeros(1, 20, 1)
    tagger.model.return_value = mock_output
    
    # Tag string containing standard punctuation marks
    results = tagger.tag_text("U . , ! ?")
    
    # Map tokens to their predicted/post-processed POS tag
    token_to_pos = {item["token"]: item["pos"] for item in results}
    
    # Ensure they are all overridden to PUNCT
    assert token_to_pos["."] == "PUNCT"
    assert token_to_pos[","] == "PUNCT"
    assert token_to_pos["!"] == "PUNCT"
    assert token_to_pos["?"] == "PUNCT"

"""Model-loading utilities for UzbekTaggerBERT."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer


DEFAULT_MODEL_NAME = "MaksudSharipov/Uzbek-POS-Tagger-TahrirchiBERT"


@dataclass
class LoadedModel:
    tokenizer: object
    model: object
    device: torch.device


def resolve_device(device: Optional[str] = None) -> torch.device:
    """Resolve CPU/GPU device."""
    if device is None or device == "auto":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    return torch.device(device)


def load_model(
    model_name: str = DEFAULT_MODEL_NAME,
    device: Optional[str] = "auto",
) -> LoadedModel:
    """Load tokenizer and token-classification model from Hugging Face Hub."""
    resolved_device = resolve_device(device)
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    model.to(resolved_device)
    model.eval()
    return LoadedModel(tokenizer=tokenizer, model=model, device=resolved_device)

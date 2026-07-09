"""Main POS tagger implementation for UzbekTaggerBERT."""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Sequence, Union

import torch

from .label_map import POS_LABELS
from .model_loader import DEFAULT_MODEL_NAME, load_model
from .tokenizer_utils import normalize_uzbek_text, overlap_size, word_spans


class UzbekTaggerBERT:
    """Transformer-based part-of-speech tagger for Uzbek.

    Parameters
    ----------
    model_name:
        Hugging Face model identifier or local model path.
    device:
        "auto", "cpu", "cuda", or another valid PyTorch device string.
    max_length:
        Maximum sequence length passed to the Transformer tokenizer.
    """

    def __init__(
        self,
        model_name: str = DEFAULT_MODEL_NAME,
        device: Optional[str] = "auto",
        max_length: int = 256,
    ) -> None:
        loaded = load_model(model_name=model_name, device=device)
        self.model_name = model_name
        self.tokenizer = loaded.tokenizer
        self.model = loaded.model
        self.device = loaded.device
        self.max_length = max_length

        self.id2label = self._load_id2label()

    def _load_id2label(self) -> Dict[int, str]:
        """Load id-to-label mapping from model config, with fallback labels."""
        config_map = getattr(self.model.config, "id2label", None)
        if isinstance(config_map, dict) and config_map:
            return {int(k): str(v) for k, v in config_map.items()}
        return {idx: label for idx, label in enumerate(POS_LABELS)}

    def tag_text(self, text: str) -> List[Dict[str, Union[str, int]]]:
        """Tag Uzbek text and return token-level dictionaries.

        Returns
        -------
        list of dict
            Example: [{"token": "Bugun", "pos": "ADV", "start": 0, "end": 5}, ...]
        """
        normalized = normalize_uzbek_text(text)
        tokens = word_spans(normalized)

        if not tokens:
            return []

        encoded = self.tokenizer(
            normalized,
            return_offsets_mapping=True,
            return_tensors="pt",
            truncation=True,
            max_length=self.max_length,
        )

        offsets = encoded.pop("offset_mapping")[0].tolist()
        encoded = {key: value.to(self.device) for key, value in encoded.items()}

        with torch.no_grad():
            logits = self.model(**encoded).logits[0].detach().cpu()

        results: List[Dict[str, Union[str, int]]] = []

        for token, start, end in tokens:
            overlapping_indices = []
            for idx, (sub_start, sub_end) in enumerate(offsets):
                # Ignore special tokens and empty spans.
                if sub_start == sub_end:
                    continue
                if overlap_size(start, end, sub_start, sub_end) > 0:
                    overlapping_indices.append(idx)

            if overlapping_indices:
                token_logits = logits[overlapping_indices].mean(dim=0)
                label_id = int(torch.argmax(token_logits).item())
                label = self.id2label.get(label_id, str(label_id))
            else:
                label = "PUNCT" if not token.isalnum() else "X"

            # Post-process punctuation override
            punctuation_chars = set(".,!?;:()[]{}\"'‘’“”…-—")
            if token in punctuation_chars or all(c in punctuation_chars for c in token):
                label = "PUNCT"

            results.append(
                {
                    "token": token,
                    "pos": label,
                    "start": start,
                    "end": end,
                }
            )

        return results

    def tag_sentence(self, sentence: str) -> List[Dict[str, Union[str, int]]]:
        """Alias for tag_text for a single sentence."""
        return self.tag_text(sentence)

    def tag_batch(self, sentences: Sequence[str]) -> List[List[Dict[str, Union[str, int]]]]:
        """Tag a batch of sentences.

        This method currently prioritizes transparency and identical output with
        single-sentence tagging. A later version may implement a fully batched
        inference path for speed.
        """
        return [self.tag_text(sentence) for sentence in sentences]

    def to_slash(self, tagged_tokens: List[Dict[str, Union[str, int]]]) -> str:
        """Convert tagged output to token/POS text format."""
        return " ".join(f"{item['token']}/{item['pos']}" for item in tagged_tokens)

    def to_conll(self, tagged_tokens: List[Dict[str, Union[str, int]]]) -> str:
        """Convert tagged output to a simple CoNLL-like two-column format."""
        return "\n".join(f"{item['token']}\t{item['pos']}" for item in tagged_tokens)

    def to_json(self, tagged_tokens: List[Dict[str, Union[str, int]]]) -> List[Dict[str, Union[str, int]]]:
        """Return tagged tokens as JSON-serializable dictionaries."""
        return tagged_tokens

    def tag(self, text: str, output_format: str = "slash"):
        """Tag text and return one of the supported output formats.

        Supported formats: "slash", "json", "conll".
        """
        tagged = self.tag_text(text)

        if output_format == "slash":
            return self.to_slash(tagged)
        if output_format == "json":
            return self.to_json(tagged)
        if output_format == "conll":
            return self.to_conll(tagged)

        raise ValueError("output_format must be one of: slash, json, conll")

    def __call__(self, text: str, output_format: str = "slash"):
        """Call interface used in quick-start examples."""
        return self.tag(text, output_format=output_format)


# Backward-compatible alias for users who prefer a descriptive class name.
UzbekPOSTagger = UzbekTaggerBERT

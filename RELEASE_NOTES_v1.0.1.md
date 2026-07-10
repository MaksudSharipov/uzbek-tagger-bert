## UzbekTaggerBERT v1.0.1

This release provides the SoftwareX-ready version of UzbekTaggerBERT, an open-source Python library for Transformer-based part-of-speech tagging of the Uzbek language.

### Highlights

- Transformer-based POS tagging for Uzbek texts.
- Fine-tuned Tahrirchi-BERT model integration.
- Python API and command-line interface (`uzbek-tagger`).
- Support for 16 Universal POS tags.
- Uzbek apostrophe normalization for Latin-script text.
- Overlap-based offset mapping for subword-to-word alignment.
- Deterministic punctuation post-processing: punctuation tokens are always tagged as `PUNCT`.
- Examples, tests, documentation, and benchmark scripts included.
- Prepared for SoftwareX original software publication submission.

### Repository structure

- `repo/src/uzbek_tagger_bert/` — source code
- `examples/` — usage examples
- `tests/` — unit and integration tests
- `benchmark/` — evaluation and speed-test scripts
- `docs/` — installation, usage, and tagset documentation

### Validation

The package was validated with:

- 12 unit tests passed
- 1 optional Hugging Face model integration test passed
- Python API examples passed
- CLI tests passed for slash, JSON, and CoNLL-like outputs
- Punctuation tokens are correctly returned as `PUNCT`
- Inference speed benchmark completed successfully

### Reported POS tagging performance

- Accuracy: 0.9810
- Weighted F1: 0.9811

### Installation

```bash
pip install uzbek-tagger-bert
```

### Model

https://huggingface.co/MaksudSharipov/Uzbek-POS-Tagger-TahrirchiBERT

### License

Apache License 2.0

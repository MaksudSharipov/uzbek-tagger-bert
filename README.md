
# UzbekTaggerBERT

[![PyPI version](https://badge.fury.io/py/uzbek-tagger-bert.svg)](https://pypi.org/project/uzbek-tagger-bert/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-%3E%3D3.7-blue.svg)](https://www.python.org/)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Model-yellow.svg)](https://huggingface.co/MaksudSharipov/Uzbek-POS-Tagger-TahrirchiBERT)

**UzbekTaggerBERT** is an open-source Python library for Transformer-based part-of-speech tagging of the Uzbek language. It is built on a fine-tuned **Tahrirchi-BERT** model and is designed to assign Universal POS tags to Uzbek words in context.

The library addresses key challenges of Uzbek NLP, including agglutinative word formation, contextual homonym disambiguation, apostrophe normalization, and subword-to-word alignment in Transformer-based token classification.

## Main Features

- Transformer-based POS tagging for Uzbek texts.
- Fine-tuned Tahrirchi-BERT model for contextual POS prediction.
- Support for 16 Universal POS tags.
- Contextual homonym disambiguation, for example distinguishing *yuz* as a noun or numeral depending on context.
- Smart apostrophe normalization for Uzbek Latin texts.
- Overlap-based offset mapping for aligning subword tokens with original words.
- Python API for integration into Uzbek NLP pipelines.
- Command-line interface for quick text tagging.
- Public distribution through PyPI and Hugging Face Hub.

## Installation

Install the package from PyPI:

```bash
pip install uzbek-tagger-bert
```

The package requires Python 3.7 or higher. The main dependencies are `torch`, `transformers`, and `numpy`.

For development installation from GitHub:

```bash
git clone https://github.com/MaksudSharipov/uzbek-tagger-bert.git
cd uzbek-tagger-bert
pip install -e .
```

## Quick Start

```python
from uzbek_tagger_bert import UzbekTaggerBERT

tagger = UzbekTaggerBERT()

text = (
    "U yuz burib ketdi va yuz soat ishladi. "
    "Alisher sariq olma olib menga qizil olma olmading dedi."
)

result = tagger(text)

print(result)
```

Expected output:

```text
U/PRON yuz/NOUN burib/VERB ketdi/VERB va/CCONJ yuz/NUM soat/NOUN ishladi/VERB ./PUNCT
Alisher/PROPN sariq/ADJ olma/NOUN olib/VERB menga/PRON qizil/ADJ olma/NOUN olmading/VERB dedi/VERB ./PUNCT
```

## Command-Line Usage

After installation, the package provides the `uzbek-tagger` command:

```bash
uzbek-tagger "U yuz burib ketdi va yuz soat ishladi."
```

JSON output:

```bash
uzbek-tagger "Bugun talabalar yangi mavzuni o‘rgandilar." --format json
```

CoNLL-like output:

```bash
uzbek-tagger "Bozordan olma olib kel." --format conll
```

## POS Tagset

UzbekTaggerBERT supports 16 Universal POS tags:

| Tag | Description | Uzbek explanation |
|---|---|---|
| ADJ | Adjective | Sifat |
| ADP | Adposition | Ko‘makchi |
| ADV | Adverb | Ravish |
| AUX | Auxiliary | Yordamchi fe’l |
| CCONJ | Coordinating conjunction | Teng bog‘lovchi |
| INTJ | Interjection | Undov |
| MOD | Modal word | Modal so‘z |
| NOUN | Noun | Ot |
| NUM | Numeral | Son |
| PART | Particle | Yuklama |
| PRON | Pronoun | Olmosh |
| PROPN | Proper noun | Atoqli ot |
| PUNCT | Punctuation | Tinish belgisi |
| SCONJ | Subordinating conjunction | Ergash bog‘lovchi |
| SYM | Symbol | Simvol |
| VERB | Verb | Fe’l |

More information is available in [`docs/tagset.md`](docs/tagset.md).

## Model

The core POS tagging model is available on Hugging Face Hub:

```text
MaksudSharipov/Uzbek-POS-Tagger-TahrirchiBERT
```

Model page:

```text
https://huggingface.co/MaksudSharipov/Uzbek-POS-Tagger-TahrirchiBERT
```

## Model Performance

The current public version reports the following evaluation results on the UzbekPOS test dataset:

| Metric | Score |
|---|---:|
| Accuracy | 0.9810 |
| Weighted F1 | 0.9811 |

Additional benchmark results, per-tag scores, baseline comparisons, and inference-speed tests are stored in the [`benchmark/`](benchmark/) directory.

## Methodology

Uzbek is an agglutinative Turkic language in which grammatical and derivational meanings are widely expressed through suffixation. This creates a large number of surface word forms and increases the complexity of token-level linguistic analysis.

UzbekTaggerBERT handles this problem by using a Transformer-based contextual encoder and a token-level POS prediction layer. The package also includes practical preprocessing and alignment mechanisms:

1. **Text normalization**: standardizes common apostrophe variants in Uzbek Latin texts.
2. **Subword tokenization**: uses the Transformer tokenizer associated with the fine-tuned Tahrirchi-BERT model.
3. **Offset alignment**: maps subword-level model predictions back to original word boundaries.
4. **Contextual POS prediction**: assigns POS tags based on surrounding context.

## Use Cases

UzbekTaggerBERT can be used in:

- Uzbek corpus annotation;
- morphological analysis pipelines;
- syntactic analysis pipelines;
- educational NLP systems;
- linguistic feature extraction;
- retrieval-augmented generation systems for Uzbek grammar;
- low-resource NLP research;
- downstream Uzbek text processing applications.

## Repository Structure

The repository is organized as follows:

```text
uzbek-tagger-bert/
├── README.md
├── LICENSE
├── CITATION.cff
├── pyproject.toml
├── repo/
│   └── src/
│       └── uzbek_tagger_bert/
│           ├── __init__.py
│           ├── tagger.py
│           ├── model_loader.py
│           ├── tokenizer_utils.py
│           ├── label_map.py
│           └── cli.py
├── examples/
│   ├── basic_usage.py
│   ├── batch_tagging.py
│   ├── export_conll.py
│   └── cli_usage.py
├── tests/
│   ├── test_import.py
│   ├── test_label_map.py
│   ├── test_tokenizer_utils.py
│   ├── test_output_format.py
│   └── test_model_integration_optional.py
├── benchmark/
│   ├── evaluate.py
│   ├── speed_test.py
│   ├── results.csv
│   └── README.md
└── docs/
    ├── installation.md
    ├── usage.md
    └── tagset.md
```

## Documentation

- Installation guide: [`docs/installation.md`](docs/installation.md)
- Usage guide: [`docs/usage.md`](docs/usage.md)
- POS tagset: [`docs/tagset.md`](docs/tagset.md)
- Benchmark scripts: [`benchmark/README.md`](benchmark/README.md)

## Examples

Run the basic example:

```bash
python examples/basic_usage.py
```

Run batch tagging:

```bash
python examples/batch_tagging.py
```

Export results in CoNLL-like format:

```bash
python examples/export_conll.py
```

## Testing

Install development dependencies:

```bash
pip install pytest scikit-learn
```

Run tests:

```bash
pytest tests
```

Optional real-model integration test:

```bash
RUN_MODEL_TESTS=1 pytest tests/test_model_integration_optional.py
```

## Benchmarking

Evaluate on a CoNLL-like test file:

```bash
python benchmark/evaluate.py --test-file path/to/test.conll --output benchmark/results.csv
```

Run inference-speed test:

```bash
python benchmark/speed_test.py
```

## SoftwareX Article

This repository accompanies the SoftwareX manuscript:

**UzbekTaggerBERT: An Open-Source Python Library for Transformer-Based Part-of-Speech Tagging of the Uzbek Language**

The repository provides the source code, usage examples, documentation, benchmark scripts, and reproducibility materials required for the software publication.

## Citation

If you use this library, model, or dataset in academic research, please cite the repository using the **Cite this repository** button on GitHub.

Related dataset publication:

Sharipov, M., Kuriyozov, E., & Vičič, J. (2026). UzbekPOS: A multi-domain dataset for Uzbek part-of-speech tagging. *Data in Brief*, 112640. https://doi.org/10.1016/j.dib.2026.112640

```bibtex
@article{sharipov2026uzbekpos,
  title={UzbekPOS: A multi-domain dataset for Uzbek part-of-speech tagging},
  author={Sharipov, Maksud and Kuriyozov, Elmurod and Vičič, Jernej},
  journal={Data in Brief},
  pages={112640},
  year={2026},
  publisher={Elsevier},
  doi={10.1016/j.dib.2026.112640}
}
```

## Author

**Maksud Sharipov**

- GitHub: https://github.com/MaksudSharipov
- Hugging Face: https://huggingface.co/MaksudSharipov
- PyPI: https://pypi.org/project/uzbek-tagger-bert/

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

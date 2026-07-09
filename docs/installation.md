# Installation

This document describes how to install **UzbekTaggerBERT**, a Python library for Transformer-based part-of-speech tagging of Uzbek texts.

## Requirements

UzbekTaggerBERT requires:

- Python 3.7 or higher
- PyTorch
- Hugging Face Transformers
- NumPy

The package is designed to work on Windows, Linux, and macOS.

## Install from PyPI

The recommended installation method is through PyPI:

```bash
pip install uzbek-tagger-bert
```

## Verify installation

After installation, verify that the package can be imported:

```python
from uzbek_tagger_bert import UzbekTaggerBERT

tagger = UzbekTaggerBERT()
print("UzbekTaggerBERT loaded successfully.")
```

On the first run, the fine-tuned Tahrirchi-BERT POS tagging model is downloaded from the Hugging Face Hub.

## Install from GitHub

For development or SoftwareX reproducibility, clone the repository:

```bash
git clone https://github.com/MaksudSharipov/uzbek-tagger-bert.git
cd uzbek-tagger-bert
pip install -e .
```

## Optional development dependencies

For testing and benchmarking, install additional packages:

```bash
pip install pytest scikit-learn
```

Then run:

```bash
pytest tests
```

## Command-line interface

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

## Troubleshooting

### The model download is slow

The first run downloads the model from Hugging Face. Subsequent runs use the local cache.

### CUDA is not available

The package automatically uses CPU if CUDA is not available.

### Apostrophe-related tokenization issues

Uzbek Latin texts may contain different apostrophe variants. UzbekTaggerBERT includes text normalization for common apostrophe variants used in Uzbek words such as `O'rgan`, `O‘rgan`, `Oʼrgan`, `Oʻrgan`, `g‘alaba`, and `ma’no`.

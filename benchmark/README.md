# Benchmark

This directory contains evaluation and inference-speed scripts for UzbekTaggerBERT.

## Files

- `evaluate.py` — evaluates the tagger on a CoNLL-like POS test file.
- `speed_test.py` — measures approximate inference speed.
- `results.csv` — stores summary benchmark results for the SoftwareX manuscript.

## Evaluation input format

The expected test file format is:

```text
Bugun	ADV
talabalar	NOUN
keldi	VERB
.	PUNCT

U	PRON
yuz	NOUN
burib	VERB
ketdi	VERB
.	PUNCT
```

Sentences must be separated by blank lines.

## Run evaluation

```bash
python benchmark/evaluate.py --test-file path/to/test.conll --output benchmark/results.csv
```

## Run speed test

```bash
python benchmark/speed_test.py
```

## Current reported results

| Model | Accuracy | Macro F1 | Weighted F1 |
|---|---:|---:|---:|
| UzbekTaggerBERT | 0.9810 | TODO | 0.9811 |

Additional baseline results will be added before SoftwareX submission.

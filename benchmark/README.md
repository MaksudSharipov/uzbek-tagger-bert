# Benchmark

This directory contains evaluation and inference-speed scripts for UzbekTaggerBERT.

## Files

- `evaluate.py` — evaluates the tagger on a CoNLL-like POS test file.
- `speed_test.py` — measures approximate inference speed.
- `results.csv` — stores summary benchmark results for the Software Impacts manuscript.

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

## Model Evaluation Results

Model quality was evaluated using five-fold cross-validation on UzbekPOS. Mean performance across the five validation folds was 0.9784 ± 0.0023 accuracy and 0.9784 ± 0.0023 weighted F1. The best validation fold (Fold 4) achieved 0.9810 accuracy and 0.9811 weighted F1:

| Fold | Accuracy | Weighted F1 |
|------|----------|-------------|
| 1 | 0.9786 | 0.9786 |
| 2 | 0.9764 | 0.9764 |
| 3 | 0.9757 | 0.9757 |
| 4 (Best validation fold) | 0.9810 | 0.9811 |
| 5 | 0.9803 | 0.9803 |
| Mean ± SD | 0.9784 ± 0.0023 | 0.9784 ± 0.0023 |

Additional benchmark information is maintained for the Software Impacts submission.

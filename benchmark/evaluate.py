"""Evaluation script for UzbekTaggerBERT.

This script evaluates UzbekTaggerBERT on a CoNLL-like test file.

Expected input format:
    token<TAB>gold_pos

Sentences are separated by blank lines.

Example:
    Bugun\tADV
    talabalar\tNOUN
    keldi\tVERB
    .\tPUNCT

Run:
    python benchmark/evaluate.py --test-file path/to/test.conll

Optional:
    python benchmark/evaluate.py --test-file path/to/test.conll --output benchmark/results.csv
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import List, Tuple

from sklearn.metrics import accuracy_score, classification_report, f1_score

from uzbek_tagger_bert import UzbekTaggerBERT


def read_conll(path: Path) -> List[Tuple[List[str], List[str]]]:
    """Read CoNLL-like token/POS sentences."""
    sentences = []
    tokens = []
    labels = []

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            if tokens:
                sentences.append((tokens, labels))
                tokens = []
                labels = []
            continue

        parts = line.split()
        if len(parts) < 2:
            continue

        token = parts[0]
        label = parts[-1]
        tokens.append(token)
        labels.append(label)

    if tokens:
        sentences.append((tokens, labels))

    return sentences


def evaluate(test_file: Path, output: Path | None = None) -> None:
    tagger = UzbekTaggerBERT()
    data = read_conll(test_file)

    y_true = []
    y_pred = []

    for tokens, gold_labels in data:
        sentence = " ".join(tokens)
        predicted = tagger.tag_text(sentence)
        pred_labels = [item["pos"] for item in predicted]

        # Align by minimum length to avoid crashes caused by punctuation/tokenization differences.
        n = min(len(gold_labels), len(pred_labels))
        y_true.extend(gold_labels[:n])
        y_pred.extend(pred_labels[:n])

    acc = accuracy_score(y_true, y_pred)
    macro = f1_score(y_true, y_pred, average="macro", zero_division=0)
    weighted = f1_score(y_true, y_pred, average="weighted", zero_division=0)

    print("Evaluation results")
    print("==================")
    print(f"Tokens: {len(y_true)}")
    print(f"Accuracy: {acc:.4f}")
    print(f"Macro F1: {macro:.4f}")
    print(f"Weighted F1: {weighted:.4f}")
    print()
    print(classification_report(y_true, y_pred, zero_division=0))

    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["metric", "score"])
            writer.writerow(["accuracy", f"{acc:.4f}"])
            writer.writerow(["macro_f1", f"{macro:.4f}"])
            writer.writerow(["weighted_f1", f"{weighted:.4f}"])
        print(f"Saved summary to: {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate UzbekTaggerBERT on a CoNLL-like POS dataset.")
    parser.add_argument("--test-file", required=True, type=Path, help="Path to CoNLL-like test file.")
    parser.add_argument("--output", type=Path, default=Path("benchmark/results.csv"), help="Output CSV path.")
    args = parser.parse_args()

    evaluate(args.test_file, args.output)


if __name__ == "__main__":
    main()

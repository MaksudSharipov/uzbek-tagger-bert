"""Inference-speed benchmark for UzbekTaggerBERT.

Run:
    python benchmark/speed_test.py

The script reports approximate runtime and tokens/second on the current machine.
"""

from __future__ import annotations

import time

from uzbek_tagger_bert import UzbekTaggerBERT


SENTENCES = [
    "Bugun talabalar yangi mavzuni o‘rgandilar.",
    "U yuz burib ketdi va yuz soat ishladi.",
    "Alisher sariq olma olib menga qizil olma olmading dedi.",
    "O‘rgan va izlan.",
    "Bozordan olma olib kel.",
] * 20


def main() -> None:
    tagger = UzbekTaggerBERT()

    start = time.perf_counter()
    results = tagger.tag_batch(SENTENCES)
    elapsed = time.perf_counter() - start

    token_count = sum(len(sentence_result) for sentence_result in results)
    sent_count = len(SENTENCES)
    tokens_per_second = token_count / elapsed if elapsed > 0 else 0.0
    sentences_per_second = sent_count / elapsed if elapsed > 0 else 0.0

    print("Inference speed benchmark")
    print("=========================")
    print(f"Sentences: {sent_count}")
    print(f"Tokens: {token_count}")
    print(f"Time: {elapsed:.4f} seconds")
    print(f"Sentences/sec: {sentences_per_second:.2f}")
    print(f"Tokens/sec: {tokens_per_second:.2f}")


if __name__ == "__main__":
    main()

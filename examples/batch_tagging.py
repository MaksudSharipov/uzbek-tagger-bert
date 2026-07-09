"""Batch tagging example for UzbekTaggerBERT.

Run:
    python examples/batch_tagging.py
"""

from uzbek_tagger_bert import UzbekTaggerBERT


def main() -> None:
    tagger = UzbekTaggerBERT()

    sentences = [
        "Bugun talabalar yangi mavzuni o‘rgandilar.",
        "Bozordan olma olib kel.",
        "O‘zbekiston mustaqil davlatdir.",
        "U yuz burib ketdi va yuz soat ishladi.",
    ]

    results = tagger.tag_batch(sentences)

    for sentence, tagged_tokens in zip(sentences, results):
        print("Sentence:", sentence)
        print(tagger.to_slash(tagged_tokens))
        print("-" * 60)


if __name__ == "__main__":
    main()

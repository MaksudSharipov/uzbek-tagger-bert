"""Basic usage example for UzbekTaggerBERT.

Run:
    python examples/basic_usage.py
"""

from uzbek_tagger_bert import UzbekTaggerBERT


def main() -> None:
    tagger = UzbekTaggerBERT()

    text = (
        "U yuz burib ketdi va yuz soat ishladi. "
        "Alisher sariq olma olib menga qizil olma olmading dedi."
    )

    result = tagger(text)
    print(result)


if __name__ == "__main__":
    main()

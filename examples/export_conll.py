"""Export POS tagging results in CoNLL-like format.

Run:
    python examples/export_conll.py
"""

from pathlib import Path

from uzbek_tagger_bert import UzbekTaggerBERT


def main() -> None:
    tagger = UzbekTaggerBERT()

    text = "Bugun talabalar yangi mavzuni o‘rgandilar."
    tagged_tokens = tagger.tag_text(text)

    conll_output = tagger.to_conll(tagged_tokens)

    output_path = Path("tagged_output.conll")
    output_path.write_text(conll_output, encoding="utf-8")

    print(conll_output)
    print(f"\nSaved to: {output_path.resolve()}")


if __name__ == "__main__":
    main()

"""Command-line interface for UzbekTaggerBERT."""

from __future__ import annotations

import argparse
import json

from .tagger import UzbekTaggerBERT


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Transformer-based POS tagging for Uzbek text."
    )
    parser.add_argument(
        "text",
        type=str,
        help="Uzbek text to tag.",
    )
    parser.add_argument(
        "--format",
        choices=["slash", "json", "conll"],
        default="slash",
        help="Output format. Default: slash.",
    )
    parser.add_argument(
        "--model",
        default="MaksudSharipov/Uzbek-POS-Tagger-TahrirchiBERT",
        help="Hugging Face model name or local model path.",
    )
    parser.add_argument(
        "--device",
        default="auto",
        help="Device: auto, cpu, cuda, etc.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    tagger = UzbekTaggerBERT(model_name=args.model, device=args.device)
    output = tagger(args.text, output_format=args.format)

    if args.format == "json":
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(output)


if __name__ == "__main__":
    main()

import sys
import argparse
from uzbek_tagger_bert.tagger import UzbekTaggerBERT

def main():
    parser = argparse.ArgumentParser(
        description="UzbekTaggerBERT Command Line Tool: High-Accuracy POS Tagger for Uzbek."
    )
    parser.add_argument("text", type=str, nargs="?", help="Text to tag. If not provided, reads from standard input.")
    args = parser.parse_args()

    # Initialize the tagger
    tagger = UzbekTaggerBERT()

    if args.text:
        # Tag argument text
        print(tagger(args.text))
    else:
        # Read from standard input (useful for piping in terminal)
        if not sys.stdin.isatty():
            text = sys.stdin.read().strip()
            if text:
                print(tagger(text))
            else:
                parser.print_help()
        else:
            parser.print_help()

if __name__ == "__main__":
    main()

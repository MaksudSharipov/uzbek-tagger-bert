"""UzbekTaggerBERT: Transformer-based POS tagging for Uzbek."""

from .tagger import UzbekTaggerBERT, UzbekPOSTagger
from .label_map import POS_LABELS

__version__ = "0.1.2"

__all__ = ["UzbekTaggerBERT", "UzbekPOSTagger", "POS_LABELS"]

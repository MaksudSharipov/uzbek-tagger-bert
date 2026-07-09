"""UzbekTaggerBERT: Transformer-based POS tagging for Uzbek."""

from .tagger import UzbekTaggerBERT, UzbekPOSTagger
from .label_map import POS_LABELS

__version__ = "1.0.0"

__all__ = ["UzbekTaggerBERT", "UzbekPOSTagger", "POS_LABELS"]

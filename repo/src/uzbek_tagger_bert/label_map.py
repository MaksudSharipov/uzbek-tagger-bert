# Mapping of part-of-speech (POS) tags used by the Uzbek POS tagger.
# These correspond to Universal Dependencies (UD) POS tags.

UD_TAG_MAP = {
    "NOUN": "Noun (Ot)",
    "VERB": "Verb (Fe'l)",
    "ADJ": "Adjective (Sifat)",
    "PRON": "Pronoun (Olmosh)",
    "NUM": "Numeral (Son)",
    "ADV": "Adverb (Ravish)",
    "CONJ": "Conjunction (Bog'lovchi)",
    "CCONJ": "Coordinating Conjunction (Teng bog'lovchi)",
    "SCONJ": "Subordinating Conjunction (Ergashtiruvchi bog'lovchi)",
    "ADP": "Adposition (Ko'makchi)",
    "PART": "Particle (Yuklama)",
    "INTJ": "Interjection (Undov)",
    "PROPN": "Proper Noun (Atoqli ot)",
    "PUNCT": "Punctuation (Tinish belgisi)",
    "SYM": "Symbol (Belgi)",
    "X": "Other (Boshqa)"
}

def get_tag_description(tag: str) -> str:
    """
    Returns the English and Uzbek description for a given UD POS tag.
    """
    return UD_TAG_MAP.get(tag, "Unknown Category")

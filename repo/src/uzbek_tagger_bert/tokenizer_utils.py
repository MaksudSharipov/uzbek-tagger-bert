import re

def normalize_text(text: str) -> str:
    """
    Standardizes apostrophes, pads punctuation, and normalizes whitespaces
    specifically for the Uzbek language to ensure optimal tokenization.
    """
    # Normalize various types of curly quotes/apostrophes used in Uzbek Latin to a straight single quote
    text = re.sub(r"[‘'’`´ʻʼ\"“”]", "'", text)
    # Join split parts around apostrophes (e.g., O'zbekiston)
    text = re.sub(r"([a-zA-Z])\s+'\s*([a-zA-Z])", r"\1'\2", text)
    # Pad punctuation with spaces
    text = re.sub(r'([.,!?();:])', r' \1 ', text)
    # Standardize spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def align_tokens_to_words(clean_text: str, pipeline_results: list) -> list:
    """
    Uses an overlap-based offset mapping algorithm to align subword token
    predictions back to the original word boundaries, resolving the UNKNOWN tag problem.
    """
    tagged_words = []
    
    # Identify original, whitespace-separated words and their start/end offsets
    for match in re.finditer(r'\S+', clean_text):
        word_start = match.start()
        word_end = match.end()
        word_text = match.group()

        word_tag = "UNKNOWN"

        # Check for overlaps with predicted tokens
        for entity in pipeline_results:
            # Overlap checking: if the entity token overlaps with the word boundary
            if entity['start'] < word_end and entity['end'] > word_start:
                word_tag = entity.get('entity_group', entity.get('entity', 'UNKNOWN'))
                break

        tagged_words.append((word_text, word_tag))
        
    return tagged_words

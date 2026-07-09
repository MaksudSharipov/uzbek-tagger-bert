from .model_loader import load_pos_pipeline
from .tokenizer_utils import normalize_text, align_tokens_to_words

class UzbekTaggerBERT:
    def __init__(self, model_id="MaksudSharipov/Uzbek-POS-Tagger-TahrirchiBERT"):
        # Load the Hugging Face token classification pipeline
        self.nlp = load_pos_pipeline(model_id)

    def _normalize_text(self, text: str) -> str:
        # Kept for backward compatibility in case external projects call this internal method
        return normalize_text(text)

    def __call__(self, text: str) -> str:
        if not self.nlp:
            return "Error: Model is not loaded properly."

        # 1. Normalize text
        clean_text = normalize_text(text)
        
        # 2. Get token predictions from pipeline
        results = self.nlp(clean_text)
        
        # 3. Align tokens to original words
        aligned_pairs = align_tokens_to_words(clean_text, results)

        # 4. Format output as word/TAG
        tagged_words = [f"{word}/{tag}" for word, tag in aligned_pairs]
        return " ".join(tagged_words)


# ==========================================
# TEST RUN
# ==========================================
if __name__ == "__main__":
    tagger = UzbekTaggerBERT()
    qiyin_matn = "U sendan yuz o'girdi va yuz marta kechirim so'ramadi. Bozordan olma olma desam ham olma olibdi."

    natija = tagger(qiyin_matn)
    print(f"\nNatija: {natija}\n")
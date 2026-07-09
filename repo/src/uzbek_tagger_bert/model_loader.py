import warnings
from transformers import pipeline

warnings.filterwarnings("ignore")

def load_pos_pipeline(model_id: str = "MaksudSharipov/Uzbek-POS-Tagger-TahrirchiBERT"):
    """
    Downloads and loads the token classification pipeline from Hugging Face.
    """
    print("Loading the model from Hugging Face. Please wait...")
    try:
        nlp = pipeline(
            "token-classification",
            model=model_id,
            tokenizer=model_id,
            aggregation_strategy="simple",
            ignore_labels=[]  # Prevents filtering of label classes
        )
        print("Success: Model is ready to use!\n")
        return nlp
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

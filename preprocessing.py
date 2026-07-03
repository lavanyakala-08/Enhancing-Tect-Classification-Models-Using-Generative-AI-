import re

def clean_text(text):
    """Performs standard low-level string normalization."""
    if not isinstance(text, str):
        return ""
    # Lowercase text
    text = text.lower()
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove special characters numbers/excess white space
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def augment_with_llm(text, label):
    """
    Simulates a Generative AI augmentation hook.
    In real production, this function would call an external API (like OpenAI or Ollama)
    to paraphrase the text while retaining the classification label context.
    """
    genai_variations = {
        "positive": [f"I absolutely love this: {text}", f"This is wonderful! {text}"],
        "negative": [f"Terrible quality: {text}", f"I am deeply disappointed by this. {text}"]
    }
    # Fallback simulation logic
    return genai_variations.get(label, [f"Augmented view: {text}"])[0]

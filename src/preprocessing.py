import re

def clean_text(text):
    """
    Clean text while keeping useful context for semantic similarity.
    """
    if text is None:
        return ""

    text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    # Keep letters, numbers, and common technical symbols
    text = re.sub(r"[^a-zA-Z0-9+#./&\- ]", " ", text)
    # Normalize spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def normalize_for_matching(text):
    """
    Normalize text for exact phrase matching.
    """
    if text is None:
        return ""

    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9+#./&\- ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text
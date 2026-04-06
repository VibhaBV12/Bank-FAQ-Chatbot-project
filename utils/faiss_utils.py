# faiss_utils.py

import os
from constants import FAQ_PATH

# ---------------- Load FAQ ----------------
def load_index():
    """
    Load FAQ file as a list of lines.
    """
    if not os.path.exists(FAQ_PATH):
        return []

    with open(FAQ_PATH, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    return lines


# ---------------- Clean Text ----------------
def preprocess(text):
    """
    Lowercase and remove simple punctuation.
    """
    return text.lower().replace("?", "").replace(".", "").replace(",", "")


# ---------------- Query FAQ ----------------
def query(db, user_query):
    """
    Improved FAQ search using word matching with threshold.
    """
    user_query = preprocess(user_query)
    query_words = set(user_query.split())

    best_match = None
    best_score = 0

    for idx, line in enumerate(db):
        if line.startswith("Q:"):
            question = preprocess(line[2:].strip())
            question_words = set(question.split())

            # Calculate similarity score
            common_words = query_words.intersection(question_words)
            score = len(common_words) / max(len(query_words), 1)

            # Track best match
            if score > best_score:
                best_score = score
                if idx + 1 < len(db) and db[idx + 1].startswith("A:"):
                    best_match = db[idx + 1][2:].strip()

    # ---------------- Threshold Check ----------------
    if best_score >= 0.5:   # You can tune this (0.4–0.7)
        return best_match
    else:
        return "Sorry, I don't have information about that. Please contact the bank."


# ---------------- Create index ----------------
def create_index():
    """
    Ensures FAQ file exists (for admin button compatibility).
    """
    if not os.path.exists(FAQ_PATH):
        os.makedirs(os.path.dirname(FAQ_PATH), exist_ok=True)
        with open(FAQ_PATH, "w", encoding="utf-8") as f:
            f.write("")
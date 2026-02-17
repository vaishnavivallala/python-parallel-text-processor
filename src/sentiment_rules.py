import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES_DIR = os.path.join(BASE_DIR, "rules")

POSITIVE_WORDS_FILE = os.path.join(RULES_DIR, "positive_words.txt")
NEGATIVE_WORDS_FILE = os.path.join(RULES_DIR, "negative_words.txt")


def load_words(file_path):
    words = set()
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip().lower()
            if word:
                words.add(word)
    return words


positive_words = load_words(POSITIVE_WORDS_FILE)
negative_words = load_words(NEGATIVE_WORDS_FILE)


def analyze_sentiment(text):
    score = 0
    words = text.lower().split()

    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    else:
        label = "neutral"

    return score, label

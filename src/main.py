import os
from sentiment_rules import analyze_sentiment


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_REVIEWS_PATH = os.path.join(BASE_DIR, "data", "raw_reviews")

def load_reviews():
    reviews = []

    for filename in os.listdir(RAW_REVIEWS_PATH):
        if filename.endswith(".txt"):
            file_path = os.path.join(RAW_REVIEWS_PATH, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        reviews.append(line)

    return reviews


if __name__ == "__main__":
    all_reviews = load_reviews()

    print("\nSentiment Analysis Results:\n")

    for review in all_reviews:
        score, label = analyze_sentiment(review)
        print(f"Review: {review}")
        print(f"Score: {score} | Sentiment: {label}")
        print("-" * 50)

import os
import sqlite3
from sentiment_rules import analyze_sentiment


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_REVIEWS_PATH = os.path.join(BASE_DIR, "data", "raw_reviews")
DB_PATH = os.path.join(BASE_DIR, "database", "reviews.db")

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


def insert_into_db(reviews):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for review in reviews:
        score, label = analyze_sentiment(review)
        cursor.execute(
            "INSERT INTO reviews (review_text, sentiment_score, sentiment_label) VALUES (?, ?, ?)",
            (review, score, label)
        )

    conn.commit()
    conn.close()
    print("Reviews inserted into database successfully.")


if __name__ == "__main__":
    reviews = load_reviews()
    insert_into_db(reviews)

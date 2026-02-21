import os
import sqlite3
import pandas as pd
from datetime import datetime
from sentiment_rules import analyze_sentiment

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSV_PATH = os.path.join(
    BASE_DIR, "data", "kaggle_amazon", "amazon_product_reviews.csv"
)

DB_PATH = os.path.join(
    BASE_DIR, "database", "reviews.db"
)


def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sentiment_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review_text TEXT NOT NULL,
            sentiment_label TEXT NOT NULL,
            sentiment_score INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
    """)


def store_results():
    # ---- Read CSV safely ----
    try:
        df = pd.read_csv(CSV_PATH)
    except Exception as e:
        print("❌ Error reading CSV file:", e)
        return

    # ---- Connect DB safely ----
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print("❌ Database connection error:", e)
        return

    # ---- Create table ----
    try:
        create_table(cursor)
    except sqlite3.Error as e:
        print("❌ Error creating table:", e)
        conn.close()
        return

    inserted = 0

    # ---- Insert data ----
    for _, row in df.iterrows():
        try:
            review_text = row["Text"]
            sentiment_label, sentiment_score = analyze_sentiment(review_text)
            timestamp = datetime.now().isoformat()

            cursor.execute("""
                INSERT INTO sentiment_results
                (review_text, sentiment_label, sentiment_score, created_at)
                VALUES (?, ?, ?, ?)
            """, (review_text, sentiment_label, sentiment_score, timestamp))

            inserted += 1

        except Exception:
            # Skip bad rows silently
            continue

    conn.commit()
    conn.close()

    print(f"✅ Stored {inserted} reviews into SQLite database.")


if __name__ == "__main__":
    store_results()
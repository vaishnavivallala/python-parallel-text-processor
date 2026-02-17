import sqlite3
import os


DB_PATH = os.path.join("database", "reviews.db")

def create_database():
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review_text TEXT NOT NULL,
            sentiment_score INTEGER,
            sentiment_label TEXT
        )
    """)

    
    conn.commit()
    conn.close()

    print("Database and table created successfully.")

if __name__ == "__main__":
    create_database()

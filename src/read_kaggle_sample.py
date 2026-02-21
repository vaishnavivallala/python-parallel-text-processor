import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(
    BASE_DIR,
    "data",
    "kaggle_amazon",
    "amazon_product_reviews.csv"
)

def read_sample():
    print("Reading file from:")
    print(CSV_PATH)

    df = pd.read_csv(CSV_PATH, nrows=5)
    print("\nColumns:")
    print(df.columns)

    print("\nSample data:")
    print(df)

if __name__ == "__main__":
    read_sample()
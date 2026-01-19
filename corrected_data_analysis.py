import pandas as pd
import os

# List of files - Using raw strings to avoid escape sequence warnings
files = [
    r"Data\olist_orders_dataset.csv",
    r"Data\olist_products_dataset.csv",
    r"Data\olist_sellers_dataset.csv",
    r"Data\product_category_name_translation.csv",
    r"Data\olist_geolocation_dataset.csv",
    r"Data\olist_order_items_dataset.csv",
    r"Data\olist_order_payments_dataset.csv",
    r"Data\olist_order_reviews_dataset.csv",
    r"Data\olist_customers_dataset.csv"
]

data = {}
for file in files:
    try:
        df = pd.read_csv(file)
        data[file] = df
        print(f"--- {file} ---")
        print(df.info())
        print(df.head())
        print("\n")
    except Exception as e:
        print(f"Error reading {file}: {e}")

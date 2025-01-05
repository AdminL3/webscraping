import json
import os
import sqlite3
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        product_url TEXT,
        image_url TEXT,
        rating_value REAL,
        review_count INTEGER,
        price REAL,
        availability TEXT
    )
    """
)
for root, dirs, files in os.walk("data"):
    for file in files:
        if file.endswith(".json"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                json_data = json.load(f)

            product_name = json_data.get("name")
            product_url = json_data.get("url")
            image_url = json_data.get("image")
            rating_value = json_data.get(
                "aggregateRating", {}).get("ratingValue")
            review_count = json_data.get(
                "aggregateRating", {}).get("reviewCount")
            price = json_data.get("offers", {}).get("price")
            availability = json_data.get("offers", {}).get("availability")
            availability = availability.split("/")[-1]

            cursor.execute(
                """
                INSERT INTO products (
                    product_name,
                    product_url,
                    image_url,
                    rating_value,
                    review_count,
                    price,
                    availability
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    product_name,
                    product_url,
                    image_url,
                    rating_value,
                    review_count,
                    price,
                    availability
                )
            )

conn.commit()
conn.close()

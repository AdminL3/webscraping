import json
import os
import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price FLOAT
    )''')

for i in os.listdir('data'):
    with open(f'data/{i}', 'r') as file:
        data = json.load(file)

    results = data.get("results", [])

    for result in results:
        name = json.dumps(result["brand"])
        cursor.execute('''
            INSERT INTO data (name, price)
            VALUES (?, ?)''',
                       (name.strip('"'), result["price"]))
    conn.commit()
conn.close()

import json
import os
import sqlite3

conn = sqlite3.connect('Networking/data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price FLOAT
    )''')

for i in os.listdir('Networking/data'):
    with open(f'Networking/data/{i}', 'r') as file:
        data = json.load(file)

    results = data.get("results", [])

    for result in results:
        try:
            name = json.dumps(result["brand"])
        except:
            print(result)
            print("Brand not found")
        cursor.execute('''
            INSERT INTO data (name, price)
            VALUES (?, ?)''',
                       (name.strip('"'), result["price"]))
    conn.commit()
conn.close()

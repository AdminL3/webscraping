# Webscraping Preset

---

## 1. Requirements

### 1. Venv

- Create a virtual environment with

```
python -m venv .venv
```

- Activate the virtual environment with

```
source .venv/bin/activate
```

### 2. Install Requirements

- Install the requirements with

```
pip install -r requirements.txt
```

---

## 2. Networking

### 1. Parse URL

- Enter Url into `Parse_url.py`
- Run `Parse_url.py`
- Copy the Output from `URL.txt` into `Get_Data.py`

### 2. Get Data

- Run `Get_Data.py`
- Use Requests to get the json data
- Saving it into the text file in `data` folder

### 3. Parse Data

- Run `Parse_Data.py`
- Parse the data and save it into the sqlite database `data.db`
- If you don't know exactly what you need to get, [jsoneditoronline.org](jsoneditoronline.org) gives a good overview

---

## 3. Selenium

Code to copy:

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-search-engine-choice-screen")
options.add_experimental_option("detach", True)
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


driver.get('https://www.google.de/')
print(driver.title)

time.sleep(2)

```

---

## 4. Beautifulsoup

Code to copy:

```python
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('title').get_text()
    print('Title of the page:', title)

    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)

```

---

## 5. Database

### 1. Import sqlite3

```python
import sqlite3
```

### 2. Create Database

```python
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price FLOAT
    )''')
```

### 3. Insert Data

```python
cursor.execute('''
            INSERT INTO data (name, price)
            VALUES (?, ?)''',
            (name, price))
    conn.commit()
conn.close()
```

### 4. Drop Database

```python
cursor.execute("DROP TABLE IF EXISTS data")
conn.commit()
```

---

## Playwright

### 1. Install Playwright

```bash
pip install playwright
```

### 2. Run Playwright

```python
def run(playwright: Playwright):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    # code here

with sync_playwright() as p:
    run(p)
```

---

## Playwright Codegen

### 1. Install Playwright Codegen

```bash
pip install playwright
```

### 2. Run Playwright Codegen

```bash
playwright codegen https://example.com
```

### 3. Copy from Codegen

Base Structure

```python
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Code here

    browser.close()


with sync_playwright() as playwright:
    run(playwright)
```

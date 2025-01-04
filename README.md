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

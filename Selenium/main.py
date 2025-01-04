import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-search-engine-choice-screen")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


driver.get('https://www.google.de/')
print(driver.title)

time.sleep(2)

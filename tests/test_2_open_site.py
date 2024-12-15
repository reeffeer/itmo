from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")

value = 'header > a > svg'
try:
    icon = driver.find_element(By.CSS_SELECTOR, value)
    print('Element is found')
except NoSuchElementException:
    print('Element\'s not found')

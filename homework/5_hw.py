from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def find_elements():
    driver.get(" https://www.saucedemo.com/")
    try:
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.XPATH, "//input[@type='submit']")

        if username and password and login_button:
            print("Элементы найдены")
        else:
            print("Not found")
    except NoSuchElementException:
        print("Элементы не найдены")


find_elements()

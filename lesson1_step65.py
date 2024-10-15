from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep

secret_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = "http://suninjuly.github.io/find_link_text"
lst = ["Ivan", "Petrov", "Smolensk", "Russia"]

try:
    browser = webdriver.Chrome()
    browser.get(link)

    lin_1 = browser.find_element(By.LINK_TEXT, secret_link)
    lin_1.click()
    
    for i, v in enumerate(lst, 1):
        temp = browser.find_element(By.CSS_SELECTOR, f".form-group:nth-child({i}) input")
        temp.send_keys(v)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    sleep(25)
    browser.quit()
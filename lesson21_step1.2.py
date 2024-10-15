from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "https://test.office.credit.club/applications"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element(By.CSS_SELECTOR, "#username")
    input1.send_keys("a.farlenkov")
    input1 = browser.find_element(By.CSS_SELECTOR, "#password")
    input1.send_keys("12345678")

    button = browser.find_element(By.CSS_SELECTOR, "#kc-login")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
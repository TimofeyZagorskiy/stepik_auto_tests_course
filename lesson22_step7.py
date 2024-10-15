from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)")
    input1.send_keys("Иван")
    
    input1 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
    input1.send_keys("Петров")

    input1 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(6)")
    input1.send_keys("мылов")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    
    
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    #print("x=", x)
    y = calc(x)
    #print("y=", y)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    
    browser.execute_script("window.scrollBy(0, 100);")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()

    print("Тест успешно завершен. 20 сек на закрытие браузера...")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
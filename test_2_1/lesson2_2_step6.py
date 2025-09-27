from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    print(y)


    field_answer = browser.find_element(By.ID, 'answer')
    print(field_answer)
    field_answer.send_keys(y)

    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()

    option2 = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("window.scrollBy(0,100);")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("window.scrollBy(0,100);")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
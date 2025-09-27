from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(nums):
        return math.fsum(nums)

    n1_element = browser.find_element(By.ID, "num1")
    n2_element = browser.find_element(By.ID, "num2")
    num1 = int(n1_element.text)
    num2 = int(n2_element.text)
    y_int = int(calc([num1, num2]))
    y = str(y_int)

    #print(y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
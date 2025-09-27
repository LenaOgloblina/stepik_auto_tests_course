from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser,  12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    #print(y)

    field_answer = browser.find_element(By.ID, 'answer')
    #print(field_answer)
    field_answer.send_keys(y)

    button_sub = browser.find_element(By.ID, "solve")
    browser.execute_script("window.scrollBy(0,100);")
    button_sub.click()

finally:
    time.sleep(5)
    browser.quit()
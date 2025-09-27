from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)
try:

    first_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder$="name"]')
    first_name.send_keys('Anuka')
    last_name=browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name'")
    last_name.send_keys('Anunaki')
    email=browser.find_element(By.CSS_SELECTOR, 'input[placeholder$="email"]')
    email.send_keys('chunim@gmail.com')
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
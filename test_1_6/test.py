from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("mail@test.com")

    # Отправляем форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(5)  # просто подождать для наглядности (можно убрать)

finally:
    browser.quit()

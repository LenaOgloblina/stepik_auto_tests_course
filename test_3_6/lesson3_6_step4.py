from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def stepik_registration():
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    browser.find_element(By.ID, "ember484").click()

    field_email = browser.find_element(By.ID, "id_login_email")
    field_email.send_keys("eleno4ka.k@gmail.com")

    field_password = browser.find_element(By.ID, "id_login_password")
    field_password.send_keys("lendokolendo")

    button_sign = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_sign.click()

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
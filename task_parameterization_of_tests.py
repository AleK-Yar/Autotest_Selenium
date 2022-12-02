import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "https://stepik.org/lesson/236895/step/1"
name = "alek-yar@hotmail.com"
password = "XaSx&6e\\)aL;i?]"

links = ("https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def autorization_login_link(browser, link, name, password):
    browser.get(link)
    browser.implicitly_wait(5)
   # WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "login_form"))
    browser.find_element(By.ID, "id_login_email").send_keys(name)
    browser.find_element(By.ID, "id_login_password").send_keys(password)
    browser.find_element(By.ID, ".button_with-loader ").submit()

# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")


if __name__ == "__main__":
    autorization_login_link(browser, link, name, password)

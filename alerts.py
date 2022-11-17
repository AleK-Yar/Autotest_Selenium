from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import math


def calc(x):
    return str(math. log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(link)

    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    valuex = browser.find_element(By.ID, "input_value")
    x = valuex.text
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answer.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    quiz = browser.switch_to.alert
    text = quiz.text.split(': ')[-1]
    quiz.accept()
    print(text)

finally:
    browser.quit()
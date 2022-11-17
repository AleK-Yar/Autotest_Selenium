from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math. log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"').submit()
    time.sleep(1)
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
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

    time.sleep(10)
    browser.quit()

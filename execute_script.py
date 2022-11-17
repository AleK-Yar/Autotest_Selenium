from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def func(x):
    return math.log(abs(12 * math.sin(int(x))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(func(x))
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, 'input#robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').submit()

    time.sleep(20)

finally:
    browser.quit()

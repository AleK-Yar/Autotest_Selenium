from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, 'treasure')
    value_treasure = treasure.get_attribute('valuex')

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(value_treasure))

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

    time.sleep(15)
finally:
    browser.quit()

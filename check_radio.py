from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math. log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(3)

    valuex = browser.find_element(By.ID, "treasure")
    x = valuex.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answer.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()



    time.sleep(30)

finally:
    browser.quit()

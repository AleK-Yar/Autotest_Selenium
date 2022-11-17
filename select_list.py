from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    num = str(int(num1) + int(num2))
    browser.find_element(By.TAG_NAME, 'select').click()
    browser.find_element(By.CSS_SELECTOR, f'[value="{num}"]').click()
    # select = Select(browser.find_element(By.TAG_NAME, 'select'))
    # select.select_by_value(num)
    browser.find_element(By.TAG_NAME, 'button').click()

    time.sleep(15)

finally:
    browser.quit()


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    browser.find_element(By.NAME, 'lastname').send_keys('Petrov')
    browser.find_element(By.NAME, 'email').send_keys('email@email.el')
    element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').submit()

finally:
    time.sleep(15)

    browser.quit()

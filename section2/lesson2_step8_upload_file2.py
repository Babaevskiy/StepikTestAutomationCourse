import os
import time
from selenium import webdriver


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element_by_name('firstname').send_keys('firstname')
    browser.find_element_by_name('lastname').send_keys('lastname')
    browser.find_element_by_name('email').send_keys('email')
    current_dir = os.path.abspath(os.path.dirname('__file__'))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element_by_name('file').send_keys(file_path)
    browser.find_element_by_class_name('btn').click()
finally:
    time.sleep(10)
    browser.quit()
from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_xpath_form')
    input1 = browser.find_element_by_name('first_name')
    input1.send_keys('Ivan')
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys('Sidorov')
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys('Smolensk')
    input4 = browser.find_element_by_id('country')
    input4.send_keys('Russia')
    # button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
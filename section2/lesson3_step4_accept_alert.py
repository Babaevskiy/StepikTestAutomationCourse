from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element_by_class_name('btn').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_class_name('btn').click()
    alert = browser.switch_to.alert
    answer = alert.text.split(': ')[-1]
    alert.accept()
    print(browser.window_handles)
    print(answer)
finally:
    time.sleep(4)
    browser.quit()

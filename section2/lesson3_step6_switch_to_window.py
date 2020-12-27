from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element_by_class_name('btn').click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_class_name('btn').click()
    alert = browser.switch_to.alert
    answer = alert.text.split(': ')[-1]
    print(answer)
    alert.accept()
finally:
    time.sleep(5)
    browser.quit()
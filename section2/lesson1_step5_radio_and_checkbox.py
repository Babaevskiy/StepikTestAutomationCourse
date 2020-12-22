from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    x = calc(browser.find_element_by_id("input_value").text)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(x)
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()
    robot_radio = browser.find_element_by_id("robotsRule")
    robot_radio.click()
    button = browser.find_element_by_class_name("btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()

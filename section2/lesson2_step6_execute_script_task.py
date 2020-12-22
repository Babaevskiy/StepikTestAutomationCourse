from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x = browser.find_element_by_id("input_value").text
    field = browser.find_element_by_id("answer")
    field.send_keys(calc(x))
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()
    robot_radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    robot_radio.click()
    button = browser.find_element_by_class_name("btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
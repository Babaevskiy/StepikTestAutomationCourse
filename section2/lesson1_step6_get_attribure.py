from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox_value = robot_checkbox.get_attribute("checked")
    print("Robot checkbox value:", robot_checkbox_value)
    assert robot_checkbox_value is None

    people_radio = browser.find_element_by_id("peopleRule")
    people_radio_value = people_radio.get_attribute("checked")
    print("People radio value:", people_radio_value)
    assert people_radio_value is not None

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_radio_value = robots_radio.get_attribute("checked")
    print("Robots radio value:", robots_radio_value)
    assert robots_radio_value is None

    button = browser.find_element_by_class_name("btn")
    button_value = button.get_attribute("disabled")
    print("Button value before 10 sec:", button_value)
    assert button_value is None

    time.sleep(10)

    button_value = button.get_attribute("disabled")
    print("Button value after 10 sec:", button_value)
    assert button_value is not None

finally:
    time.sleep(2)
    browser.quit()

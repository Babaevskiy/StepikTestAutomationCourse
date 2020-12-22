from selenium import webdriver
from time import sleep


try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    sleep(4)
    browser.quit()

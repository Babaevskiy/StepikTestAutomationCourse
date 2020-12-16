from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name_field = browser.find_element_by_css_selector(".first_block .first")
    first_name_field.send_keys("value")
    last_name_field = browser.find_element_by_css_selector(".first_block .second")
    last_name_field.send_keys("value")
    email_field = browser.find_element_by_css_selector(".first_block .third")
    email_field.send_keys("value")
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    time.sleep(1)
    welcome_text = browser.find_element_by_tag_name("h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(3)
    browser.quit()

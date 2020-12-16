from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_css_selector(".first_block input")
    for element in elements:
        element.send_keys("value")
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    time.sleep(1)
    welcome_text = browser.find_element_by_tag_name("h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(3)
    browser.quit()
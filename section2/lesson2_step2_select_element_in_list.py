from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text("97")
finally:
    time.sleep(3)
    browser.quit()
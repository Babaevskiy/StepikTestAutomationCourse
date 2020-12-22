from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    summa = str(int(num1) + int(num2))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(summa)
    button = browser.find_element_by_class_name("btn")
    button.click()
finally:
    sleep(10)
    browser.quit()
from selenium import webdriver
from time import sleep


try:
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing'; alert('Robot framework');")
finally:
    sleep(4)
    browser.quit()
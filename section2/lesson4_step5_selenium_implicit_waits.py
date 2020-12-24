from selenium import webdriver


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")
    browser.find_element_by_id("verify").click()
    assert browser.find_element_by_id("verify_message").text == "Verification was successful!"
finally:
    browser.quit()


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")
    browser.find_element_by_id("button")
finally:
    browser.quit()
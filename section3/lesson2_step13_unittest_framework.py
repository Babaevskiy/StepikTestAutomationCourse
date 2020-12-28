from selenium import webdriver
import time
import unittest


class TestUnittest(unittest.TestCase):
    def test_registration1(self):
        self.link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        self.first_name_field = self.browser.find_element_by_css_selector(".first_block .first")
        self.first_name_field.send_keys("value")
        self.last_name_field = self.browser.find_element_by_css_selector(".first_block .second")
        self.last_name_field.send_keys("value")
        self.email_field = self.browser.find_element_by_css_selector(".first_block .third")
        self.email_field.send_keys("value")
        self.button = self.browser.find_element_by_css_selector("[type='submit']")
        self.button.click()
        time.sleep(1)
        self.welcome_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text)
        self.browser.quit()


    def test_registration2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        self.first_name_field = self.browser.find_element_by_css_selector(".first_block .first")
        self.first_name_field.send_keys("value")
        self.last_name_field = self.browser.find_element_by_css_selector(".first_block .second")
        self.last_name_field.send_keys("value")
        self.email_field = self.browser.find_element_by_css_selector(".first_block .third")
        self.email_field.send_keys("value")
        self.button = self.browser.find_element_by_css_selector("[type='submit']")
        self.button.click()
        time.sleep(1)
        self.welcome_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text)
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()

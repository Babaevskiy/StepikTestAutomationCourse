from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize("link", links)
def test_correct_text(browser, link):
    answer = str(math.log(int(time.time())))
    browser.get(link)
    field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "textarea")))
    field.send_keys(answer)
    button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "submit-submission")))
    button.click()
    feedback = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    feedback_text = feedback.text
    assert "Correct!" == feedback_text

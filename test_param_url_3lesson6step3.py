# открыть страницу
# ввести правильный ответ
# нажать кнопку отправить
# дождаться фидбека о том что ответ правильный
# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_url(browser, url):
    answer = math.log(int(time.time()))
    link = f"{url}"
    browser.get(link)
    textarea = browser.find_element_by_xpath('//textarea')
    textarea.send_keys(str(answer))
    button = browser.find_element_by_xpath('//button[@class="submit-submission"]')
    button.click()
    #ember123 = WebDriverWait(browser, 2).until(
    #    EC.text_to_be_present_in_element((By.ID, "ember123"), "Абсолютно точно.")
    #)
    pre = browser.find_element_by_xpath('//pre')
    pre_text = pre.text
    assert "Correct!" == pre_text
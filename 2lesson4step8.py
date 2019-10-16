from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()
    price = WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    book_button = driver.find_element_by_xpath('//button[@id="book"]')
    book_button.click()
    x_element = driver.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    answer_form = driver.find_element_by_xpath('//input[@id="answer"]')
    answer_form.send_keys(y)
    button_submit = driver.find_element_by_xpath('//button[@type="submit"]')
    button_submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()
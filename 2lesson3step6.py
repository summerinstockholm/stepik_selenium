from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()
    button_start = driver.find_element_by_xpath('//button[@type="submit"]')
    button_start.click()
    current_window = driver.current_window_handle
    new_window = driver.window_handles[2]
    driver.switch_to.window(new_window)
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
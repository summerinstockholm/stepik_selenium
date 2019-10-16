from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()
    x_element = driver.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    driver.execute_script("window.scrollBy(0, 100);")
    answer_form = driver.find_element_by_xpath('//input[@id="answer"]')
    answer_form.send_keys(y)
    robot_checkbox = driver.find_element_by_xpath('//input[@id="robotCheckbox"]')
    robot_checkbox.click()
    robot_radiobutton = driver.find_element_by_xpath('//input[@id="robotsRule"]')
    robot_radiobutton.click()
    button_submit = driver.find_element_by_xpath('//button[@type="submit"]')
    button_submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()
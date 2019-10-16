from selenium import webdriver
import time
import math
def calc(treasure_value):
    return str(math.log(abs(12 * math.sin(int(treasure_value)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()
    time.sleep(3)
    treasure_picture = driver.find_element_by_xpath('//img[@id="treasure"]')
    treasure_value = treasure_picture.get_attribute('valuex')
    y = calc(treasure_value)
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
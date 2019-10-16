from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()
    x_element = driver.find_element_by_xpath('//span[@id="num1"]')
    y_element = driver.find_element_by_xpath('//span[@id="num2"]')
    x = x_element.text
    y = y_element.text
    sum = str(str(int(x)+int(y)))
    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_value(sum)
    button_submit = driver.find_element_by_xpath('//button[@type="submit"]')
    button_submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()
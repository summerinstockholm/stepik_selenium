import math
from selenium.webdriver.chrome.webdriver import WebDriver
import time
driver = WebDriver(executable_path='F://chromedriver//chromedriver.exe')

link = "http://suninjuly.github.io/find_link_text"
try:
    driver.get(link)
    linktext = str(math.ceil(math.pow(math.pi, math.e)*10000))
    search_linktext = driver.find_element_by_link_text(linktext)
    search_linktext.click()
    input1 = driver.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id('country')
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
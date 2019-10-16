import math
from selenium.webdriver.chrome.webdriver import WebDriver
import time
driver = WebDriver(executable_path='F://chromedriver//chromedriver.exe')

link = "http://suninjuly.github.io/huge_form.html"
try:
    driver.get(link)
    elements = driver.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("Хуй")
    button = driver.find_element_by_xpath('//button')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()
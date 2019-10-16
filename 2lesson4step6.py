#Неявные ожидания
from selenium import webdriver
driver = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течении 5 секунд
driver.implicitly_wait(5)
link = " http://suninjuly.github.io/cats.html"
driver.get(link)
button = driver.find_element_by_id("button")
button.click()

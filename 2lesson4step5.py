#Неявные ожидания
from selenium import webdriver
driver = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течении 5 секунд
driver.implicitly_wait(5)
link = "http://suninjuly.github.io/wait1.html"
driver.get(link)
button = driver.find_elements_by_id("verify")
button.click()
message = driver.find_element_by_id("verify_message")
assert "successful" in message.txt
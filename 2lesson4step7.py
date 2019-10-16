from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button.click()
message = driver.find_element_by_id("verify_message")

assert "successful" in message.text
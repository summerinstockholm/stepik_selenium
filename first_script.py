import time
from selenium.webdriver.chrome.webdriver import WebDriver
driver = WebDriver(executable_path='F://chromedriver//chromedriver.exe')
time.sleep(5)
driver.get("https://stepik.org/lesson/25969/step/12")
driver.maximize_window()
time.sleep(5)
textarea = driver.find_elements_by_css_selector(".textarea")
textarea.send_keys("get()")
time.sleep(5)
submit_button = driver.find_elements_by_css_selector(".submit-submission")
submit_button.click()
time.sleep(5)
driver.quit()
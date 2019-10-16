from selenium import webdriver
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()
    first_name = driver.find_element_by_xpath('//input[@name="firstname"]')
    first_name.send_keys('хуй')
    last_name = driver.find_element_by_xpath('//input[@name="lastname"]')
    last_name.send_keys('пизда')
    email = driver.find_element_by_xpath('//input[@name="email"]')
    email.send_keys('am@ya.ru')
    button_file = driver.find_element_by_xpath('//input[@name="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'empty.txt')  # добавляем к этому пути имя файла
    button_file.send_keys(file_path)
    button_submit = driver.find_element_by_xpath('//button[@type="submit"]')
    button_submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()
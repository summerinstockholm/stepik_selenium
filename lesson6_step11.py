from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    firstname = browser.find_element_by_xpath('//input[@placeholder="Input your first name" and @required]')
    firstname.send_keys('Иван')
    lastname = browser.find_element_by_xpath('//input[@placeholder="Input your last name" and @required]')
    lastname.send_keys('Иванов')
    email = browser.find_element_by_xpath('//input[@placeholder="Input your email" and @required]')
    email.send_keys('ivanivanov@gmail.ru')
    # Достал атрибут placeholder, т.к. он выглядел самым уникальным в input. А так да, лучше искать по класссу. Но в данном случае вариант с xpath тоже валиден.
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
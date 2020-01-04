import unittest
from selenium import webdriver
import time

class TestReg(unittest.TestCase):
    def testreg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        firstname = browser.find_element_by_xpath('//input[@placeholder="Input your first name" and @required]')
        firstname.send_keys('Иван')
        lastname = browser.find_element_by_xpath('//input[@placeholder="Input your last name" and @required]')
        lastname.send_keys('Иванов')
        email = browser.find_element_by_xpath('//input[@placeholder="Input your email" and @required]')
        email.send_keys('ivanivanov@gmail.ru')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
    def testreg2(self):
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
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
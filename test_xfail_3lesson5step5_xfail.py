# XFail: помечать тест как ожидаемо падающий
# Теперь добавим в наш тестовый класс тест, который проверяет наличие кнопки "Избранное":
# def test_guest_should_see_search_button_on_the_main_page(self, browser):
#      browser.get(link)
#      browser.find_element_by_css_selector("button.favorite")
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")

# Запустим наши тесты:
# pytest -v test_fixture10.py
# Наш упавший тест теперь отмечен как xfail, но результат прогона тестов помечен как успешный:

#Conftest.py и передача параметров в командной строке
#Встроенная фикстура request может получать данные о текущем запущенном тесте, что позволяет, например, сохранять дополнительные данные в отчёт,
# а также делать многие другие интересные вещи. В этом шаге мы хотим показать, как можно настраивать тестовые окружения с помощью передачи параметров через командную строку.
#Это делается с помощью встроенной функции pytest_addoption и фикстуры request.
# Сначала добавляем в файле conftest обработчик опции в функции pytest_addoption,
# затем напишем фикстуру, которая будет обрабатывать переданные в опции данные. Подробнее можно ознакомиться здесь: https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption
#Добавим логику обработки командной строки в conftest.py. Для запроса значения параметра мы можем вызвать команду:
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
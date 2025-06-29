import pytest
from requests.utils import default_user_agent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
@pytest.fixture
def browser(request):

    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    time.sleep(30)
    browser.quit()

#@pytest.fixture
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language, for example: ru/fr/es...')


@pytest.fixture(scope="function")
def language(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    #browser = webdriver.Chrome(options=options)
    #link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



























    # link = None
    # if language == "ru":
    #     print("\nstart ru version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    # elif language == "en-gb":
    #     print("\nstart en-gb version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    # elif language == "fr":
    #     print("\nstart fr version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/")
    # elif language == "ar":
    #     print("\nstart ar version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/ar/catalogue/coders-at-work_207/")
    # elif language == "ca":
    #     print("\nstart ca version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/ca/catalogue/coders-at-work_207/")
    # elif language == "cs":
    #     print("\nstart cs version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/cs/catalogue/coders-at-work_207/")
    # elif language == "da":
    #     print("\nstart da version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/da/catalogue/coders-at-work_207/")
    # elif language == "de":
    #     print("\nstart de version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/de/catalogue/coders-at-work_207/")
    # elif language == "el":
    #     print("\nstart el version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/el/catalogue/coders-at-work_207/")
    # elif language == "es":
    #     print("\nstart es version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/")
    # elif language == "fi":
    #     print("\nstart fi version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/fi/catalogue/coders-at-work_207/")
    # elif language == "it":
    #     print("\nstart it version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/it/catalogue/coders-at-work_207/")
    # elif language == "ko":
    #     print("\nstart ko version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/ko/catalogue/coders-at-work_207/")
    # elif language == "nl":
    #     print("\nstart nl version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/nl/catalogue/coders-at-work_207/")
    # elif language == "pl":
    #     print("\nstart pl version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/pl/catalogue/coders-at-work_207/")
    # elif language == "pt":
    #     print("\nstart pt version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/pt/catalogue/coders-at-work_207/")
    # elif language == "pt-br":
    #     print("\nstart pt-br version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/pt-br/catalogue/coders-at-work_207/")
    # elif language == "ro":
    #     print("\nstart ro version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/ro/catalogue/coders-at-work_207/")
    # elif language == "sk":
    #     print("\nstart sk version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/sk/catalogue/coders-at-work_207/")
    # elif language == "uk":
    #     print("\nstart uk version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/")
    # elif language == "zh-cn":
    #     print("\nstart zh-cn version for test..")
    #     link = ("https://selenium1py.pythonanywhere.com/zh-cn/catalogue/coders-at-work_207/")


















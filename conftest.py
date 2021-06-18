import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#reading the parameter 'language'
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language (default - en): ")


@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")
    options = Options()
    #setting the language option
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    #turning off the output of excess log
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
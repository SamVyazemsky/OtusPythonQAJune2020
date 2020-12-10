import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store',
                     default='chrome')
    parser.addoption('--url', action='store',
                     default='http://localhost/')


@pytest.fixture
def page_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="function")
def web_driver(request):
    browser = request.config.getoption('--browser')
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument('start-fullscreen')
        browser = webdriver.Chrome(chrome_options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.add_argument('start-fullscreen')
        browser = webdriver.Firefox(firefox_options=options)
    yield browser
    browser.quit()




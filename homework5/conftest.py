import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store',
                     default='chrome')
    parser.addoption('--url', action='store',
                     default='http://localhost/')


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="function")
def browser(request, url):
    browser = request.config.getoption('--browser')
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = False
        options.add_argument('start-fullscreen')
        driver = webdriver.Chrome(chrome_options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.add_argument('start-fullscreen')
        driver = webdriver.Firefox(firefox_options=options)
    else:
        raise Exception("Такой браузер не поддерижвается")

    # yield browser
    # browser.quit()
    driver.implicitly_wait(5)
    driver.maximize_window()

    request.addfinalizer(driver.quit)
    def open(path=""):
        return driver.get(url + path)
    driver.open = open
    driver.open()
    return driver






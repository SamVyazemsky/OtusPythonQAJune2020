import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from .page_object.common.MyListiner import MyListener


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
        driver = EventFiringWebDriver(webdriver.Chrome(chrome_options=options), MyListener())

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.add_argument('start-fullscreen')
        driver = EventFiringWebDriver(webdriver.Firefox(firefox_options=options), MyListener())
    else:
        raise Exception("Такой браузер не поддерижвается")

    # yield browser
    # browser.quit()
    driver.implicitly_wait(5)
    driver.maximize_window()

    session_id = driver.session_id

    allure.attach(name=session_id,
                  body=str(driver.desired_capabilities),
                  attachment_type=allure.attachment_type.JSON)

    request.addfinalizer(driver.quit)

    def open(path=""):
        return driver.get(url + path)
    driver.open = open
    driver.open()
    return driver






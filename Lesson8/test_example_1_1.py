import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions


@pytest.fixture
def browser():  # request
    chrome_options = ChromeOptions()
    chrome_options.headless = True
    # if pytest.getOptinons("browser") == chrome:
    wd = webdriver.Chrome(options=chrome_options)
    # elif pytest.getOptinons("browser") == firefox:
    # wd = webdriver.Firefox(options=firefox_options)
    yield
    # request.addfinalizer(wd.quit)
    wd.quit()
    # return wd


def test_example(browser):
    """

    """
    browser.get("https://www.google.com//")
    element = browser.find_element_by_css_selector("*[name=q]")
    element.send_keys("Python Zen")
    element.send_keys(Keys.ENTER)
    assert browser.title == 'Python Zen - Поиск в Google'

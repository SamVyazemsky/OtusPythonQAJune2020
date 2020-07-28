import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def chrome_browser(request):

    desired_capabilities = {'browserName': 'chrome',
                            'version': '2',
                            'javascriptEnabled': True}
    wd = webdriver.Chrome(desired_capabilities=desired_capabilities)

    print(wd.capabilities)

    request.addfinalizer(wd.quit)
    return wd


def test_example(chrome_browser):
    """
    Example with cookie and run with capabilities
    """
    chrome_browser.get("https://otus.ru/")
    chrome_browser.add_cookie({'name': 'test', 'value': 'bar'})  # Добавить Cookie
    chrome_browser.get_cookie('test')  # Считать информацию о cookie
    chrome_browser.delete_cookie('test')  # Удалить Cookie
    chrome_browser.delete_all_cookies()  # Удалить все cookies

import pytest
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import DesiredCapabilities as DC

@pytest.fixture
def chrome_browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument('start-fullscreen')
    options.headless = False
    options.binary_location = "/usr/bin/google-chrome"
    #options.headless = True
   # options.add_argument("headless")
    wd = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
    # cap = DC()
    request.addfinalizer(wd.quit)
    return wd


def test_example(chrome_browser):
    """
    Example with ChromeOptions
    """
    chrome_browser.get("https://otus.ru/")


def test_mailru(chrome_browser):
    chrome_browser.get("https://mail.ru/")
    picture_link = chrome_browser.find_element_by_css_selector("a[data-name=pictures]")
    picture_link.click()
    find_string = chrome_browser.find_element_by_css_selector("input[name=q]")
    find_string.click()
    find_string.clear()
    find_string.send_keys("qa automation")
    click_button = chrome_browser.find_element_by_css_selector("button[type=submit]")
    click_button.click()
    found_picture = chrome_browser.find_element_by_css_selector("div#mediaResponsesList > div[data-index='1'] > a > div > img")
    src = found_picture.get_attribute('currentSrc')
    r = requests.get(src)
    with open('res.jpg', 'wb') as f:
        f.write(r.content)

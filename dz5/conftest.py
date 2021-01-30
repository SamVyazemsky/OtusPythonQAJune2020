import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help="Choose browser: chrome, firefox or ie"
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://demo.opencart.com",
        help="Request base url"
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080");
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        wd = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = webdriver.FirefoxOptions()
        options.add_argument("--window-size=1920,1080");
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        wd = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    elif browser_name == "ie":
        print("\nstart Internet Explorer browser for test..")
        options = webdriver.IeOptions()
        options.add_argument("--window-size=1920,1080");
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        wd = webdriver.Ie(IEDriverManager().install(), options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or ie")
    yield wd
    print("\nquit browser..")
    wd.quit()

@pytest.fixture(scope="function")
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="function")
def admin_login(browser, base_url):
    browser.get(url=f'{base_url}/admin/')
    browser.find_element(By.ID, "input-password").submit()
    WebDriverWait(browser, 5).until(EC.title_is('Dashboard'))
    return True

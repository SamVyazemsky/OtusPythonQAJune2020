import pytest
from selenium import webdriver
from pages.main import MainPage
from pages.catalog import CatalogPage
from pages.account import LoginPage
from pages.admin import AdminPage
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


@pytest.fixture()
def main_page(browser):
    page = MainPage(browser)
    page.go_to('/')
    return page


@pytest.fixture()
def catalog_page(browser, path):
    page = CatalogPage(browser)
    page.go_to(f'/index.php?route=product/{path}')
    return page


@pytest.fixture()
def account_page(browser, path):
    page = LoginPage(browser)
    page.go_to(f'/index.php?route=account/{path}')
    return page


@pytest.fixture()
def admin_page(browser):
    page = AdminPage(browser)
    page.go_to(f'/admin/')
    return page


@pytest.fixture(scope="function")
def admin_login(browser, admin_page):
    page = AdminPage(browser)
    page.go_to(f'/admin/')
    browser.find_element(By.ID, "input-password").submit()
    WebDriverWait(browser, 5).until(EC.title_is('Dashboard'))
    return True

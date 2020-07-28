import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser():
	options = webdriver.ChromeOptions()
	# options.add_argument("headless")
	wd = webdriver.Chrome(options=options)
	yield wd
	wd.quit()


@pytest.fixture
def firefox_browser():
    wd = webdriver.Firefox()
    yield wd
    wd.quit()
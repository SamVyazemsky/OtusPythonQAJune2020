import pytest
import selenium


def test_opencart(web_driver, page_url):
    wd = web_driver
    wd.get(page_url)
    current_url = wd.current_url
    assert current_url == "http://localhost/"


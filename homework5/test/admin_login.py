import pytest
import time

url_category = "/admin/index.php?route=common/login"
user_admin = "user"
password_admin = "bitnami"


@pytest.mark.parametrize("login_password", [('admin', 'admin'), ('ttt@mail.ru', '12345'), ('pochta@@mailru', 'fsdfsdfsdf')])
def test_error_login(login_password, web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_id("input-username").send_keys(login_password[0])
    wd.find_element_by_id("input-password").send_keys(login_password[1])
    wd.find_element_by_css_selector("#content > div > div > div > div > "
                                    "div.panel-body > form > div.text-right > button").click()
    time.sleep(1)
    error_text = wd.find_element_by_css_selector("#content > div > div > div > div > div.panel-body > div").text
    assert "No match for Username and/or Password." in error_text


def test_forgotten_back(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_css_selector('#content > div > div > div > div > div.panel-body > '
                                    'form > div:nth-child(2) > span > a').click()
    wd.find_element_by_id("input-email").click()
    wd.find_element_by_id("input-email").send_keys("ttt@mail.ru")
    wd.find_element_by_css_selector("#content > div > div > div > div > "
                                    "div.panel-body > form > div.text-right > a").click()
    current_url = wd.current_url
    assert current_url == "http://localhost/admin/index.php?route=common/login"


def test_forgotten_error(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_css_selector('#content > div > div > div > div > div.panel-body > '
                                    'form > div:nth-child(2) > span > a').click()
    wd.find_element_by_id("input-email").click()
    wd.find_element_by_id("input-email").send_keys("ttt@mail.ru")
    wd.find_element_by_css_selector("#content > div > div > div > div > "
                                    "div.panel-body > form > div.text-right > button").click()
    error_text = wd.find_element_by_css_selector("#content > div > div > div > div > div.panel-body > div").text
    assert "Warning: The E-Mail Address was not found in our records, please try again!" in error_text


def test_login_admin(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_id("input-username").send_keys(user_admin)
    wd.find_element_by_id("input-password").send_keys(password_admin)
    wd.find_element_by_tag_name("button").click()
    current_url = wd.current_url
    assert "http://localhost/admin/index.php?route=common/dashboard" in current_url


def test_logout(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_id("input-username").send_keys(user_admin)
    wd.find_element_by_id("input-password").send_keys(password_admin)
    wd.find_element_by_tag_name("button").click()
    login_url = wd.current_url
    wd.find_element_by_css_selector("#header > div > ul > li:nth-child(2) > a").click()
    logout_url = wd.current_url
    assert logout_url == "http://localhost/admin/index.php?route=common/login" and "http://localhost/admin/index.php?route=common/dashboard" in login_url


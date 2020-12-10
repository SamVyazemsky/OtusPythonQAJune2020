import pytest
import time
import random

url_category = "/index.php?route=account/login"
email = "mail" + str(random.randint(1,1000000000)) + "@mail.ru"


@pytest.mark.parametrize("login_password", [('admin@adsa.ru', 'admin'), ('ttt@mail.ru', '12345'), ('pochta@@mailru', 'fsdfsdfsdf')])
def test_error_login(login_password, web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_id("input-email").send_keys(login_password[0])
    wd.find_element_by_id("input-password").send_keys(login_password[1])
    wd.find_element_by_css_selector("#content > div > div:nth-child(2) > div > form > input").click()
    time.sleep(1)
    error_text = wd.find_element_by_css_selector("#account-login > div.alert.alert-danger.alert-dismissible").text
    assert error_text == "Warning: No match for E-Mail Address and/or Password."


def test_button_new_customer(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_css_selector("#content > div > div:nth-child(1) > div > a").click()
    new_customer = wd.find_element_by_css_selector("#content > h1").text
    assert new_customer == "Register Account"


def test_forgotten_password_link(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_css_selector('#content > div > div:nth-child(2) > div > form > div:nth-child(2) > a').click()
    new_customer = wd.find_element_by_css_selector("#content > h1").text
    assert new_customer == "Forgot Your Password?"


def test_login(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_css_selector("#content > div > div:nth-child(1) > div > a").click()
    wd.find_element_by_id("input-firstname").click()
    time.sleep(1)
    wd.find_element_by_id("input-firstname").send_keys("Kirill" + str(random.randint(1,1000000000)))
    wd.find_element_by_id("input-lastname").click()
    wd.find_element_by_id("input-lastname").send_keys("qwerty1234" + str(random.randint(1,1000000000)))
    wd.find_element_by_id("input-email").click()
    wd.find_element_by_id("input-email").send_keys(email)
    wd.find_element_by_id("input-telephone").click()
    wd.find_element_by_id("input-telephone").send_keys("+777777")
    wd.find_element_by_id("input-password").click()
    wd.find_element_by_id("input-password").send_keys("11111")
    wd.find_element_by_id("input-confirm").click()
    wd.find_element_by_id("input-confirm").send_keys("11111")
    wd.find_element_by_css_selector("#content > form > div > div > input[type=checkbox]:nth-child(2)").click()
    wd.find_element_by_css_selector("#content > form > div > div > input.btn.btn-primary").click()
    create_account = wd.find_element_by_css_selector("#content > h1").text
    assert create_account == "Your Account Has Been Created!"


def test_forgotten_error(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_css_selector('#content > div > div:nth-child(2) > div > form > div:nth-child(2) > a').click()
    time.sleep(1)
    wd.find_element_by_id("input-email").click()
    wd.find_element_by_id("input-email").send_keys(email)
    wd.find_element_by_css_selector("#content > form > div > div.pull-right > input").click()
    time.sleep(1)
    error_text = wd.find_element_by_css_selector("#account-forgotten > div.alert.alert-danger.alert-dismissible").text
    assert "Warning: The E-Mail Address was not found in our records, please try again!" in error_text

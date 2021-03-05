import pytest
from homework5.page_object.LoginPage import Login
import time


@pytest.mark.parametrize("login_password", Login.login_password)
def test_error_login(browser, login_password):
    browser.open(Login.url_login)
    error_text = Login(browser).\
        input_data(Login.INPUT_EMAIL, login_password[0])\
        .input_data(Login.INPUT_PASSWORD, login_password[1])\
        .click(Login.BUTTON_LOGIN)\
        .get_element_text(Login.NOTIFICATION_ERROR)

    assert error_text == Login.error_text_notification


def test_button_new_customer(browser):
    browser.open(Login.url_login)
    h1_register = Login(browser).\
        click(Login.NEW_USER).\
        get_element_text(Login.H1_REGISTER_ACCOUNT)

    assert h1_register == Login.h1_register_template


def test_forgotten_password_link(browser):
    browser.open(Login.url_login)
    h1_password_recovery = Login(browser).click(Login.FORGOTTEN_PASSWORD_LINK)\
        .get_element_text(Login.H1_REGISTER_ACCOUNT)

    assert h1_password_recovery == Login.h1_password_recovery_template


def test_login(browser):
    browser.open(Login.url_login)
    new_user = Login(browser).click(Login.NEW_USER)\
        .input_data(Login.FIRST_NAME, Login.name)\
        .input_data(Login.LAST_NAME, Login.name)\
        .input_data(Login.EMAIL, Login.email)\
        .input_data(Login.TELEPHONE, Login.telephone)\
        .input_data(Login.INPUT_PASSWORD, Login.password)\
        .input_data(Login.CONFIRM_PASSWORD, Login.password)\
        .click(Login.NEWSLETTER_CHECKBOX_YES)\
        .click(Login.PRIVACY_POLICY)\
        .click(Login.INPUT_CONTINUE)
    h1_register = new_user.get_element_text(Login.H1_REGISTER_ACCOUNT)
    assert h1_register == Login.h1_new_account_register
#TODO: не вводит перое поле, ожидания

def test_forgotten_error(browser):
    browser.open(Login.url_login)
    forgotten_error = Login(browser).\
        click(Login.FORGOTTEN_PASSWORD_LINK).\
        input_data(Login.INPUT_EMAIL, "test_email@12.ru")\
        .click(Login.INPUT_CONTINUE).get_element_text(Login.NOTIFICATION_ERROR)
    assert Login.error_forgotten_notification in forgotten_error

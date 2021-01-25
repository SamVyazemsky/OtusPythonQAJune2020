import pytest
import allure
from selenium.common.exceptions import NoSuchElementException
from homework5.page_object.LoginPage import Login


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Проверка страницы авторизации пользователя.")
@allure.feature("Проверка получения ошибки при некорректном вводе данных")
@allure.title("Вводим некорректный логин и пароль. Получаем ошибку.")
@pytest.mark.parametrize("login_password", Login.login_password)
def test_error_login(browser, login_password):
    browser.open(Login.url_login)
    with allure.step("Получаем Ошибку при не корректном логине/пароли"):
        try:
            error_text = Login(browser)\
                .input_data(Login.INPUT_EMAIL, login_password[0])\
                .input_data(Login.INPUT_PASSWORD, login_password[1])\
                .click(Login.BUTTON_LOGIN)\
                .get_element_text(Login.NOTIFICATION_ERROR)
        except NoSuchElementException as e:
            allure.attach(body=browser.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)
        raise AssertionError(e.msg)

    assert error_text == Login.error_text_notification


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Проверка страницы авторизации пользователя.")
@allure.feature("Проверка перехода по ссылки на страницу регистрации нового пользователя.")
@allure.title("Нажимаем на кнопку новый пользователь и проверяем h1 загаловок страницы.")
def test_button_new_customer(browser):
    browser.open(Login.url_login)
    h1_register = Login(browser).\
        click(Login.NEW_USER).\
        get_element_text(Login.H1_REGISTER_ACCOUNT)

    assert h1_register == Login.h1_register_template


@allure.severity(allure.severity_level.NORMAL)
@allure.story("Проверка страницы авторизации пользователя.")
@allure.feature("Проверка перехода по ссылки на страницу восстановления пароля.")
@allure.title("Нажимаем на ссылку востановления пароля и проверяем h1 загаловок страницы.")
def test_forgotten_password_link(browser):
    browser.open(Login.url_login)
    h1_password_recovery = Login(browser).click(Login.FORGOTTEN_PASSWORD_LINK)\
        .get_element_text(Login.H1_REGISTER_ACCOUNT)

    assert h1_password_recovery == Login.h1_password_recovery_template


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Проверка страницы регитсрации нового пользователя.")
@allure.feature("Регистрируем нового пользоавтеля.")
@allure.title("Переходим на страницу регистрации нового пользователя."
              "Вводим корректный данные для регистрации."
              "Получаем подтверждения, что регистрация прошла успешно.")
def test_login(browser):
    browser.open(Login.url_login)
    with allure.step("Регистрируем нового пользователя"):
        try:
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
        except NoSuchElementException as e:
            allure.attach(body=browser.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e.msg)
        h1_register = new_user.get_element_text(Login.H1_REGISTER_ACCOUNT)

    assert h1_register == Login.h1_new_account_register


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка страницы авторизации пользователя.')
@allure.feature("Проверка ошибки при восстановление пароля.")
@allure.title("Нажимаем на ссылку востановления пароля"
              "Вводим не существующий в базе  email."
              "Получаем корректную ошибку.")
def test_forgotten_error(browser):
    browser.open(Login.url_login)
    forgotten_error = Login(browser).\
        click(Login.FORGOTTEN_PASSWORD_LINK).\
        input_data(Login.INPUT_EMAIL, "test_email@12.ru")\
        .click(Login.INPUT_CONTINUE).get_element_text(Login.NOTIFICATION_ERROR)
    assert Login.error_forgotten_notification in forgotten_error

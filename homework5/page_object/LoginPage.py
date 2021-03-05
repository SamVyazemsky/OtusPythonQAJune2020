from .BasePage import BasePage
from selenium.webdriver.common.by import By
import random


class Login(BasePage):

        url_login = "/index.php?route=account/login"
        name = "test" + str(random.randint(1, 1000000000))
        email = "mail" + str(random.randint(1, 1000000000)) + "@mail.ru"
        telephone = "+700012345960"
        password = "alfmsFNNRR123"
        login_password = [('admin@adsa.ru', 'admin'), ('ttt@mail.ru', '12345'), ('pochta@@mailru', 'fsdfsdfsdf')]

        error_text_notification = "Warning: No match for E-Mail Address and/or Password."
        h1_register_template = "Register Account"
        h1_password_recovery_template = "Forgot Your Password?"
        h1_new_account_register = "Your Account Has Been Created!"
        error_forgotten_notification = "Warning: The E-Mail Address was not found in our records, please try again!"

        INPUT_EMAIL = (By.ID, 'input-email')
        INPUT_PASSWORD = (By.ID, 'input-password')
        BUTTON_LOGIN = (By.XPATH, '//input[@value="Login"]')
        NOTIFICATION_ERROR = (By.CSS_SELECTOR, '.alert-danger')
        NEW_USER = (By.XPATH, '//a[text()="Continue"]')
        H1_REGISTER_ACCOUNT = (By.CSS_SELECTOR, '#content h1')
        FORGOTTEN_PASSWORD_LINK = (By.XPATH, '//a[text()="Forgotten Password"]')
        FIRST_NAME = (By.ID, 'input-firstname')
        LAST_NAME = (By.ID, 'input-lastname')
        EMAIL = (By.ID, 'input-email')
        TELEPHONE = (By.ID, 'input-telephone')
        CONFIRM_PASSWORD = (By.ID, 'input-confirm')
        NEWSLETTER_CHECKBOX_YES = (By.XPATH, '//input[@name="newsletter"]')
        PRIVACY_POLICY = (By.XPATH, '//input[@name="agree"]')
        INPUT_CONTINUE = (By.XPATH, '//input[@value="Continue"]')


        def click(self, locator):
            self._find_element(locator).click()
            return self

        def get_element_text(self, locator):
            return self._find_element(locator).text

        def input_data(self, locator, value):
            self._input(locator, value)
            return self
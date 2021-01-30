from selenium.webdriver.common.by import By
from .base import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[value = \'Login\']")
    FORGOTTEN_PASS_LINK = (By.CSS_SELECTOR, "[href = \'https://demo.opencart.com/index.php?route=account/forgotten\']")
    REG_ACC_BUTTON = (By.CSS_SELECTOR, "[href = \'https://demo.opencart.com/index.php?route=account/register']")
    REG_FIRST_NAME = (By.ID, "input-firstname")
    REG_LAST_NAME = (By.ID, "input-lastname")
    REG_EMAIL = (By.ID, "input-email")
    REG_TELEPHONE = (By.ID, "input-telephone")
    REG_PASS = (By.ID, "input-password")
    REG_PASS_CONFIRM = (By.ID, "input-confirm")
    REG_PRIVACY_POLICY = (By.NAME, "agree")
    REG_CONTINUE = (By.CSS_SELECTOR, "[value='Continue']")
    REG_ACCOUNT_CREATED = (By.CSS_SELECTOR, "#content h1")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def should_be_login_elements(self):
        self.find_element(locator=self.EMAIL_INPUT)
        self.find_element(locator=self.PASSWORD_INPUT)
        self.find_element(locator=self.LOGIN_BUTTON)
        self.find_element(locator=self.FORGOTTEN_PASS_LINK)
        self.find_element(locator=self.REG_ACC_BUTTON)

    def input_reg_first_name(self):
        self.find_element(locator=self.REG_FIRST_NAME).send_keys('first name')

    def input_reg_last_name(self):
        self.find_element(locator=self.REG_LAST_NAME).send_keys('last name')

    def input_reg_email(self):
        self.find_element(locator=self.REG_EMAIL).send_keys('autotests@opencart.com')

    def input_reg_telephone(self):
        self.find_element(locator=self.REG_TELEPHONE).send_keys('+70000000000')

    def input_reg_pass(self):
        self.find_element(locator=self.REG_PASS).send_keys('123456')

    def input_reg_pass_confirm(self):
        self.find_element(locator=self.REG_PASS_CONFIRM).send_keys('123456')

    def accept_reg_policy(self):
        self.find_element(locator=self.REG_PRIVACY_POLICY).click()

    def accept_reg_form(self):
        self.find_element(locator=self.REG_CONTINUE).click()

    def new_account_created(self):
        self.wait_for_title('Your Account Has Been Created!')
        text = self.find_element(locator=self.REG_ACCOUNT_CREATED).text
        assert "Your Account Has Been Created!" == text, "Successful registration message didn`t show"

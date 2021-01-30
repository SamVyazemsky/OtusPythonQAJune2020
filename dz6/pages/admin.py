from selenium.webdriver.common.by import By
from .base import BasePage


class AdminPage(BasePage):
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    FORGOTTEN_PASS_LINK = (By.CSS_SELECTOR, "[href=\'https://demo.opencart.com/admin/index.php?route=common/forgotten']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    HEADER_LOGO = (By.CSS_SELECTOR, ".navbar-brand")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".hidden-xs.hidden-sm.hidden-md")
    MENU_CATALOG = (By.ID, "menu-catalog")
    MENU_PRODUCTS = (By.CSS_SELECTOR, "#collapse1 li:nth-child(2)")
    PRODUCT_LIST = (By.CSS_SELECTOR, "#content div.container-fluid div div.col-md-9.col-md-pull-3.col-sm-12 div")
    PANEL_FILTER = (By.CSS_SELECTOR, ".panel.panel-default")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def should_be_login_elements(self):
        self.find_element(locator=self.USERNAME_INPUT)
        self.find_element(locator=self.PASSWORD_INPUT)
        self.find_element(locator=self.FORGOTTEN_PASS_LINK)
        self.find_element(locator=self.LOGIN_BUTTON)
        self.find_element(locator=self.HEADER_LOGO)

    def login_successful(self):
        self.find_element(locator=self.USERNAME_INPUT).clear()
        self.find_element(locator=self.USERNAME_INPUT).send_keys('demo')
        self.find_element(locator=self.PASSWORD_INPUT).clear()
        self.find_element(locator=self.PASSWORD_INPUT).send_keys('demo')
        self.find_element(locator=self.PASSWORD_INPUT).submit()
        self.wait_for_title('Dashboard')

    def logout(self):
        self.driver.find_element(locator=self.LOGOUT_BUTTON).click()
        self.wait_for_title('Administration')

    def open_menu_products(self):
        self.find_element(locator=self.MENU_CATALOG).click()
        self.wait_for_element_clickable(locator=self.MENU_PRODUCTS)
        self.find_element(locator=self.MENU_PRODUCTS).click()

    def check_product_list(self):
        self.wait_for_element_clickable(locator=self.PRODUCT_LIST)
        self.find_element(locator=self.PRODUCT_LIST)

    def check_panel_filter(self):
        self.wait_for_element_clickable(locator=self.PANEL_FILTER)
        self.find_element(locator=self.PANEL_FILTER)

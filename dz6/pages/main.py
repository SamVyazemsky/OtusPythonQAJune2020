from selenium.webdriver.common.by import By
from .base import BasePage


class MainPage(BasePage):
    HEADER_TABLETS = (By.LINK_TEXT, "Tablets")
    HEADER_SOFTWARE = (By.LINK_TEXT, "Software")
    HEADER_PHONES = (By.LINK_TEXT, "Phones & PDAs")
    HEADER_CAMERAS = (By.LINK_TEXT, "Cameras")
    HEADER_DESKTOPS = (By.LINK_TEXT, "Desktops")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn.btn-default.btn-lg")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def should_be_header_elements(self):
        self.find_element(locator=self.HEADER_TABLETS)
        self.find_element(locator=self.HEADER_SOFTWARE)
        self.find_element(locator=self.HEADER_PHONES)
        self.find_element(locator=self.HEADER_CAMERAS)
        self.find_element(locator=self.HEADER_DESKTOPS)

    def search(self, value):
        self.find_element(locator=self.SEARCH_INPUT).send_keys(value)
        self.find_element(locator=self.SEARCH_BUTTON).click()

    def title_is(self, expected_title):
        self.wait_for_title(expected_title)

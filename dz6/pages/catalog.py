from selenium.webdriver.common.by import By
from .base import BasePage


class CatalogPage(BasePage):
    IPHONE_PHOTO = (By.CSS_SELECTOR, "[alt='iPhone']")
    IPHONE_PRICE = (By.CSS_SELECTOR, "div:nth-child(5) p.price")
    IPHONE_ADD_CART = (By.CSS_SELECTOR, "div:nth-child(5) div div:nth-child(2) button:nth-child(1)")
    IPHONE_ADD_WISHLIST = (By.CSS_SELECTOR, "div:nth-child(5) div div:nth-child(2) button:nth-child(2)")
    IPHONE_COMPARE = (By.CSS_SELECTOR, "div:nth-child(5) div div:nth-child(2) button:nth-child(3)")

    PRODUCT_DESCRIPTION = (By.ID, "tab-description")
    PRODUCT_ADD_CART = (By.ID, "button-cart")
    CART_BUTTON = (By.ID, "cart")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content div div.col-sm-4 h1")
    PRICE_VALUE = (By.CSS_SELECTOR, "#content div div.col-sm-4 ul:nth-child(4) li:nth-child(1) h2")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def should_be_catalog_elements(self):
        self.find_element(locator=self.IPHONE_PHOTO)
        self.find_element(locator=self.IPHONE_PRICE)
        self.find_element(locator=self.IPHONE_ADD_CART)
        self.find_element(locator=self.IPHONE_ADD_WISHLIST)
        self.find_element(locator=self.IPHONE_COMPARE)

    def should_be_product_card_elements(self):
        self.find_element(locator=self.PRODUCT_DESCRIPTION)
        self.find_element(locator=self.PRODUCT_ADD_CART)
        self.find_element(locator=self.CART_BUTTON)
        self.find_element(locator=self.PRODUCT_NAME)
        self.find_element(locator=self.PRICE_VALUE)

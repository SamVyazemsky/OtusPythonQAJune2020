import time
from .BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    price_euro = '392.30€'
    price_dollar = '$500.00'
    price_pound = '£306.25'

    SLIDESHOW = (By.ID, "slideshow0")
    NAME_PRODUCT = (By.CSS_SELECTOR, '#content h1')
    FEATURED_PRODUCTS = (By.CSS_SELECTOR, '.product-layout')
    CURRENCY_DROP_MENU = (By.CSS_SELECTOR, '#form-currency button')
    CURRENCY_EURO = (By.XPATH, '//button[text()="€ Euro"]')
    CURRENCY_POUND_STERLING = (By.XPATH, '//button[text()="£ Pound Sterling"]')
    CURRENCY_DOLLAR = (By.XPATH, '//button[text()="$ US Dollar"]')
    CORRECT_PRICE_EURO = (By.XPATH, f"//span[@class='price-tax'and text()='Ex Tax: {price_euro}']")
    CORRECT_PRICE_DOLLAR = (By.XPATH, f"//span[@class='price-tax'and text()='Ex Tax: {price_dollar}']")
    CORRECT_PRICE_POUND = (By.XPATH, f"//span[@class='price-tax'and text()='Ex Tax: {price_pound}']")
    INPUT_SEARCH = (By.XPATH, '//*[@id="search"]/input')
    BUTTON_SEARCH = (By.CSS_SELECTOR, '#search span')
    TEXT_AFTER_SEARCH = (By.CSS_SELECTOR, '#content > h1')

    def count_featured_products(self, locator):
        a = MainPage(self.driver)._find_elements(locator, 1)
        return len(a)

    def input_search(self, locator, value):
        return self._input(locator, value)

    def get_result(self, locator):
        time.sleep(2)
        return self._find_element(locator).text

    def click(self, locator):
        self._find_element(locator).click()
        return self




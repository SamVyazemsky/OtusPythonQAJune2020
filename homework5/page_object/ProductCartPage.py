import time
from .BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductCartPage(BasePage):
    url_product = "/macbook"
    wish_list_assert_text = 'Wish List (1)'

    NAME_PRODUCT = (By.CSS_SELECTOR, '#content h1')
    BUTTON_ADD_WISH_LIST = (By.XPATH, '//button[@data-original-title="Add to Wish List"]')
    WISH_LIST = (By.CSS_SELECTOR, '#wishlist-total span')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '#content li h2')
    BUTTON_ADD_TO_CART = (By.ID, 'button-cart')
    SHOPPING_CART = (By.ID, 'cart-total')
    AMOUNT_OF_GOODS = (By.ID, 'input-quantity')
    BUTTON_REVIEWS = (By.XPATH, '//a[text()="0 reviews"]')
    BUTTON_WRITE_REVIEWS = (By.XPATH, '//a[text()="Write a review"]')
    BUTTON_TAB_REVIEWS = (By.XPATH, '//a[@href="#tab-review"]')
    REVIEW_NAME = (By.ID, 'input-name')
    REVIEW_TEXT = (By.ID, 'input-review')
    SEND_REVIEW = (By.ID, 'button-review')
    NOTIFICATION_SUCCESS_REVIEW_ADD = (By.CSS_SELECTOR, '#form-review > div.alert.alert-success.alert-dismissible')

    def add_product_cart(self, locator):
        self.click(self.BUTTON_ADD_TO_CART)
        time.sleep(2)
        return self._get_element_string(locator)

    def add_comment(self, locator, value_rating=1):
        self.click(locator)
        self.input_data(self.REVIEW_NAME, "Kirill")
        self.input_data(self.REVIEW_TEXT, "Текст длиной более 25 символоа!!!!!!!!!!!!!")
        self.click((By.XPATH, f'//input[@name="rating" and @value="{value_rating}"]'))
        self.click(self.SEND_REVIEW)
        return self._get_element_string(self.NOTIFICATION_SUCCESS_REVIEW_ADD)

    def save_price(self, locator=PRICE_PRODUCT):
        return self._find_element(locator).text

    def click(self, locator):
        self._find_element(locator).click()
        return self

    def get_element_text(self, locator):
        return self._find_element(locator).text

    def input_data(self, locator, value):
        self._input(locator, value)
        return self



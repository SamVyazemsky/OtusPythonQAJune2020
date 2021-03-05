from .BasePage import BasePage
from selenium.webdriver.common.by import By
from .BasePage import BasePage
import selenium


class Catalog(BasePage):
    url_category = "/index.php?route=product/category&path=20"
    link_text_category = [(
        ((By.LINK_TEXT, 'Desktops'),"Desktops"),
        ((By.LINK_TEXT, 'Tablets'),"Tablets"),
        ((By.LINK_TEXT, 'Software'),"Software"),
        ((By.LINK_TEXT, 'Phones & PDAs'),"Phones & PDAs"),
        ((By.LINK_TEXT, 'Cameras'),"Cameras"))]
    first_product = "Sony VAIO"

    IMG_CATALOG = (By.CLASS_NAME, 'img-responsive')
    ADD_TO_CART_BUTTON = (By.XPATH, '//span[text()="Add to Cart"]')
    SWITCH_SORT = (By.ID, 'input-sort')
    SORT_SWITCH_Z_to_A = (By.XPATH, '//option[text()="Name (Z - A)"]')
    FIRST_PRODUCT = (By.CSS_SELECTOR, '#content h4 a')
    LINK_CATEGORY_CAMERAS = (By.LINK_TEXT, 'Cameras')
    LIST_MENU = (By.CLASS_NAME, 'list-group-item')
    H2_CATEGORY_PRODUCT = (By.CSS_SELECTOR, '#content h2')

    def click(self, locator):
        self._find_element(locator).click()
        return self

    def get_element_text(self, locator):
        return self._find_element(locator).text

    def input_data(self, locator, value):
        self._input(locator, value)
        return self

    def get_count_elements(self, locator):
        count = self._find_elements(locator)
        return len(count)

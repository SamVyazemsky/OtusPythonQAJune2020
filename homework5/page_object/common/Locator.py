from selenium.webdriver.common.by import By


class LocatorMainPage:

    """ 
    Локаторы главной страницы
    """

    SLIDESHOW = (By.ID, "slideshow0")
    NAME_PRODUCT = (By.CSS_SELECTOR, '#content h1')
    FEATURED_PRODUCTS = (By.CSS_SELECTOR, 'product-layout')
    CURRENCY_DROP_MENU = (By.CSS_SELECTOR, '#form-currency button')
    CURRENCY_EURO = (By.XPATH, '//button[text()="€ Euro"]')
    CURRENCY_POUND_STERLING = (By.XPATH, '//button[text()="£ Pound Sterling"]')
    CURRENCY_DOLLAR = (By.XPATH, '//button[text()="$ US Dollar]')


class LocatorSearch:
    INPUT_SEARCH = (By.XPATH, '//*[@id="search"]/input')
    BUTTON_SEARCH = (By.CSS_SELECTOR, '#search span')
    TEXT_AFTER_SEARCH = (By.CSS_SELECTOR, '#content > h1')


class LocatorShopCart:
    CART_BUTTON = (By.CSS_SELECTOR, '#cart button')
    CART_DROP_NOTIFICATION = (By.CSS_SELECTOR, '.dropdown-menu p')
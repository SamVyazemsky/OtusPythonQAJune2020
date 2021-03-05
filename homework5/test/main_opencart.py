import pytest
import time
import selenium
from homework5.page_object.MainPage import MainPage
from homework5.page_object.common.ShopCart import ShopCart
from homework5.page_object.common.Search import Search


def test_slider_link(browser):
    h1_product = MainPage(browser)\
        .click(MainPage.SLIDESHOW)\
        .get_element_text(MainPage.NAME_PRODUCT)
    assert h1_product == "Samsung Galaxy Tab 10.1"


def test_count_product(browser):
    count_featured = MainPage(browser)\
        .count_featured_products(MainPage.FEATURED_PRODUCTS)
    assert count_featured == 4


@pytest.mark.parametrize("input_test_search", ('mac', 'Mac', 'MAC'))
def test_search(browser, input_test_search):
    result_search = MainPage(browser)\
        .input_search(MainPage.INPUT_SEARCH, input_test_search)\
        .click(Search.BUTTON_SEARCH)\
        .get_element_text(Search.RESULT_SEARCH)
    assert result_search == f"Search - {input_test_search}"


def test_button_cart(browser):
    notification = MainPage(browser)\
        .click(ShopCart.CART_BUTTON)\
        .get_element_text(ShopCart.CART_DROP_NOTIFICATION)
    assert notification == "Your shopping cart is empty!"



@pytest.mark.parametrize("currency_and_url", [(MainPage.CURRENCY_EURO, MainPage.price_euro, MainPage.CORRECT_PRICE_EURO),
                                      (MainPage.CURRENCY_POUND_STERLING, MainPage.price_pound, MainPage.CURRENCY_POUND_STERLING),
                                      (MainPage.CURRENCY_DOLLAR, MainPage.price_dollar, MainPage.CURRENCY_DOLLAR)])
def test_money(browser, currency_and_url):
    price = MainPage(browser)\
        .click(MainPage.CURRENCY_DROP_MENU)\
        .click(currency_and_url[0])\
        #.get_result(currency_and_url[2]) #TODO поменять локаторы на корректные

    # wd.find_element_by_css_selector("#form-currency > div > button").click()
    # wd.find_element_by_css_selector(currency_and_url[0]).click()
    # price = wd.find_element_by_css_selector(currency_and_url[2])
    # assert price == currency_and_url[1]


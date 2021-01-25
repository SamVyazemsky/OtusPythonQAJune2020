import pytest
import allure
from homework5.page_object.MainPage import MainPage
from homework5.page_object.common import Search
from homework5.page_object.common import ShopCart

@allure.severity(allure.severity_level.NORMAL)
@allure.story('Проверка основной страницы сайта.')
@allure.feature("Проверка клика на слайдер")
@allure.title("Кликаем на слайдер,"
              "Переходим на странницу товара Samsung Galaxy Tab 10.1,"
              "Проверяем заголовок.")
def test_slider_link(browser):
    h1_product = MainPage(browser)\
        .click(MainPage.SLIDESHOW)\
        .get_element_text(MainPage.NAME_PRODUCT)
    assert h1_product == "Samsung Galaxy Tab 10.1"


@allure.severity(allure.severity_level.NORMAL)
@allure.story('Проверка основной страницы сайта.')
@allure.feature("Проверка количества нового товара на странице")
@allure.title("Получаем число новых продуктов на главной странице"
              "Сравниваем его с ожидаемым числом")
def test_count_product(browser):
    count_featured = MainPage(browser)\
        .count_featured_products(MainPage.FEATURED_PRODUCTS)
    assert count_featured == 4


@allure.severity(allure.severity_level.NORMAL)
@allure.story('Проверка основной страницы сайта.')
@allure.feature("Проверка клика на слайдер")
@allure.title("Кликаем на слайдер,"
              "Переходим на странницу товара Samsung Galaxy Tab 10.1,"
              "Проверяем заголовок.")
@pytest.mark.parametrize("input_test_search", ('mac', 'Mac', 'MAC'))
def test_search(browser, input_test_search):
    result_search = MainPage(browser)\
        .input_search(MainPage.INPUT_SEARCH, input_test_search)\
        .click(Search.BUTTON_SEARCH)\
        .get_element_text(Search.RESULT_SEARCH)
    assert result_search == f"Search - {input_test_search}"


@allure.severity(allure.severity_level.NORMAL)
@allure.story('Проверка основной страницы сайта.')
@allure.feature("Проверка пустой корзины товаров")
@allure.title("Кликаем на корзину товаров"
              "Получаем сообщения о том, что она пуста")
def test_button_cart(browser):
    notification = MainPage(browser)\
        .click(ShopCart.CART_BUTTON)\
        .get_element_text(ShopCart.CART_DROP_NOTIFICATION)
    assert notification == "Your shopping cart is empty!"


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка основной страницы сайта.')
@allure.feature("Проверка пустой корзины товаров")
@allure.title("Кликаем на корзину товаров"
              "Получаем сообщения о том, что она пуста")
@pytest.mark.parametrize("currency_and_url", [(MainPage.CURRENCY_EURO, MainPage.price_euro, MainPage.CORRECT_PRICE_EURO),
                                      (MainPage.CURRENCY_POUND_STERLING, MainPage.price_pound, MainPage.CORRECT_PRICE_POUND),
                                      (MainPage.CURRENCY_DOLLAR, MainPage.price_dollar, MainPage.CORRECT_PRICE_DOLLAR)])
def test_money(browser, currency_and_url):
    price = MainPage(browser)\
        .click(MainPage.CURRENCY_DROP_MENU)\
        .click(currency_and_url[0])\
        .get_result(currency_and_url[2])

    assert currency_and_url[1] in price


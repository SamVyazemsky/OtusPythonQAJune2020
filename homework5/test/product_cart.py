import pytest
import allure
from homework5.page_object.ProductCartPage import ProductCartPage


@allure.severity(allure.severity_level.NORMAL)
@allure.story("Проверка страницу 'карта товара'")
@allure.feature("Проверка корректного перехода на страницу с картой товара")
@allure.title("Переходим в карту товара 'Макбук' и проверяем заголовок страницы")
def test_h1(browser):
    browser.open(ProductCartPage.url_product)
    text = ProductCartPage(browser) \
        .get_element_text(ProductCartPage.NAME_PRODUCT)
    assert text == "MacBook"


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Проверка страницу 'карта товара'")
@allure.feature("Проверка добавления товара в списокк желаний")
@allure.title("Открываем карту товара, "
              "нажимаем кнопку 'Добавить в список желаемого' и проверям, "
              "что спсиок увеличился на 1")
def test_wish_list(browser):
    browser.open(ProductCartPage.url_product)
    text = ProductCartPage(browser)\
        .click(ProductCartPage.BUTTON_ADD_WISH_LIST)\
        .get_element_text(ProductCartPage.WISH_LIST)
    assert ProductCartPage.wish_list_assert_text in text


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Проверка страницу 'карта товара'")
@allure.feature("Проверка добавления товара в корзину")
@allure.title("Открываем карту товара, "
              "сохраняем цену товара"
              "нажимаем кнопку 'Добавить в корзину' и проверям, "
              "что в корзине 1 товар с ценной товара")
def test_add_cart(browser):
    browser.open(ProductCartPage.url_product)
    price_product = ProductCartPage(browser).save_price()
    price_shop_cart = ProductCartPage(browser)\
        .add_product_cart(ProductCartPage.SHOPPING_CART)

    assert price_shop_cart == "1 item(s) - " + price_product


@allure.severity(allure.severity_level.NORMAL)
@allure.story("Проверка страницу 'карта товара'")
@allure.feature("Проверка добавления указаного кол-ва товаров в корзину")
@allure.title("Открываем карту товара, "
              "вписываем количество товара"
              "нажимаем кнопку 'Добавить в корзину' и проверям, "
              "что в корзине указанное кол-во товаров")
@pytest.mark.parametrize("count", (2, 3, 4, 10))
def test_add_cart_many(browser, count):
    browser.open(ProductCartPage.url_product)
    ProductCartPage(browser).input_data(ProductCartPage.AMOUNT_OF_GOODS, count)
    count_items = ProductCartPage(browser) \
        .add_product_cart(ProductCartPage.SHOPPING_CART)

    assert f"{count} item(s) -" in count_items


@allure.severity(allure.severity_level.NORMAL)
@allure.story("Проверка страницу 'карта товара'")
@allure.feature("Проверка отправки комментария при переходе с разных мест страницы 'карта товара' с разными оценками")
@allure.title("Открываем карту товара, "
              "переходим на добавления комментария к товару,"
              "добавлениям данные и устанавливаем оценку и проверям,"
              "что комментарий успешно отправлен на одорбрение")
@pytest.mark.parametrize("locator", (ProductCartPage.BUTTON_REVIEWS, ProductCartPage.BUTTON_WRITE_REVIEWS,
                                     ProductCartPage.BUTTON_TAB_REVIEWS))
@pytest.mark.parametrize("value_rating", (1, 2, 3, 4, 5))
def test_error_add_comment(browser, locator, value_rating):
    browser.open(ProductCartPage.url_product)
    alert = ProductCartPage(browser).add_comment(locator, value_rating)

    assert alert == "Thank you for your review. It has been submitted to the webmaster for approval."


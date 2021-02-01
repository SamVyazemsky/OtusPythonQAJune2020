import pytest
from homework5.page_object.CatalogePage import Catalog
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка старницы Каталог.')
@allure.feature("Проверка клика на фотографию товара.")
@allure.title("Кликаем по первой фотографии на странице.")
def test_link_image(browser):
    browser.open(Catalog.url_category)
    Catalog(browser).click(Catalog.IMG_CATALOG)


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка старницы Каталог.')
@allure.feature("Проверка нажатия на кнопку 'Добавления в корзину'")
@allure.title("Кликаем по первой кнопки 'Добавления в корзину' у товара.")
def test_button(browser):
    browser.open(Catalog.url_category)
    Catalog(browser).click(Catalog.ADD_TO_CART_BUTTON)


@allure.severity(allure.severity_level.NORMAL)
@allure.story('Проверка старницы Каталог.')
@allure.feature("Проверка сортировки на странице.")
@allure.title("Переключаем сортировку на Z-A и смотрим, что указанный товар отображается первый в каталоге.")
def test_sort(browser):
    browser.open(Catalog.url_category)
    h4_first_product = Catalog(browser).click(Catalog.SWITCH_SORT)\
        .click(Catalog.SORT_SWITCH_Z_to_A)\
        .get_element_text(Catalog.FIRST_PRODUCT)

    assert h4_first_product == Catalog.first_product


@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Проверка старницы Каталог.')
@allure.feature("Проверка кол-ва категорий в меню")
@allure.title("Переходим на категорию 'Камеры' и считаем кол-во категорий в боком меню.")
def test_count_main_menu(browser):
    browser.open(Catalog.url_category)
    count_category_main_menu = Catalog(browser)\
        .click(Catalog.LINK_CATEGORY_CAMERAS)\
        .get_count_elements(Catalog.LIST_MENU)
    assert count_category_main_menu == 8


@allure.severity(allure.severity_level.TRIVIAL)
@allure.story('Проверка старницы Каталог.')
@allure.feature("Проверка заголовков страниц категорий")
@allure.title("Поочередно заходим в каждую категорию и сравниваем заголовк на странице с корректным")
@pytest.mark.parametrize("input_data", Catalog.link_text_category)
def test_h2_name(browser, input_data):
    browser.open(Catalog.url_category)
    h2_category = Catalog(browser).click(input_data[0]).\
        get_element_text(Catalog.H2_CATEGORY_PRODUCT)
    assert h2_category == input_data[1]

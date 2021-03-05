import pytest
from homework5.page_object.CatalogePage import Catalog


def test_link_image(browser):
    browser.open(Catalog.url_category)
    Catalog(browser).click(Catalog.IMG_CATALOG)


def test_button(browser):
    browser.open(Catalog.url_category)
    Catalog(browser).click(Catalog.ADD_TO_CART_BUTTON)


def test_sort(browser):
    browser.open(Catalog.url_category)
    h4_first_product = Catalog(browser).click(Catalog.SWITCH_SORT)\
        .click(Catalog.SORT_SWITCH_Z_to_A)\
        .get_element_text(Catalog.FIRST_PRODUCT)

    assert h4_first_product == Catalog.first_product


def test_count_main_menu(browser):
    browser.open(Catalog.url_category)
    count_category_main_menu = Catalog(browser)\
        .click(Catalog.LINK_CATEGORY_CAMERAS)\
        .get_count_elements(Catalog.LIST_MENU)
    assert count_category_main_menu == 8


#TODO: не работает из-за селекторов, разобраться
@pytest.mark.parametrize("input_data", Catalog.link_text_category)
def test_h2_name(browser, input_data):
    browser.open(Catalog.url_category)
    h2_category = Catalog(browser).click(input_data[0]).\
        get_element_text(Catalog.H2_CATEGORY_PRODUCT)
    assert h2_category == input_data[1]







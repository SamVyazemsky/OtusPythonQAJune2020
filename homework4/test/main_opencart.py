import pytest
import time


def test_slider_link(web_driver, page_url):
    wd = web_driver
    wd.get(page_url)
    wd.find_element_by_id("slideshow0").click()
    h1 = wd.find_element_by_xpath('//*[@id="content"]/div/div[2]/h1')
    assert h1.text == "Samsung Galaxy Tab 10.1"


def test_count_product(web_driver, page_url):
    wd = web_driver
    wd.get(page_url)
    list_notebook = wd.find_elements_by_class_name("product-layout")
    assert len(list_notebook) == 4


@pytest.mark.parametrize("input_test_search", ('mac', 'Mac', 'MAC'))
def test_search(input_test_search, web_driver, page_url):
    wd = web_driver
    wd.get(page_url)
    wd.find_element_by_xpath('//*[@id="search"]/input').send_keys(input_test_search)
    wd.find_element_by_css_selector("#search > span").click()
    h1 = wd.find_element_by_css_selector("#content > h1")
    assert h1.text == f"Search - {input_test_search}"


def test_button_cart(web_driver, page_url):
    wd = web_driver
    wd.get(page_url)
    wd.find_element_by_css_selector("#cart > button").click()
    notification = wd.find_element_by_css_selector("#cart > ul > li > p")
    assert notification.text == "Your shopping cart is empty!"


@pytest.mark.parametrize("currency_and_url", [('#form-currency > div > ul > li:nth-child(1) > button', '392.30€', '#content > div.row > div:nth-child(1) > div > div.caption > p.price > span'),
                                      ('#form-currency > div > ul > li:nth-child(2) > button', '£61.86', '#content > div.row > div:nth-child(2) > div > div.caption > p.price > span'),
                                      ('#form-currency > div > ul > li:nth-child(3) > button', '$90.00', '#content > div.row > div:nth-child(3) > div > div.caption > p.price > span.price-tax')])
def test_money(currency_and_url, web_driver, page_url):
    wd = web_driver
    wd.get(page_url)
    wd.find_element_by_css_selector("#form-currency > div > button").click()
    wd.find_element_by_css_selector(currency_and_url[0]).click()
    price = wd.find_element_by_css_selector(currency_and_url[2])
    print(price.text + '==' + currency_and_url[1])
    assert currency_and_url[1] == price.text



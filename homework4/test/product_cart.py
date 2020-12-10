import pytest
import time


url_category = "/macbook"


def test_h1(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    h1 = wd.find_element_by_css_selector("#content > div > div.col-sm-4 > h1")
    print(h1.text)
    assert h1.text == "MacBook"


def test_wish_list(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_css_selector("#content > div > div.col-sm-4 > div.btn-group > button:nth-child(1)").click()
    wish = wd.find_element_by_css_selector("#wishlist-total > span")
    assert "Wish List (1)" in wish.text


def test_add_cart(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    price = wd.find_element_by_css_selector("#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > h2")
    wd.find_element_by_id("button-cart").click()
    time.sleep(2)
    shop_cart = wd.find_element_by_id("cart-total")
    assert shop_cart.text == "1 item(s) - " + price.text


@pytest.mark.parametrize("count", (2, 3, 4, 10))
def test_add_cart_many(count, web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_id("input-quantity").clear()
    wd.find_element_by_id("input-quantity").send_keys(count)
    wd.find_element_by_id(("button-cart")).click()
    time.sleep(2)
    shop_cart = wd.find_element_by_id("cart-total")
    assert f"{count} item(s) -" in shop_cart.text


@pytest.mark.parametrize("url", ('#content > div > div.col-sm-4 > div.rating > p > a:nth-child(6)',
                                 '#content > div > div.col-sm-4 > div.rating > p > a:nth-child(7)',
                                 '#content > div > div.col-sm-8 > ul.nav.nav-tabs > li:nth-child(3) > a'))
def test_error_add_comment(url, web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_css_selector(url).click()
    wd.find_element_by_id("input-name").send_keys("Kirill")
    wd.find_element_by_id("input-review").send_keys("Текст длиной более 25 символоа!!!!!!!!!!!!!")
    wd.find_element_by_id("button-review").click()
    time.sleep(1)
    error_text = wd.find_element_by_css_selector("#form-review > div.alert.alert-danger.alert-dismissible").text
    assert error_text == "Warning: Please select a review rating!"





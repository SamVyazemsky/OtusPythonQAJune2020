import pytest
import time

url_category = "/index.php?route=product/category&path=20"


def test_link_image(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_class_name('img-responsive').click()


def test_button_(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_tag_name("button").click()


def test_sort(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_id("input-sort").click()
    wd.find_element_by_css_selector("#input-sort > option:nth-child(3)").click()
    h4_first_product = wd.find_element_by_css_selector("#content > div:nth-child(7) > div:nth-child(1) > div > "
                                          "div:nth-child(2) > div.caption > h4 > a")
    assert h4_first_product.text == "Sony VAIO"


def test_count_main_menu(web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_link_text("Cameras").click()
    list_notebook = wd.find_elements_by_class_name("list-group-item")
    assert len(list_notebook) == 8


@pytest.mark.parametrize("input_h2", ("Desktops", "Tablets", "Software", "Phones & PDAs", "Cameras",))
def test_h2_name(input_h2, web_driver, page_url):
    wd = web_driver
    wd.get(page_url + url_category)
    wd.find_element_by_link_text(input_h2).click()
    h2 = wd.find_element_by_css_selector("#content > h2")
    assert h2.text == input_h2







import pytest


def test_title(main_page):
    assert main_page.driver.title == 'Your Store'


def test_main_page(main_page):
    main_page.should_be_header_elements()


@pytest.mark.parametrize('search_input, expected_title', [('iPhone', 'Search - iPhone'),
                                                          ('MacBook', 'Search - MacBook'),
                                                          ('Canon', 'Search - Canon')])
def test_main_search(main_page, search_input, expected_title):
    main_page.search(search_input)
    main_page.title_is(expected_title)

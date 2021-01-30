def test_title(admin_page):
    admin_page.should_be_login_elements()


def test_login_logout(admin_page):
    admin_page.login_successful()
    admin_page.logout()


def test_product_list(admin_page, admin_login):
    admin_page.open_menu_products()
    admin_page.check_product_list()


def test_filter(admin_page, admin_login):
    admin_page.open_menu_products()
    admin_page.check_panel_filter()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_title(browser, base_url):
    browser.get(url=f'{base_url}/')
    assert browser.title == 'Your Store'


def test_main_page_elements(browser, base_url):
    browser.get(url=f'{base_url}/')
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.LINK_TEXT, "Tablets")))
    assert browser.find_element(By.LINK_TEXT, "Tablets"), 'iPhone photo is not presented'
    assert browser.find_element(By.LINK_TEXT, "Software"), 'iPhone price is not presented'
    assert browser.find_element(By.LINK_TEXT, "Phones & PDAs"), 'Cart add button is not presented'
    assert browser.find_element(By.LINK_TEXT, "Cameras"), 'Wishlist add button is not presented'
    assert browser.find_element(By.LINK_TEXT, "Desktops"), 'Compare add button is not presented'


def test_catalog_page_elements(browser, base_url):
    browser.get(url=f'{base_url}/index.php?route=product/category&path=20')
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[alt='iPhone']")))
    assert browser.find_element(By.CSS_SELECTOR, "[alt='iPhone']"), 'iPhone photo is not presented'
    assert browser.find_element(By.CSS_SELECTOR, "div:nth-child(5) p.price"), 'iPhone price is not presented'
    assert browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(5) div div:nth-child(2) button:nth-child(1)"),\
                                'Cart add button is not presented'
    assert browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(5) div div:nth-child(2) button:nth-child(2)"),\
                                'Wishlist add button is not presented'
    assert browser.find_element(By.CSS_SELECTOR,
                                "div:nth-child(5) div div:nth-child(2) button:nth-child(3)"),\
                                'Compare add button is not presented'


def test_product_page_elements(browser, base_url):
    browser.get(url=f'{base_url}/index.php?route=product/product&path=57&product_id=49')
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, "cart")))
    assert browser.find_element(By.ID, "tab-description"), 'Description is not presented'
    assert browser.find_element(By.ID, "button-cart"), 'Add to Cart button is not presented'
    assert browser.find_element(By.ID, "cart"), 'Cart button is not presented'
    assert browser.find_element(By.CSS_SELECTOR, "#content div div.col-sm-4 h1"),\
                                'Product name is not presented'
    assert browser.find_element(By.CSS_SELECTOR,
                                "#content div div.col-sm-4 ul:nth-child(4) li:nth-child(1) h2"),\
                                'Price name is not presented'


def test_login_page_elements(browser, base_url):
    browser.get(url=f'{base_url}/index.php?route=account/login')
    assert browser.find_element(By.ID, "input-email"), 'Email input is not presented'
    assert browser.find_element(By.ID, "input-password"), 'Password input is not presented'
    assert browser.find_element(By.CSS_SELECTOR, "[value = \'Login\']"), 'Login button is not presented'
    assert browser.find_element(By.CSS_SELECTOR,
                                "[href = \'https://demo.opencart.com/index.php?route=account/forgotten\']"),\
                                'Forgotten Password link is not presented'
    assert browser.find_element(By.CSS_SELECTOR,
                                "[href = \'https://demo.opencart.com/index.php?route=account/register']"),\
                                'Register Account button is not presented'


def test_admin_page_elements(browser, base_url):
    browser.get(url=f'{base_url}/admin/')
    assert browser.find_element(By.ID, "input-username"), 'Username input is not presented'
    assert browser.find_element(By.ID, "input-password"), 'Password input is not presented'
    assert browser.find_element(By.CSS_SELECTOR,
                                "[href=\'https://demo.opencart.com/admin/index.php?route=common/forgotten']"), \
                                'Forgotten Password link is not presented'
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary"), 'Login button is not presented'
    assert browser.find_element(By.CSS_SELECTOR, ".navbar-brand"), 'Logo button (header) is not presented'


def test_admin_login_logout(browser, base_url):
    browser.get(url=f'{base_url}/admin/')
    browser.find_element(By.ID, "input-username").clear()
    browser.find_element(By.ID, "input-password").clear()
    browser.find_element(By.ID, "input-username").send_keys('demo')
    browser.find_element(By.ID, "input-password").send_keys('demo')
    browser.find_element(By.ID, "input-password").submit()
    WebDriverWait(browser, 5).until(EC.title_is('Dashboard'))
    assert browser.title == 'Dashboard'
    browser.find_element(By.CSS_SELECTOR, ".hidden-xs.hidden-sm.hidden-md").click()
    WebDriverWait(browser, 5).until(EC.title_is('Administration'))
    assert browser.title == 'Administration'


def test_admin_products(browser, admin_login):
    browser.find_element(By.ID, "menu-catalog").click()
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#collapse1 > li:nth-child(2)")))
    browser.find_element(By.CSS_SELECTOR, "#collapse1 > li:nth-child(2)").click()
    assert browser.find_element(By.CSS_SELECTOR, ".panel.panel-default")

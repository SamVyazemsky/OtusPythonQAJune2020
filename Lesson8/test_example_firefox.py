import pytest
from selenium import webdriver
import pickle


def test_example(chrome_browser):
    """
    Example with ChromeOptions
    """
    chrome_browser.get('http://testing-ground.scraping.pro/login')
    chrome_browser.find_element_by_id('usr').send_keys('admin')
    chrome_browser.find_element_by_id('pwd').send_keys('12345')
    chrome_browser.find_element_by_css_selector('input[type=submit]').click()
    cookies = chrome_browser.get_cookies()
    pickle.dump(cookies, open("cookies.pkl", "wb"))


def test_two(chrome_browser):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    print(cookies)
    chrome_browser.delete_all_cookies()
    for each in cookies:
        chrome_browser.add_cookie(each)
    chrome_browser.get('http://testing-ground.scraping.pro/')
    print('Result')


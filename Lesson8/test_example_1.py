from selenium import webdriver
from selenium.webdriver import FirefoxOptions, Proxy
from webdrivermanager import GeckoDriverManager


def test_example():
    """
    First test
    """
    #Создаем объект менеджер
    gdd = GeckoDriverManager()
    gdd.download_and_install()
    # proxy = Proxy("http://user@password:proxy.example.com:123")
    option = FirefoxOptions()
    option.set_capability("browserName", "chrome")
    wd = webdriver.Firefox(options=option)
    wd.get("https://otus.ru/")
    assert wd.title == 'Онлайн‑курсы для профессионалов, дистанционное обучение современным профессиям'
    wd.quit()

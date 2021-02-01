from selenium.webdriver.common.by import By


class Search:
    INPUT_SEARCH = (By.XPATH, '//*[@id="search"]/input')
    BUTTON_SEARCH = (By.CSS_SELECTOR, '#search span')
    RESULT_SEARCH = (By.CSS_SELECTOR, '#content > h1')

    def __init__(self, driver):
        self.driver = driver


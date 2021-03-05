from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def _find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")


    def _input(self, selector, value):
        element = self._find_element(selector)
        element.clear()
        element.send_keys(value)
        return self
    #
    # def get_element_string(self, locator, time=5):
    #     return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
    #                                                   message=f"Get element by locator {locator}").text
    #
    # def text_in_element(self, locator, text, timeout=3):
    #     return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text),
    #                                                       message=f"Get text element by {locator}")

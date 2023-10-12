from .manager import MyBrowser
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from enum import Enum

class ActionType(Enum):
    CLICK = "click"
    FILL = "fill"
    SELECT_DROPDOWN_OPTION = "select_dropdown_option"
    NAVIGATE = "navigate"

class WebActions:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait_for_element(locator, 3)
        self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        self.wait_for_element(locator, 3)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def wait_for_element(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def select_dropdown_option(self, locator, value=None, text=None):
        self.wait_for_element(locator, 5)
        dropdown = Select(self.driver.find_element(*locator))
        if value is not None:
            dropdown.select_by_value(value)
        if text is not None:
            dropdown.select_by_visible_text(text)

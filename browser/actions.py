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

class BrowserActions:
    """
    A class representing web actions that can be performed using a WebDriver.

    Args:
        driver: The WebDriver instance to use for performing the actions.

    Methods:
        __init__(self, driver): Initializes the WebActions instance with the specified WebDriver.
        navigate(self, url): Navigates to the specified URL.
        click(self, locator): Clicks on the element specified by the locator.
        input_text(self, locator, text): Enters the specified text into the element specified by the locator.
        wait_for_element(self, locator, timeout=30): Waits for the element specified by the locator to be present.
        select_dropdown_option(self, locator, value=None, text=None): Selects an option from the dropdown element specified by the locator.

    Example:
        ```python
        driver = webdriver.Chrome()
        actions = WebActions(driver)
        actions.navigate("https://www.example.com")
        actions.click((By.ID, "submit-button"))
        actions.input_text((By.NAME, "username"), "john.doe")
        actions.wait_for_element((By.CLASS_NAME, "message"), timeout=10)
        actions.select_dropdown_option((By.XPATH, "//select[@name='country']"), value="US")
        ```
    """

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        # go to url
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

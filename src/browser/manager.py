from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# import sister module -> /data/real_info/user_agent.py
from data.real_info.user_agent import generate_random_user_agent

import undetected_chromedriver as uc


class MyBrowser(uc.Chrome):
    """
    A class representing a customized web browser based on `undetected_chromedriver`.

    This class extends the functionality of the undetected_chromedriver by adding custom methods
    for navigation, clicking elements, inputting text, waiting for elements, and selecting dropdown options.
    It also allows for dynamic user agent setting and additional browser options configuration.

    Attributes:
        options (Options): The options used to configure the browser.
        user_agent (str): The user agent string for the browser.

    Methods:
        navigate(url): Navigates to the given URL.
        click(locator): Clicks on the element identified by the locator.
        input_text(locator, text): Inputs text into the element identified by the locator.
        wait_for_element(locator, timeout=30): Waits for an element to be present on the page.
        select_dropdown_option(locator, value=None, text=None): Selects an option in a dropdown menu.
    """

    def __init__(self, options=None):
        """
        Initializes the MyBrowser instance with the specified options.

        Args:
            options (Options, optional): The options to configure the browser. Defaults to None.
        """
        self.options = options or Options()

        self._setup_options()
        self.options.add_argument("--start-maximized")
        self.user_agent = generate_random_user_agent()
        self.options.add_argument(f'user-agent={self.user_agent}')

    def navigate(self, url):
        """
        Navigates to the given URL.

        Args:
            url (str): The URL to navigate to.
        """
        try:
            super().get(url)
        except Exception as e:
            print(f"Navigation error: {e}")

    def click(self, locator):
        """
        Clicks on the element identified by the locator.

        Args:
            locator (tuple): A tuple containing the method to locate the element and the locator string.
        """
        try:
            self.wait_for_element(locator).click()
        except Exception as e:
            print(f"Click error: {e}")

    def input_text(self, locator, text):
        """
        Inputs text into the element identified by the locator.

        Args:
            locator (tuple): A tuple containing the method to locate the element and the locator string.
            text (str): The text to input into the element.
        """
        try:
            element = self.wait_for_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Input text error: {e}")

    def wait_for_element(self, locator, timeout=30):
        """
        Waits for an element to be present on the page.

        Args:
            locator (tuple): A tuple containing the method to locate the element and the locator string.
            timeout (int, optional): The maximum time to wait for the element. Defaults to 30 seconds.

        Returns:
            WebElement: The located element.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))

    def select_dropdown_option(self, locator, value=None, text=None):
        """
        Selects an option in a dropdown menu identified by the locator.

        Args:
            locator (tuple): A tuple containing the method to locate the element and the locator string.
            value (str, optional): The value of the option to select. Defaults to None.
            text (str, optional): The visible text of the option to select. Defaults to None.
        """
        try:
            dropdown = Select(self.wait_for_element(locator))
            if value:
                dropdown.select_by_value(value)
            elif text:
                dropdown.select_by_visible_text(text)
        except Exception as e:
            print(f"Dropdown selection error: {e}")

    def verify_link(self, url: str, timeout: int = 30) -> bool:
        """
        Verifies the accessibility of a URL by navigating to it and checking for successful page load.

        Args:
            url (str): The URL to verify.
            timeout (int, optional): The maximum time to wait for the page to load. Defaults to 30 seconds.

        Returns:
            bool: True if the page loads successfully within the timeout period, False otherwise.
        """
        try:
            self.navigate(url)
            # Optionally, wait for a specific element to ensure the page has fully loaded
            # self.wait_for_element((By.CSS_SELECTOR, "body"), timeout=timeout)
            return True
        except TimeoutException:
            print(f"Timeout loading URL: {url}")
            return False
        except Exception as e:
            print(f"Error loading URL: {url}, Error: {e}")
            return False

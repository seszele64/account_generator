from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json

# ! move it to browser module
import sys
sys.path.append(".") # Adds higher directory to python modules path.
from browser.manager import Browser
browser = Browser()
browser.add_options("--start-maximized")
driver = browser.create_driver()

# Import the “Select” package
from selenium.webdriver.support.ui import Select

import logging
# Configure logging
logging.basicConfig(filename='instruction_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')


class Instruction:
    def __init__(self, xpath, action, value=None):
        self.xpath = xpath
        self.action = action
        self.value = value

    def perform_action(self, driver):
        """
            Performs an action on a web element based on the provided parameters.

            Args:
                * self: The current instance of the class.
                * driver: The WebDriver instance used to interact with the web page.

            Returns:
                True if the action was performed successfully.

            Raises:
                TimeoutException: If the element with the specified XPath is not found.

            Example:
                ```python
                driver = webdriver.Chrome()
                xpath = '/html/body/div[5]/div/div/div/button[2]/div[3]'
                action = 'click'
                ```
        """

        try:

            # await element to load -> max 10 seconds
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.xpath)))

            # Click the element
            if self.action == 'click':
                element.click()
                logging.info(f"Clicked element with XPath: {self.xpath}")

            # Input the value into the field
            elif self.action == 'input':
                element.send_keys(self.value)
                logging.info(f"Input '{self.value}' into element with XPath: {self.xpath}")


            # Select the option from the dropdown
            elif self.action == 'select':
                dropdown = Select(driver.find_element(By.XPATH, self.xpath))
                dropdown.select_by_visible_text(self.value)
                logging.info(f"Input '{self.value}' into element with XPath: {self.xpath}")

            
            # wait for the element to load
            elif self.action == 'wait':
                if element is not None:
                    return True
            return True
        
        except TimeoutException:
            logging.error(f"TimeoutException: Element with XPath {self.xpath} not found")
            return False

def perform_instructions(
        driver: webdriver,
        base_url: str,
        instructions: list[Instruction]
    ):
    
    """
    Performs a series of instructions on a web page (base_url)

    Args:
        * base_url: The base URL of the web page to register on.
        * driver: The WebDriver instance used to interact with the web page.
        * instructions: A list of Instruction objects representing the actions to perform.

    Returns:
        bool: True if the registration is successful, False otherwise.

    Raises:
        TimeoutException: If the action times out while waiting for an element to load.

    Example:
        ```python
        base_url = "https://example.com"
        driver = webdriver.Chrome()
        instructions = [
            Instruction(xpath="//input[@id='username']", action="input", value="john"),
            Instruction(xpath="//input[@id='password']", action="input", value="password"),
            Instruction(xpath="//button[@id='register']", action="click")
        ]
        register(base_url, driver, instructions)
        ```
    """

    try:
        # open the base url
        driver.get(base_url)

        for instruction in instructions:
            
            response = instruction.perform_action(driver)

            if not response:
                return False # One of the instructions failed
            
        return True # All instructions were performed successfully
    
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return False # An error occurred
    
    finally:
        driver.quit()
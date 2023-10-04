import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


import os
import sys
# Add the parent directory to the sys.path list
sys.path.append(".")
from browser.manager import global_browser as driver

class ServiceTasks:

    """
    Represents a set of tasks for performing actions on a website.

    Args:
        actions_data (dict): The data containing instructions for each action.

    Attributes:
        driver: The driver used for interacting with the website.
        actions_data (dict): The data containing instructions for each action.

    Methods:
        wait_for_element(xpath, wait_time=10): Waits for an element to be visible on the page.
        navigate(url): Navigates to a specified URL.
        click(xpath): Clicks on an element specified by its XPath.
        send_keys(xpath, keys): Sends keys to an input element specified by its XPath.
        perform_action(action_name, **kwargs): Performs an action based on its name.

    Example:
        ```python
        actions_data = {
            "action1": {
                "instructions": {
                    "instruction1": {
                        "type": "navigate",
                        "url": "https://example.com"
                    },
                    "instruction2": {
                        "type": "click",
                        "xpath": "//button[@id='submit']"
                    }
                }
            }
        }
        tasks = ServiceTasks(actions_data)
        tasks.perform_action("action1")
        ```
    """


    def __init__(self, actions_data):
        self.driver = driver
        self.actions_data = actions_data

    def wait_for_element(self, xpath, wait_time=10):
        try:
            return WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
        except Exception as e:
            print(f"Failed to find element with xpath {xpath}. Error: {e}")
            return False

    def navigate(self, **kwargs):
        if url := kwargs.get('url', None):
            self.driver.get(url.format(**kwargs))
            return True
        return False
        

    def click(self, xpath):
        if element := self.wait_for_element(xpath):
            element.click()
            return True
        return False

    def send_keys(self, xpath, keys):
        if element := self.wait_for_element(xpath):
            element.send_keys(keys)
            return True    
        return False
    
    def select_dropdown_option(self, xpath, value=None, text=None):
        if element := self.wait_for_element(xpath):
            select = Select(element)
            if value:
                select.select_by_value(value)
            elif text:
                select.select_by_visible_text(text)
            return True
        
        return False
    

    def perform_action(self, action_name, **kwargs):
        if action_name in self.actions_data:
            instructions = self.actions_data[action_name]['instructions']
            for instruction_name, instruction_data in instructions.items():

                success = True

                if instruction_data['type'] == 'navigate':
                    success = self.navigate(**{**instruction_data, **kwargs}) # Merge instruction_data and kwargs -> go to either url or url.format(**kwargs)
                elif instruction_data['type'] == 'click':
                    success = self.click(instruction_data['xpath'])
                elif instruction_data['type'] == 'input':
                    # Replace placeholders in input_value with actual values from kwargs
                    input_value_template = instruction_data['input_value']
                    input_value = input_value_template.format(**kwargs)
                    success = self.send_keys(instruction_data['xpath'], input_value)

                elif instruction_data['type'] == 'select':
                    # Replace placeholders in input_value with actual values from kwargs
                    select_value_template = instruction_data['select_value']
                    select_value = select_value_template.format(**kwargs)
                    success = self.select_dropdown_option(instruction_data['xpath'], value=select_value)

                elif instruction_data['type'] == 'wait':
                    duration = instruction_data.get('duration', 10)
                    success = self.wait_for_element(instruction_data['xpath'], duration)

                # Check if it's a skippable instruction and the action wasn't successful
                if not success and not instruction_data.get('skippable', False):
                    print(f"Failed to execute instruction {instruction_name} for action {action_name}!")
                    break  # or continue, depending on desired behavior

        else:
            print(f"Action '{action_name}' not found for Wolt service.")
                

class Service:

    """
    Represents a service for performing actions on a website.

    Args:
        config_path (str): The path to the configuration file.

    Attributes:
        driver: The driver used for interacting with the website.
        actions_data (dict): The loaded actions data from the configuration file.
        tasks (ServiceTasks): The tasks object for performing actions.

    Methods:
        load_actions(filename): Loads the actions data from a JSON file.
        execute(action_name, **kwargs): Executes an action based on its name.
        create_account(**kwargs): Performs the 'create_account' action.
        register(**kwargs): Performs the 'register' action.
        login(**kwargs): Performs the 'login' action.

    Example:
        ```python
        service = Service("https://example.com", "config.json")
        service.create_account(username="john", password="password")
        service.login(username="john", password="password")
        ```
    """



    def __init__(self, config_path):
        self.driver = driver
        self.actions_data = self.load_actions(config_path)
        self.tasks = ServiceTasks(self.actions_data)

    def load_actions(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)
        
    def execute(self, action_name, **kwargs):
        if action_name in self.actions_data:
            self.tasks.perform_action(action_name, **kwargs)
        else:
            print(f"Action '{action_name}' not found for chosen service.")


    def create_account(self, **kwargs):
        self.tasks.perform_action('create_account', **kwargs)

    def register(self, **kwargs):
        self.tasks.perform_action('register', **kwargs)

    def login(self, **kwargs):
        self.tasks.perform_action('login', **kwargs)
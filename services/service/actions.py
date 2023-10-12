
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from enum import Enum

import sys
sys.path.append(".")

# browser/__init__.py
# from browser import global_user_agent as user_agent,
from browser.manager import MyBrowser
from browser.actions import WebActions

class ActionType(Enum):
    CLICK = "click"
    FILL = "fill"
    SELECT_DROPDOWN_OPTION = "select_dropdown_option"
    NAVIGATE = "navigate"

class Actions:
    def __init__(self, browser: MyBrowser = None, **kwargs):
        self.browser = browser
        self.actions = []

    def add_action(self, action_type, *args, **kwargs):

        if action_type == ActionType.CLICK:
            action = ClickAction(self.browser, *args, **kwargs)
        elif action_type == ActionType.FILL:
            action = SendKeysAction(self.browser, *args, **kwargs)
        elif action_type == ActionType.SELECT_DROPDOWN_OPTION:
            action = SelectDropdownOptionAction(self.browser, *args, **kwargs)
        elif action_type == ActionType.NAVIGATE:
            action = NavigateAction(self.browser, *args, **kwargs)
        else:
            raise ValueError(f"Invalid action_type: {action_type}")

        self.actions.append(action)
        return self

    def select_action(self):
        self.print_actions()
        while True:
            try:
                action_index = int(input("Select action: "))
                if action_index < 0 or action_index >= len(self.actions):
                    print("Invalid action index. Please try again.")
                else:
                    return self.actions[action_index]
            except ValueError:
                print("Invalid input. Please enter a number.")

    def print_actions(self):
        for i, action in enumerate(self.actions):
            print(f"{i}: {action}")

    def run(self):
        for action in self.actions:
            try:
                action.execute()
            except Exception as e:
                print(f"An error occurred while executing action: {str(action)}")
                print(f"Error details: {e}")
                # You can handle the error as needed (e.g., logging or raising an error).
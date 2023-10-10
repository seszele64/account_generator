from .manager import global_browser, global_user_agent, MyBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Action:
    def __init__(self, browser: MyBrowser):
        self.browser = browser

    def find_element(self, by, value):
        return self.browser.find_element(by, value)

    def find_elements(self, by, value):
        return self.browser.find_elements(by, value)

    def execute(self):
        raise NotImplementedError("Subclasses must override execute() method")

class ClickAction(Action):
    def __init__(self, browser: MyBrowser, by, value):
        super().__init__(browser)
        self.by = by
        self.value = value

    def execute(self):
        element = self.find_element(self.by, self.value)
        element.click()

class SendKeysAction(Action):
    def __init__(self, browser: MyBrowser, by, value, keys):
        super().__init__(browser)
        self.by = by
        self.value = value
        self.keys = keys

    def execute(self):
        element = self.find_element(self.by, self.value)
        element.send_keys(self.keys)

class SelectDropdownOptionAction(Action):
    def __init__(self, browser: MyBrowser, by, value=None, text=None):
        super().__init__(browser)
        self.by = by
        self.value = value
        self.text = text

    def execute(self):
        dropdown = Select(self.find_element(self.by, self.value))
        
        if self.value is not None:
            dropdown.select_by_value(self.value)

        if self.text is not None:
            dropdown.select_by_visible_text(self.text)

class NavigateAction(Action):
    def __init__(self, browser: MyBrowser, url):
        super().__init__(browser)
        self.url = url

    def execute(self):
        self.browser.get(self.url)

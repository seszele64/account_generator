from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

# import sister module -> /data/real_info/user_agent.py
from data.real_info.user_agent import generate_random_user_agent
import undetected_chromedriver as uc

# # global user agent
# global_user_agent = generate_random_user_agent

class MyBrowser(uc.Chrome):
    """
    A class representing a customized web browser based on `webdriver.Chrome`.

    Args:
    options (Options, optional): The options to configure the browser. Defaults to None.

    Attributes:
    options (Options): The options used to configure the browser.
    user_agent (str): The user agent string for the browser.

    Methods:
    __init__(self, options: Options = None): Initializes the browser with the specified options.
    get_random_user_agent(self) -> str: Returns a random user agent string.
    change_user_agent(self): Changes the user agent of the browser.
    create_driver(self) -> webdriver.Chrome: Creates and returns a Chrome driver.
    add_options(self, options: Options): Adds additional options to the browser.

    Example:
    ```python
    options = Options()
    [browser](VALID_DIRECTORY) = MyBrowser(options)
    [browser](VALID_DIRECTORY).change_user_agent()
    [browser](VALID_DIRECTORY).add_options(options)
    ```
    """


    # -------------------------------- constructor ------------------------------- #

    def __init__(self, options: Options = None):

        # ---------------------------------- options --------------------------------- #
        # create options
        if options is None:
            self.options = Options()

        # add headless mode
        # self.options.add_argument('--headless')
        self.options.add_argument("--start-maximized")

        # -------------------------------- user agent -------------------------------- #

        self.user_agent = generate_random_user_agent()
        
        # add user agent to options
        self.options.add_argument(f'user-agent={self.user_agent}')

        # ----------------------------------- proxy ---------------------------------- #
        # self.proxy_server = self.create_proxy_server()
        # self.proxy = self.proxy_server.create_proxy()
        # self.options.add_argument(f'--proxy-server={self.proxy.proxy}')

        # ---------------------------------- driver ---------------------------------- #
        # create browser -> autoinstalled chrome
        self.driver = self.create_driver()

    # ---------------------------------- methods --------------------------------- #

    # change user agent
    def change_user_agent(self):
        random_user_agent = generate_random_user_agent()
        self.options.add_argument(f'user-agent={random_user_agent}')
        self.driver = self.create_driver()

    def create_driver(self) -> webdriver.Chrome:
        # , proxy=self.proxy)
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=self.options)
    
    # -------------------------- quicker browser actions ------------------------- #

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

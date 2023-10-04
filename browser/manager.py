from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, Popularity, HardwareType
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service


class Browser():

    # -------------------------------- constructor ------------------------------- #

    def __init__(self):

        # ---------------------------------- options --------------------------------- #
        # create options
        self.options = Options()

        # add headless mode
        # self.options.add_argument('--headless')

        # -------------------------------- user agent -------------------------------- #
        # create user agent rotator
        self.user_agent_rotator = UserAgent()

        # set user agent parameters -> software_names, operating_systems, popularity, hardware_type
        self.software_names = [SoftwareName.CHROME.value]
        self.operating_systems = [OperatingSystem.WINDOWS.value]
        self.popularity = [Popularity.POPULAR.value]
        self.hardware_type = [HardwareType.COMPUTER.value]

        # get random user agent
        self.random_user_agent = self.get_random_user_agent()

        # add user agent to options
        self.options.add_argument(f'user-agent={self.random_user_agent}')
        self.options.add_argument("--start-maximized")

        # ----------------------------------- proxy ---------------------------------- #
        # self.proxy_server = self.create_proxy_server()
        # self.proxy = self.proxy_server.create_proxy()
        # self.options.add_argument(f'--proxy-server={self.proxy.proxy}')

        # ---------------------------------- driver ---------------------------------- #
        # create browser -> autoinstalled chrome
        # self.driver = self.create_driver()

    # ---------------------------------- methods --------------------------------- #

    def get_random_user_agent(self) -> str:
        user_agent_rotator = UserAgent(
            software_names=self.software_names,
            operating_systems=self.operating_systems,
            popularity=self.popularity,
            limit=100
        )
        return user_agent_rotator.get_random_user_agent()
    
    # change user agent
    def change_user_agent(self):
        self.random_user_agent = self.get_random_user_agent()
        self.options.add_argument(f'user-agent={self.random_user_agent}')
        self.driver = self.create_driver()

    def create_driver(self) -> webdriver.Chrome:
        # , proxy=self.proxy)
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=self.options)
    
    # add options
    def add_options(self, options: Options):
        self.options.add_argument(options)

# create global variable -> global_browser
global_browser = Browser().create_driver()
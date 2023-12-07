# import browser_actions
from browser.actions import BrowserActions

# import database queries
from data.database import database_manager

# import mail verification
from verification.mail import MailManager

# import phone verification
from verification.phone import PhoneManager

# import scraper
from scraper import Scraper

# import browser
from browser import MyBrowser

# import real info
from data.real_info import RealInfoManager

class AccountCreator:
    def __init__(self):
        self.scraper = Scraper()
        self.browser = MyBrowser()
        self.browser_actions = BrowserActions(self.browser)
        self.database_manager = database_manager
        self.mail_manager = MailManager()
        self.phone_api = PhoneManager()
        self.real_info_manager = RealInfoManager()


        # ---
        self.person = self.scraper.create_person()
        self.mail_address = self.create_mail_address()
        self.password = self.real_info_manager.get_random_password()
        self.user_agent = self.real_info_manager.get_random_user_agent()
    
    # create mail address
    def create_mail_address(self):
        return self.mail_manager.create_mail_address(
            username=f'{self.person.name.first}.{self.person.name.last}'
        )

    # if other function is called raise NotImplementedError
    def create_account(self, account):
        raise NotImplementedError
    
    def login(self, account):
        raise NotImplementedError
    

    
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
    """
    Manages the creation of accounts using various verification methods and real/fake personal information.
    """
    def __init__(self):
        """
        Initializes the AccountCreator with necessary managers and actions.
        """
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
        """
        Creates a mail address using the MailManager.
        
        Returns:
            str: The created mail address.
        """
        
        try:
            return self.mail_manager.create_mail_address(
            username=f'{self.person.name.first}.{self.person.name.last}'
        )
        
        except Exception as e:
            print(f"Failed to create mail address: {e}")
            return None

    # if other function is called raise NotImplementedError
    def create_account(self, account):
        """
        Creates an account on the specified platform using the generated credentials.
        
        Args:
            account (str): The platform for which to create an account.
        
        Raises:
            NotImplementedError: Indicates the method needs to be implemented.
        """
        raise NotImplementedError
    
    def login(self, account):
        raise NotImplementedError
    

    

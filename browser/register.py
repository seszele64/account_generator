# registering at a site, given xpath fields and their respective values

from dataclasses import dataclass

@dataclass
class Buttons:
    submit: str = None

@dataclass
class Selectors:
    country_selector: str = None
    country_option: str = None
    
    # phone
    phone_code_selector: str = None
    phone_code_option: str = None # <option value="AC">AC +247</option>

@dataclass
class Xpaths:
    country: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    password: str = None
    password_confirm: str = None
    referral_code: str = None
    buttons: Buttons = None
    selectors: Selectors = None

@dataclass
class Values(Xpaths):
    pass

class RegisterSite:

    def __init__(self, xpaths: Xpaths):
        self.xpaths = xpaths
        self.values = {}

    
class WoltRegister(RegisterSite):

    def __init__(self, xpaths: Xpaths):
        super().__init__(xpaths)

    def register(self, driver, first_name, last_name, email, password, country):
        pass

wolt = WoltRegister(
    Xpaths(
        first_name = '//*[@id="create-account-first-name"]',
        last_name = '//*[@id="create-account-last-name"]',
        email = '//*[@id="email"]',
        phone = '//*[@id="create-account-phone-number"]',
        buttons = Buttons(
            submit = '//*[@id="register-form"]/div[6]/button',
        ),
        selectors = Selectors(
            country_selector = '/html/body/div[6]/div/aside/div[2]/div/div[1]/div/div/form/div[2]/label/select',
            # options are given as <option value="COUNTRY_CODE">COUNTRY_NAME</option> in html, under select tag
            country_option = '/html/body/div[6]/div/aside/div[2]/div/div[1]/div/div/form/div[2]/label/select/option[{}]',
            phone_code_selector='/html/body/div[6]/div/aside/div[2]/div/div[1]/div/div/form/div[4]/div[1]/label/select',
            # example: <option value="AC">AC +247</option>
            phone_code_option='/html/body/div[6]/div/aside/div[2]/div/div[1]/div/div/form/div[4]/div[1]/label/select/option[{}]',
        ),
        referral_code='//*[@id="create-account-referral-code"]',
    )
)
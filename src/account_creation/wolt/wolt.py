from ..account_creator import AccountCreator


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

# from browser import BrowserActions
from browser import MyBrowser

class WoltAccountCreate:

    def __init__(self, browser: MyBrowser):
        self.browser = browser
        
        self.visit_page_url = "https://wolt.com/en/"
        self.button1_locator = (By.XPATH, "/html/body/div[6]/div/div/div/button[2]/div[3]")
        self.button2_locator = (By.XPATH, "/html/body/div[2]/div[2]/div/header/div[2]/div[3]/div/div/button")
        self.input_email_locator = (By.XPATH, "//*[@id='method-select-email']")
        self.click_next_button_locator1 = (By.XPATH, "/html/body/div[7]/div/aside/div[2]/div/div[1]/div/div/div[2]/form/button")
        self.click_next_button_locator2 = (By.XPATH, "/html/body/div[8]/div/aside/div[2]/div/div[1]/div/div/div[2]/form/button")

        # error 
        # self.error_field_locator = (By.XPATH, "/html/body/div[7]/div/aside/div[2]/div/div[1]/div/div/div[2]/form/div[2]/div")
        self.error_field_locator = (By.CSS_SELECTOR, 'div[data-test-id="MethodSelect.EmailLoginError"]')
        self.resend_mail_locator = (By.CSS_SELECTOR, "button[data-test-id='EmailSent.Resend']")

    def visit_page(self):
        self.browser.navigate(self.visit_page_url)

    def click_button1(self):
        self.browser.click(self.button1_locator)

    def click_button2(self):
        self.browser.click(self.button2_locator)

    def input_email(self, email):
        from selenium.webdriver.common.keys import Keys
        element = self.browser.driver.find_element(*self.input_email_locator)
        self.browser.input_text(self.input_email_locator, email)
        element.send_keys(Keys.ENTER)

    def await_error(self, timeout=5):
        try:
            # If the error element is found within the timeout, return True
            if self.browser.wait_for_element(self.error_field_locator, timeout):
                return True
        except TimeoutException:
            # If the error element is not found within the timeout, return False
            return False
        return False


    def wait_for_button_resend_mail(self, timeout=30):
        self.browser.wait_for_element(self.resend_mail_locator, timeout)

    def click_resend_mail(self):
        self.browser.click(self.resend_mail_locator)


class WoltAccountRegister:

    def __init__(self, browser: MyBrowser):
        self.browser = browser
        
        self.visit_page_url = "https://wolt.com/en/"
        self.button1_locator = (By.XPATH, "/html/body/div[5]/div/div/div/button[2]/div[3]")
        self.button2_locator = (By.XPATH, "/html/body/div[2]/div[2]/div/header/div[2]/div[3]/div/div/button")
        self.input_email_locator = (By.XPATH, "//*[@id='method-select-email']")
        self.click_next_button_locator = (By.XPATH, "/html/body/div[7]/div/aside/div[2]/div/div[1]/div/div/div[2]/form/button")
        # error 
        # self.error_field_locator = (By.XPATH, "/html/body/div[7]/div/aside/div[2]/div/div[1]/div/div/div[2]/form/div[2]/div")
        self.error_field_locator = (By.CSS_SELECTOR, 'div[data-test-id="MethodSelect.EmailLoginError"]')
        self.resend_mail_locator = (By.CSS_SELECTOR, "button[data-test-id='EmailSent.Resend']")

    def visit_page(self, url):
        self.browser.navigate(url)

    def click_confirm_cookies(self):
        self.browser.click(self.confirm_cookies_button_selector)

    def click_confirm_not_bot(self):
        self.browser.click(self.confirm_not_bot_selector)

    def wait_for_modal(self):
        self.browser.wait_for_element(self.modal_selector, 5)
    
    def select_country(self, country):
        self.browser.select_dropdown_option(self.select_country_selector, value=country)

    def input_first_name(self, first_name):
        self.browser.input_text(self.first_name_input_selector, first_name)

    def input_last_name(self, last_name):
        self.browser.input_text(self.last_name_input_selector, last_name)

    def select_country_code(self, country_code):
        self.browser_actionsself.browser_actions.select_dropdown_option(self.select_country_code_selector, value=country_code)

    def input_phone_number(self, phone_number):
        self.browser.input_text(self.input_phone_number_selector, phone_number)

    def input_referral_code(self, referral_code):
        self.browser.input_text(self.input_referral_code_selector, referral_code)

    # def click_personal_data_consent(self):
    #     self.click(self.personal_data_consent_selector)
    def click_intercepting_element(self, element):
        # move to element
        ActionChains(self.driver).move_to_element(element).click_and_hold().release().perform()

    def click_all_consents(self):
        elements = self.driver.find_elements(*self.consents_selector)
        for element in elements:
            try:
                self.click_intercepting_element(element)
            except Exception as e:
                print(f'Failed to click on intercepting element due to: {e}')

    def click_continue_button(self):
        self.browser.click(self.continue_button_selector)

    def check_for_error(self, timeout=5):
        try:
            # Locate the error element by its data-test-id attribute
            error_element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.error_field_locator)))

            if error_element is not None:
                print("Error appeared, check error message on the page")
                return True

            # # If the element is found and it's visible (displayed), then the error is present
            # if error_element.is_displayed():
            #     # You can also retrieve the error message text if needed
            #     print(error_element)
            #     # if message is not None:
            #     if (error_message := error_element.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(1)").text) is not None:
            #         print(f"Error appeared: {error_message}")
            #         raise ValueError(error_message)
            #     print("Error appeared, check error message on the page")
            #     return True
        except:
            # No error
            return False

        return False
    
    def wait_for_verification_code_modal(self):
        self.browser.wait_for_element(self.modal_selector, 5)


class Wolt(AccountCreator):

    def __init__(self):

        # init super
        super().__init__()
        self.account_create = WoltAccountCreate(self.browser)
        self.account_register = WoltAccountRegister(self.browser)


    def create_account(self):

        # visit page
        self.account_create.visit_page()
        # click button 1
        self.account_create.click_button1()
        # click button 2
        self.account_create.click_button2()
        # input email
        self.account_create.input_email(self.mail_address)
        # click next button
        # self.account_create.click_next_button()
        # await error
        if self.account_create.await_error():
            print("Error appeared, check error message on the page")
            raise ValueError("Error appeared, check error message on the page")
        # wait for button resend mail
        self.account_create.wait_for_button_resend_mail()
        # click resend mail
        self.account_create.click_resend_mail()

        # add to database
        self.database_manager.insert_generated_data(
            person=self.person,
            email=self.mail_address,
            password=self.password,
            user_agent=self.user_agent
        )



    def register(self, account):
        # visit page
        self.account_register.visit_page(account.url)
        # click confirm cookies
        # self.account_register.click_confirm_cookies()
        # click confirm not bot
        # self.account_register.click_confirm_not_bot()
        # wait for modal
        # self.account_register.wait_for_modal()
        # select country
        # self.account_register.select_country(account.country)
        # input first name
        # self.account_register.input_first_name(account.first_name)
        # input last name
        # self.account_register.input_last_name(account.last_name)
        # select country code
        # self.account_register.select_country_code(account.country_code)
        # input phone number
        # self.account_register.input_phone_number(account.phone_number)
        # input referral code
        # self.account_register.input_referral_code(account.referral_code)
        # click all consents
        # self.account_register.click_all_consents()
        # click continue button
        # self.account_register.click_continue_button()
        # check for error
        # if self.account_register.check_for_error():
        #     print("Error appeared, check error message on the page")
        #     raise ValueError("Error appeared, check error message on the page")
        # wait for verification code modal
        # self.account_register.wait_for_verification_code_modal()
        # input verification code
        # self.account_register.input_verification_code(account.verification_code)
        # click verify button
        # self.account_register.click_verify_button()
        # check for error
        # if self.account_register.check_for_error():
        #     print("Error appeared, check error message on the page")
        #     raise ValueError("Error appeared, check error message on the page")
        # add to database
        # self.account_register.add_to_database(account)
        pass

    def login(self, account):
        pass

    
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

from website_actions.base import BaseService

import sys
import time

sys.path.append(".")

from browser.actions import BrowserActions
from browser.manager import MyBrowser

class CreateAccount(BrowserActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.visit_page_url = "https://wolt.com/en/"
        self.button1_locator = (By.XPATH, "/html/body/div[5]/div/div/div/button[2]/div[3]")
        self.button2_locator = (By.XPATH, "/html/body/div[2]/div[2]/div/header/div[2]/div[3]/div/div/button")
        self.input_email_locator = (By.XPATH, "//*[@id='method-select-email']")
        self.click_next_button_locator = (By.XPATH, "/html/body/div[7]/div/aside/div[2]/div/div[1]/div/div/div[2]/form/button")
        # error 
        # self.error_field_locator = (By.XPATH, "/html/body/div[7]/div/aside/div[2]/div/div[1]/div/div/div[2]/form/div[2]/div")
        self.error_field_locator = (By.CSS_SELECTOR, 'div[data-test-id="MethodSelect.EmailLoginError"]')
        self.resend_mail_locator = (By.CSS_SELECTOR, "button[data-test-id='EmailSent.Resend']")

    def visit_page(self):
        self.navigate(self.visit_page_url)

    def click_button1(self):
        self.click(self.button1_locator)

    def click_button2(self):
        self.click(self.button2_locator)

    def input_email(self, email):
        self.input_text(self.input_email_locator, email)

    def click_next_button(self):
        self.wait_for_element(self.click_next_button_locator)
        self.click(self.click_next_button_locator)

    def await_error(self, timeout=5):
        try:
            # If the error element is found within the timeout, return True
            if self.wait_for_element(self.error_field_locator, timeout):
                return True
        except TimeoutException:
            # If the error element is not found within the timeout, return False
            return False
        return False


    def wait_for_button_resend_mail(self, timeout=30):
        self.wait_for_element(self.resend_mail_locator, timeout)

    def click_resend_mail(self):
        self.click(self.resend_mail_locator)

class RegisterAccount(BrowserActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.confirm_cookies_button_selector = (By.XPATH, '/html/body/div[5]/div/div/div/button[2]')
        self.confirm_not_bot_selector = (By.XPATH, "//*[@id='mainContent']/div/button")

        # div role = "dialog"
        self.modal_selector = (By.CSS_SELECTOR, 'div[role="dialog"]')

        # self.select_country_selector = (By.XPATH, "/html/body/div[6]/div/aside/div[2]/div/div[1]/div/div/form/div[2]/label/select")
        self.select_country_selector = (By.CSS_SELECTOR, 'select[name="country"][data-test-id="CreateAccount.Country"]')
        self.first_name_input_selector = (By.XPATH, "//*[@id='create-account-first-name']")
        self.last_name_input_selector = (By.XPATH, "//*[@id='create-account-last-name']")
        self.select_country_code_selector = (By.CSS_SELECTOR, 'select[data-test-id="CreateAccount.PhoneNumberCountryCode"][name="phoneNumberCountryCode"]')
        self.input_phone_number_selector = (By.XPATH, "//*[@id='create-account-phone-number']")
        self.input_referral_code_selector = (By.XPATH, "//*[@id='create-account-referral-code']")
        
        # consents
        self.consents_selector = (By.CSS_SELECTOR, '[data-test-id^="CreateAccount.Consent"]')
        self.continue_button_selector = (By.CSS_SELECTOR, 'button[data-test-id="CreateAccount.Continue"]')
        self.error_field_locator = (By.CSS_SELECTOR, 'div[data-test-id="CreateAccount.SubmitError"]')
        self.confirm_sms_modal_selector = (By.CSS_SELECTOR, 'div[data-test-id="VerifyCode.CodeNotReceived"]')
    
    def visit_page(self, url):
        self.navigate(url)

    def click_confirm_cookies(self):
        self.click(self.confirm_cookies_button_selector)

    def click_confirm_not_bot(self):
        self.click(self.confirm_not_bot_selector)

    def wait_for_modal(self):
        self.wait_for_element(self.modal_selector, 5)
    
    def select_country(self, country):
        self.select_dropdown_option(self.select_country_selector, value=country)

    def input_first_name(self, first_name):
        self.input_text(self.first_name_input_selector, first_name)

    def input_last_name(self, last_name):
        self.input_text(self.last_name_input_selector, last_name)

    def select_country_code(self, country_code):
        self.select_dropdown_option(self.select_country_code_selector, value=country_code)

    def input_phone_number(self, phone_number):
        self.input_text(self.input_phone_number_selector, phone_number)

    def input_referral_code(self, referral_code):
        self.input_text(self.input_referral_code_selector, referral_code)

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
        self.click(self.continue_button_selector)

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
        self.wait_for_element(self.modal_selector, 5)

  
class Wolt(BaseService):

    def __init__(self, driver: MyBrowser = None, **kwargs):
        self.driver = driver
        
    def create_account(self, email):
        account_creation = CreateAccount(self.driver)
        account_creation.visit_page()
        account_creation.click_button1()
        account_creation.click_button2()
        account_creation.input_email(email)
        account_creation.click_next_button()
        if account_creation.await_error():
            raise ValueError("Error while creating account")
        account_creation.wait_for_button_resend_mail()
        account_creation.click_resend_mail()
        time.sleep(2)

        # verify email
        


    def register(self, url, country, first_name, last_name, country_code, phone_number, referral_code=""):
        account_registration = RegisterAccount(self.driver)
        account_registration.visit_page(url)
        account_registration.click_confirm_cookies()
        account_registration.click_confirm_not_bot()
        # wait for site to load fully
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
        account_registration.select_country(country)
        account_registration.input_first_name(first_name)
        account_registration.input_last_name(last_name)
        account_registration.select_country_code(country_code)
        account_registration.input_phone_number(phone_number)
        # account_registration.input_referral_code(referral_code)

        # account_registration.click_personal_data_consent()
        account_registration.click_all_consents()
        account_registration.click_continue_button()
        if account_registration.check_for_error():
            raise ValueError("Error while registering account")
        
        # wait for confirmation to appear
        account_registration.wait_for_verification_code_modal()


# # Usage:
# def test_create_account():
#     driver = MyBrowser().create_driver()
#     wolt = Wolt(driver)
#     wolt.create_account("test@maddafaka.com")
#     driver.quit()

# def test_register_account():
#     driver = MyBrowser().create_driver()
#     wolt = Wolt(driver)
#     wolt.register(
#         url = 'https://wolt.com/me/magic_login?email=m---%40sake.prout.be&email_hash=3ehGzx9hNwMb1ar4l_uYh9lPHnmJFfiyvJ9KIgzTsJM&token=-8Zp3xnggzB8ulG9UQ2UMaoZd1ftHtmIXY54qrC_jEY&new_user=true&attribution=%3Ab5f86f6c-626c-46b3-affb-df3ac0f09cf1%3A',
#         country="POL",
#         first_name="John",
#         last_name="Doe",
#         country_code="PL",
#         phone_number="520830290"
#     )

#     driver.quit()

# test_register_account()
# register at a site for given service
from abc import ABC, abstractmethod
# import from ./mail/main.py
from mail.links import (VerificationMail, VERIFICATION_SERVICES)

class WoltVerificationMail(VerificationMail):

    def __init__(self, mail_html):
        super().__init__(mail_html)

    def find_verification_link(self) -> str:
        # Define the regex pattern specific to Wolt emails
        regex_pattern = r'https://wolt.com/me/magic_login[^"]*'
        return super().find_verification_link(regex_pattern)

# add new service to VERIFICATION_SERVICES
VERIFICATION_SERVICES.Wolt = WoltVerificationMail

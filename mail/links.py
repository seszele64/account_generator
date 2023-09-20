
import requests
import json

# from mail import Mail
# from yopmail import YopmailHTML
from bs4 import BeautifulSoup

import re

class Mail:

    def __init__(self, mail):
        self.html = mail.html

    def find_link(self, regex_pattern: re.Pattern) -> str:
        import re
        for line in self.html.splitlines():
            # find link that begins with 'regex_pattern' and until the next "
            if match := re.search(regex_pattern, line):
                return match.group(0)
        return None

class ServiceRegex:
    def __init__(self, verification_regex: re.Pattern, login_regex: re.Pattern):
        self.verification_link = verification_regex
        self.login_link = login_regex

class Service(
    ServiceRegex
):

    def __init__(self, service_name: str, service_regex: ServiceRegex):
        self.name = service_name
        self.regex = ServiceRegex(*service_regex)

    def get_verification_link(self, mail: Mail) -> str:
        return Mail(mail).find_link(self.regex.verification_link)

    def get_login_link(self, mail: Mail) -> str:
        return mail.find_link(self.regex.login_link)
    

class ServiceRegistry:
    _services = {}  # Dictionary to store service objects

    @classmethod
    def register_service(cls, name, service_regex):
        cls._services[name] = Service(name, service_regex)

    @classmethod
    def get_service(cls, name):
        return cls._services.get(name)

# register new service
ServiceRegistry.register_service('wolt', (r'https://wolt.com/me/magic_login[^"]*', r'https://wolt.com/me/magic_login[^"]*'))





    
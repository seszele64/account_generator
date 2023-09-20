
import re
from dataclasses import dataclass
# datetime
from datetime import datetime

class Address:
    def __init__(self, street_name: str, street_number: str, zip_code: str, city: str):
        self.street_name = street_name
        self.street_number = street_number
        self.zip_code = zip_code
        self.city = city


class Name:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Company:
    def __init__(self, name: str, occupation: str):
        self.name = name
        self.occupation = occupation


class Contact:
    def __init__(self, phone: str, email: str):
        self.phone = phone
        self.email = email


class Person:
    def __init__(self, name: Name, birthdate: datetime, company: Company, contact: Contact, address: Address):
        self.name = name
        self.birthdate = birthdate
        self.company = company
        self.contact = contact
        self.address = address

    def __str__(self) -> str:
        return f'''Person(
    name=Name('{self.name.first_name}', '{self.name.last_name}'),
    birthdate=Birthdate('{self.birthdate}'),
    company=Company('{self.company.name}', '{self.company.occupation}'),
    contact=Contact('{self.contact.phone}', '{self.contact.email}'),
    address=Address('{self.address.street_name}', '{self.address.street_number}', '{self.address.zip_code}', '{self.address.city}')
    )'''


class AddressRegex:
    def __init__(self, street_name: re.Pattern, street_number: re.Pattern, zip_code: re.Pattern, city: re.Pattern):
        self.street_name = street_name
        self.street_number = street_number
        self.zip_code = zip_code
        self.city = city

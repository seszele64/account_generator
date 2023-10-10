
import re
from dataclasses import dataclass
# datetime
from datetime import datetime
from typing import Any
from fng_api import *
import pycountry

# ----------------------- sub constituents of a person ----------------------- #

class Street:

    def __init__(self, data):
        self.data = data
        self.name, self.number = self.parse_address()

    def parse_address(self) -> 'Street':
        # street number
        street_number_pattern = r'(\d+)\s+'
        # street name
        street_name_pattern = r'\d+\s+(.+?),'
        street_name = re.search(street_name_pattern, self.data).group(1)
        street_number = re.search(street_number_pattern, self.data).group(1)
        return street_name, street_number

class Address:
    def __init__(self, street: Street, zip_code: str, city: str):
        
        self.street = self.parse_street(street)
        self.zip_code = zip_code
        self.city = city

    def parse_street(self, street: str) -> 'Street':
        return Street(street)
    
    def __str__(self) -> str:
        print(f"Address(street={self.street}, zip_code={self.zip_code}, city={self.city})")

class Name:

    def __init__(self, data: str):
        self.data = data
        self.first, self.last = self.parse()

    def parse(self):
        # parse Word + space + Word to two words
        # find first word -> before space
        first_name_pattern = r'(.+)\s'
        first_name = re.search(first_name_pattern, self.data).group(1)

        # find last word -> after space
        last_name_pattern = r'\s(.+)'
        last_name = re.search(last_name_pattern, self.data).group(1)

        return first_name, last_name


class Company:
    def __init__(self, name: str = None, occupation: str = None):
        self.name = name
        self.occupation = occupation

class Contact:
    def __init__(self, phone: str = None, email: str = None):
        self.phone = phone
        self.email = email

# ------------------------------------- < ------------------------------------ #


class Person:
    def __init__(self, name: Name = None, birthdate: datetime = None, company: Company = None, contact: Contact = None, address: Address = None):
        self.name = name
        self.birthdate = birthdate
        self.company = company
        self.contact = contact
        self.address = address

    def from_random_data(self, identity: getIdentity) -> 'Person':
        """
        Parses random data from the provided identity and address regex and returns a Person object.

        Args:
            identity (getIdentity.identity): The identity object containing random data.
            address_regex (Address.AddressRegex): The address regex object for parsing the address.

        Returns:
            Person: A Person object with parsed random information.
                - name (Name): The parsed Name object.
                - birthdate (datetime): The parsed birthdate.
                - company (Company): The parsed Company object.
                - contact (Contact): The parsed Contact object.
                - address (Address): The parsed Address object.

        Example:
            ```python
            identity = getIdentity.identity(...)
            address_regex = Address.AddressRegex(...)
            parse_random_data(identity, address_regex)
            ```
        """
        return Person(
            name=Name(identity.name),
            birthdate=datetime.strptime(identity.birthday, '%B %d, %Y'),
            company=Company(identity.company, identity.occupation),
            contact=Contact(identity.phone, identity.email),
            address=Address(identity.address, identity.zip, identity.city)
        )

    def __str__(self) -> str:
        return f'''Person(
    name=Name('{self.name.first}', '{self.name.last}'),
    birthdate=Birthdate('{self.birthdate}'),
    company=Company('{self.company.name}', '{self.company.occupation}'),
    contact=Contact('{self.contact.phone}', '{self.contact.email}'),
    address=Address('{self.address.street.name}', '{self.address.street.number}', '{self.address.zip_code}', '{self.address.city}')
    )'''

# ------------------------------- create person ------------------------------ #


def get_country_list() -> list:

    """
    Returns a list of country codes.

    Returns:
        list: A list of country codes.

    Example:
        ```python
        get_country_list()
        ```
    """
    return [country.lower() for country in {country.alpha_2 for country in pycountry.countries}]

# create person
def create_person(country_list: list = None) -> Person:

    """
    Creates a Person object with random information based on the provided country list.

    Args:
        country_list (list, optional): A list of country codes. Value defaults to None, but if not provided, the default country is Poland.

    Returns:
        - Person: A Person object with random information
            - name(first_name, last_name): Name object with random first and last name
            - birthdate: datetime object with random birthdate
            - company(name, occupation): Company object with random name and occupation
            - contact(phone, email): Contact object with random phone and email
            - address(street, zip_code, city): Address object with random street, zip code and city

    Example:
        ```python
        create_person(['pl', 'us'])
        ```
    """
    
    if country_list is None:
        country_list = ['pl']
    if not isinstance(country_list, list):
        raise TypeError(f"country_list must be of type list, not {type(country_list)}")
    # check if countries in country_list belong in pycountry
    for country in country_list:
        if country not in get_country_list():
            raise ValueError(f"Invalid country: {country}")

    return Person().from_random_data(getIdentity(country_list))

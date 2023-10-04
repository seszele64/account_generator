
import re
from dataclasses import dataclass
# datetime
from datetime import datetime
from fng_api import *
import pycountry


countries = {country.alpha_2 for country in pycountry.countries}

class Street:
    name: str = None
    number: str = None

    def __init__(self, name: str = None, number: str = None):
        self.name = name
        self.number = number

    def parse_address(self) -> tuple:
        pattern = r'^(\d+)\s+(.+)'
        if not (match := re.match(pattern, self)):
            raise ValueError(f'Invalid address: {self}')
        street_number = match[1]
        street_name = match[2]
        return Street(street_name, street_number)

class Address:
    def __init__(self, street: Street, zip_code: str, city: str):
        self.street = street
        self.zip_code = zip_code
        self.city = city

    class AddressRegex:
        def __init__(self, street_name: re.Pattern, street_number: re.Pattern, zip_code: re.Pattern, city: re.Pattern):
            self.street_name = street_name
            self.street_number = street_number
            self.zip_code = zip_code
            self.city = city


    def parse(self, address_regex: 'AddressRegex') -> 'Address':
        return Address(
            street=Street(
                name=address_regex.street_name.search(self.street.name).group(),
                number=address_regex.street_number.search(self.street.number).group()
            ),
            zip_code=address_regex.zip_code.search(self.zip_code).group(),
            city=address_regex.city.search(self.city).group()
        )

class Name:
    def __init__(self, first_name: str = None, last_name: str = None):
        self.first_name = first_name
        self.last_name = last_name

    def parse(self, name: str) -> 'Name':
        pattern = r'^(\w+) (\w+)$'
        if not (match := re.match(pattern, name)):
            raise ValueError(f'Invalid name: {name}')
        first_name, last_name = match[1], match[2]
        return Name(first_name, last_name)

class Company:
    def __init__(self, name: str = None, occupation: str = None):
        self.name = name
        self.occupation = occupation

class Contact:
    def __init__(self, phone: str = None, email: str = None):
        self.phone = phone
        self.email = email

class Person:
    def __init__(self, name: Name = None, birthdate: datetime = None, company: Company = None, contact: Contact = None, address: Address = None):
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

# ------------------------------- create person ------------------------------ #

def parse_random_data(identity: getIdentity.identity,
                      address_regex: 'Address.AddressRegex') -> Person:
    
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
        name=Name.parse(identity.name),
        birthdate=datetime.strptime(identity.birthday, '%B %d, %Y'),
        company=Company(identity.company, identity.occupation),
        contact=Contact(identity.phone, identity.email),
        address=Address.parse(address_regex),
    )

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

    # Identity
    identity = getIdentity(country_list)

    # Address
    addres_regex = Address.AddressRegex(
        street_name = re.compile(r'(.+)'),
        street_number = re.compile(r'(\d+)'),
        zip_code = re.compile(r'(\d+)'),
        city = re.compile(r'(.+)'),
    )

    return parse_random_data(identity, addres_regex)

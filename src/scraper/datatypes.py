
import re
from datetime import datetime
from fng_api import *

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

    def from_fake_data(self, identity: getIdentity) -> 'Person':
        """
        Parses fake data from the provided identity and address regex and returns a Person object.

        Args:
            identity (getIdentity.identity): The identity object containing fake data.
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



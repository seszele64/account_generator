# pip install fng-api
from .datatypes import Person, Address, Name, Company, Contact
import re
from .info_parser import parse_address, parse_name
from datetime import datetime

# create api
from fng_api import *


def get_random_person(identity: Identity):

    # Person
    person = Person(
        name=Name(
            first_name = parse_name(identity.name)[0],
            last_name = parse_name(identity.name)[1],
        ),
        birthdate=datetime.strptime(identity.birthday, '%B %d, %Y'),
        company=Company(
            name = identity.company,
            occupation = identity.occupation,
        ),
        contact=Contact(
            phone = identity.phone,
            email = identity.email,
        ),
        address=Address(
            street_name = parse_address(identity.street)[0],
            street_number = parse_address(identity.street)[1],
            zip_code = identity.zip,
            city = identity.city,
        )
    )

    return person
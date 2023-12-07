
# enum for the services
from enum import Enum

import re

# create enums for regex patterns of the services

class Wolt(Enum):
    """
    A class representing a regex pattern for Wolt.
    """
    verification: re.Pattern = r'https:\/\/wolt\.com\/me\/magic_login\?email=[^"\s]+'
    login: re.Pattern = r'https:\/\/wolt\.com\/me\/magic_login\?email=[^"\s]+'


class UberEats(Enum):
    """
    A class representing a regex pattern for UberEats.
    """
    verification: re.Pattern = r'https:\/\/www\.ubereats\.com\/en-US\/signup\/[^"\s]+'
    login: re.Pattern = r'https:\/\/www\.ubereats\.com\/en-US\/signup\/[^"\s]+'


# add all the services here
class ServiceLinksEnum(Enum):
    """
    A class representing a service.
    """
    WOLT = Wolt
    UBEREATS = UberEats

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)

    @classmethod
    def get_service(cls, service_name: str):
        if service_name.upper() not in cls.__members__:
            raise ValueError(f"Service {service_name} is not supported.")
        return cls[service_name.upper()].value
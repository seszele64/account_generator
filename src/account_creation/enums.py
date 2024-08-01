from enum import Enum

from .wolt import Wolt

class AccountSite(Enum):
    """
    Defines the supported sites for account creation.
    """
    Wolt = Wolt
    # Additional sites can be added as the project expands.

# imports
from .api import get_random_person
from fng_api import *

# create person
def create_person():
    country_list = ['pl']
    identity = getIdentity(country_list)
    return get_random_person(identity)
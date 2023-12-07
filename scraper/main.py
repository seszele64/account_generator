import pycountry
from fng_api import *
from .datatypes import *

class Scraper:
    def __init__(self, country_list=None):
        if country_list is None:
            country_list = ['pl']
        if not isinstance(country_list, list):
            raise TypeError(f"country_list must be of type list, not {type(country_list)}")
        # check if countries in country_list belong in pycountry
        for country in country_list:
            if country not in self.get_country_list():
                raise ValueError(f"Invalid country: {country}")
        self.country_list = country_list

    def get_country_list(self):
        """
        Returns a list of country codes.

        Returns:
            list: A list of country codes.
        """
        return [country.lower() for country in {country.alpha_2 for country in pycountry.countries}]

    def create_person(self):
        """
        Creates a Person object with random information based on the provided country list.

        Returns:
            - Person: A Person object with random information
                - name(first_name, last_name): Name object with random first and last name
                - birthdate: datetime object with random birthdate
                - company(name, occupation): Company object with random name and occupation
                - contact(phone, email): Contact object with random phone and email
                - address(street, zip_code, city): Address object with random street, zip code and city
        """
        return Person().from_fake_data(getIdentity(self.country_list))

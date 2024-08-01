

import difflib
import pycountry

country_codes = [country.alpha_2 for country in pycountry.countries]
country_names = [country.name.lower() for country in pycountry.countries]

class CountrySelector:
    def __init__(self):
        self._selected_country = None

    def set_by_name(self, country_name):
        """Set the selected country by its name."""
        country = pycountry.countries.get(name=country_name)
        if country:
            self._selected_country = country
        else:
            raise ValueError(f"No country found with the name: {country_name}")

    def set_by_alpha_2(self, alpha_2_code):
        """Set the selected country by its 2-letter code."""
        country = pycountry.countries.get(alpha_2=alpha_2_code)
        if country:
            self._selected_country = country
        else:
            raise ValueError(f"No country found with the code: {alpha_2_code}")

    def set_by_alpha_3(self, alpha_3_code):
        """Set the selected country by its 3-letter code."""
        country = pycountry.countries.get(alpha_3=alpha_3_code)
        if country:
            self._selected_country = country
        else:
            raise ValueError(f"No country found with the code: {alpha_3_code}")

    def get_country_code(self):
        """Get the 2-letter code of the selected country in lowercase."""
        if self._selected_country:
            return self._selected_country.alpha_2.lower()
        else:
            raise ValueError("No country has been selected.")

    def search_country(self, query):
        """Search for a country by name and set it as the selected country."""
        countries = list(pycountry.countries.search_fuzzy(query))
        if countries:
            self._selected_country = countries[0]
        else:
            raise ValueError(f"No country found with the query: {query}")



def enter_country():
    """Enter a country and return its 2-letter code in lowercase."""

    # create a country selector
    selector = CountrySelector()

    print("Available countries:")

    country_codes = [country.alpha_2 for country in pycountry.countries]
    country_names = [country.name.lower() for country in pycountry.countries]

    for i, country in enumerate(country_codes):
        print(f"{i+1}. {country} - {pycountry.countries.get(alpha_2=country).name}")

    country_input = input('Enter country id or name: ').lower()

    # if country is a number -> get country from country_codes using index
    if country_input.isdigit():
        index = int(country_input) - 1
        if 0 <= index < len(country_codes):
            return country_codes[index].lower()
        else:
            print("Invalid country id.")
            return enter_country()

    # if country is a string
    elif isinstance(country_input, str):
        # if two letter country code -> search in country_codes
        if len(country_input) == 2:
            try:
                selector.set_by_alpha_2(country_input)
                return selector.get_country_code()
            except ValueError:
                print("Invalid country id.")
                return enter_country()

        # if longer name -> search in country_names
        elif len(country_input) > 2:
            try:
                selector.search_country(country_input)
                return selector.get_country_code()
            except ValueError:
                matches = difflib.get_close_matches(country_input, country_names, n=5)
                if matches:
                    print("Did you mean one of these countries?")
                    for match in matches:
                        print(match)
                    input("Press Enter to continue...")
                    return enter_country()
                else:
                    print("Invalid country name.")
                    return enter_country()
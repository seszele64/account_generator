"""
Module for handling data generation and database operations in the account generator tool.
Provides functions to generate random person data and real data for account creation and verification.
"""

# database
# random_info
import random_info
# real_info
import real_info

from database import *


def random_person_data():
    """
    Generates random person data for account creation.
    
    Returns:
        dict: Random person data.
    """
    # Scrape data
    # url = "YOUR_TARGET_URL"
    countries = ['pl']
    return random_info.create_person(countries)

def real_data():
    """
    Generates real data for account creation, such as user agent and password.
    
    Returns:
        tuple: A tuple containing a user agent string and a password.
    """
    user_agent = real_info.get_random_user_agent()
    password = real_info.get_random_password()
    return user_agent, password



# print(random_person_data())
# print(real_data())

# test
# generated_data_id_as_foreign_key(insert_email_verification_data('dd@gmail.com', 'https://www.google.com', 'pending', '2020-01-01', '2020-01-01'))



# database
# random_info
import random_info
# real_info
import real_info


def random_person_data():
    # Scrape data
    # url = "YOUR_TARGET_
    countries = ['pl']
    return random_info.create_person(countries)

# Real data
def real_data():
    user_agent = real_info.get_random_user_agent()
    password = real_info.get_random_password()
    return user_agent, password



# print(random_person_data())
# print(real_data())

# Database
from database import *

# test
# generated_data_id_as_foreign_key(insert_email_verification_data('dd@gmail.com', 'https://www.google.com', 'pending', '2020-01-01', '2020-01-01'))



from data.database import database_manager

# database_manager.insert_generated_data(
#     first_name='Brandon',
#     last_name='Moe',
#     birthdate='1990-01-01',
#     company_name='Company',
#     occupation='Occupation',
#     phone='12345678',
#     street_name='Street',
#     street_number='1',
#     zip_code='1234',
#     city='City',
#     email="ddd.dd@gov.pl",
#     password='Password',
#     user_agent='User Agent'
# )

# change verification_data_id in account_information table to 1
# database_manager.update_verification_data_id(5, 1)

# get account information where generated_data_id is 1
# account_information = database_manager.session.query(database_manager.AccountInformationPostgreSQL).filter_by(generated_data_id=6).first()
# print(account_information)


# # change generated_data_id in account_information table to 5 for account_id 1
# database_manager.session.query(database_manager.AccountInformationPostgreSQL).filter_by(account_id=1).update({database_manager.AccountInformationPostgreSQL.generated_data_id: 5})
# database_manager.session.commit()


## V2

# create person
from scraper.fake_info.person import create_person

# person = create_person(['pl'])

# # insert person into database
# database_manager.insert_generated_data(
#     person=person,
#     email="dd@gov.pl",
#     password='Password',
#     user_agent='User Agent'
# )

# get account information where generated_data_id is 1
account_information = database_manager.session.query(database_manager.AccountInformationPostgreSQL).first()

# print account information as text
print(account_information.generated_data.first_name)
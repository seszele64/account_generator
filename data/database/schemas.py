from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base class for your database models
BasePostgreSQL = declarative_base()

# top - down


# define table for account information
class AccountInformationPostgreSQL(BasePostgreSQL):
    __tablename__ = 'account_information'
    account_id = Column(Integer, primary_key=True)
    generated_data_id = Column(Integer, ForeignKey('generated_data.id'))
    verification_data_id = Column(Integer, ForeignKey('verification_data.verification_id'))

    # Define relationships
    generated_data = relationship("GeneratedDataPostgreSQL")
    verification_data = relationship("VerificationDataPostgreSQL")


# Define the "generated_data" table for PostgreSQL
class GeneratedDataPostgreSQL(BasePostgreSQL):
    __tablename__ = 'generated_data'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birthdate = Column(Date)
    company_name = Column(String)
    occupation = Column(String)
    phone = Column(String)
    street_name = Column(String)
    street_number = Column(String)
    zip_code = Column(String)
    city = Column(String)

    # other data
    email = Column(String)
    password = Column(String)
    user_agent = Column(String)



# create table for sms verification
class SMSVerificationPostgreSQL(BasePostgreSQL):
    __tablename__ = 'sms_verification'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String)
    verification_code = Column(String)
    status = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)




# create table for email verification
class EmailVerificationPostgreSQL(BasePostgreSQL):
    __tablename__ = 'email_verification'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    verification_link = Column(String)
    status = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)



# Define the "verification_status" table for PostgreSQL
class VerificationDataPostgreSQL(BasePostgreSQL):
    __tablename__ = 'verification_data'

    verification_id = Column(Integer, primary_key=True)
    status = Column(String)

    # ids of the verification services
    sms_verification_id = Column(Integer, ForeignKey('sms_verification.id'))
    email_verification_id = Column(Integer, ForeignKey('email_verification.id'))

    # relationship
    sms_verification = relationship(SMSVerificationPostgreSQL)
    email_verification = relationship(EmailVerificationPostgreSQL)
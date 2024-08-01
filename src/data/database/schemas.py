from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base class for your database models
BasePostgreSQL = declarative_base()

# define table for account information
class AccountInformationPostgreSQL(BasePostgreSQL):

    """
    Represents account information, linking generated data with verification data.
    
    Attributes:
        account_id (int): Unique identifier for the account information record.
        generated_data_id (int): Foreign key referencing GeneratedDataPostgreSQL.id.
        verification_data_id (int): Foreign key referencing VerificationDataPostgreSQL.verification_id.
        
    Relationships:
        generated_data: Relationship to GeneratedDataPostgreSQL model.
        verification_data: Relationship to VerificationDataPostgreSQL model.
    """
    
    __tablename__ = 'account_information'
    account_id = Column(Integer, primary_key=True)
    generated_data_id = Column(Integer, ForeignKey('generated_data.id'))
    verification_data_id = Column(Integer, ForeignKey('verification_data.verification_id'))

    # Define relationships
    generated_data = relationship("GeneratedDataPostgreSQL")
    verification_data = relationship("VerificationDataPostgreSQL")


# Define the "generated_data" table for PostgreSQL
class GeneratedDataPostgreSQL(BasePostgreSQL):
    """
    Stores generated personal and company information for account creation purposes.
    
    Attributes:
        id (int): Unique identifier for the generated data record.
        first_name (str): First name of the individual.
        last_name (str): Last name of the individual.
        birthdate (date): Birthdate of the individual.
        company_name (str): Name of the company.
        occupation (str): Occupation of the individual.
        phone (str): Phone number of the individual.
        street_name (str): Street name part of the address.
        street_number (str): Street number part of the address.
        zip_code (str): ZIP code part of the address.
        city (str): City part of the address.
        email (str): Email address of the individual.
        password (str): Password for account creation.
        user_agent (str): User agent string for browser simulation.
        
    Relationships:
        None defined explicitly, but related through foreign keys in AccountInformationPostgreSQL.
    """

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
    """
    Stores SMS verification details including phone numbers and verification codes.
    
    Attributes:
        id (int): Unique identifier for the SMS verification record.
        phone_number (str): Phone number associated with the verification.
        verification_code (str): Verification code received via SMS.
        status (str): Status of the verification (e.g., pending, verified).
        created_at (date): Timestamp when the record was created.
        updated_at (date): Timestamp when the record was last updated.
        
    Relationships:
        sms_verification: Relationship to VerificationDataPostgreSQL model.
    """

    __tablename__ = 'sms_verification'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String)
    verification_code = Column(String)
    status = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)

# create table for email verification
class EmailVerificationPostgreSQL(BasePostgreSQL):
    """
    Stores email verification details including email addresses and verification links.
    
    Attributes:
        id (int): Unique identifier for the email verification record.
        email (str): Email address associated with the verification.
        verification_link (str): Link sent to the email for verification purposes.
        status (str): Status of the verification (e.g., pending, verified).
        created_at (date): Timestamp when the record was created.
        updated_at (date): Timestamp when the record was last updated.
        
    Relationships:
        email_verification: Relationship to VerificationDataPostgreSQL model.
    """

    __tablename__ = 'email_verification'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    verification_link = Column(String)
    status = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)


# Define the "verification_status" table for PostgreSQL
class VerificationDataPostgreSQL(BasePostgreSQL):
    """
    Aggregates verification details for SMS and email verifications.
    
    Attributes:
        verification_id (int): Unique identifier for the verification data record.
        status (str): Overall status of the verification processes.
        sms_verification_id (int): Foreign key referencing SMSVerificationPostgreSQL.id.
        email_verification_id (int): Foreign key referencing EmailVerificationPostgreSQL.id.
        
    Relationships:
        sms_verification: Relationship to SMSVerificationPostgreSQL model.
        email_verification: Relationship to EmailVerificationPostgreSQL model.
    """

    __tablename__ = 'verification_data'

    verification_id = Column(Integer, primary_key=True)
    status = Column(String)

    # ids of the verification services
    sms_verification_id = Column(Integer, ForeignKey('sms_verification.id'))
    email_verification_id = Column(Integer, ForeignKey('email_verification.id'))

    # relationship
    sms_verification = relationship(SMSVerificationPostgreSQL)
    email_verification = relationship(EmailVerificationPostgreSQL)
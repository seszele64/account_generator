from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base class for your database models
BasePostgreSQL = declarative_base()

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

    # Real data
    email = Column(String)
    password = Column(String)
    user_agent = Column(String)

# Define the "verification_status" table for PostgreSQL
class VerificationStatusPostgreSQL(BasePostgreSQL):
    __tablename__ = 'verification_status'

    id = Column(Integer, primary_key=True)
    phone_verification = Column(String)
    email_verification = Column(String)

# Define the "connection" table to connect "generated_data" and "verification_status" for PostgreSQL
class ConnectionPostgreSQL(BasePostgreSQL):
    __tablename__ = 'connection'

    id = Column(Integer, primary_key=True)
    generated_data_id = Column(Integer, ForeignKey('generated_data.id'))
    verification_status_id = Column(Integer, ForeignKey('verification_status.id'))

    generated_data = relationship('GeneratedDataPostgreSQL', backref='connections')
    verification_status = relationship('VerificationStatusPostgreSQL', backref='connections')
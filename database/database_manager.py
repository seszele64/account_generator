# database_module.py

from sqlalchemy import create_engine
# import /random_info/datatypes.py
from random_info.datatypes import Person

from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()

class Person(Base):
    __tablename__ = 'random_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    birthdate = Column(Date)
    company_name = Column(String)
    company_occupation = Column(String)
    phone = Column(String)
    email = Column(String)
    street_name = Column(String)
    street_number = Column(Integer)
    zip_code = Column(String)
    city = Column(String)

class DatabaseManager:
    def __init__(self, db_path='random_info.db'):
        self.engine = create_engine(f'sqlite:///{db_path}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def insert_person(self, person_data):
        session = self.Session()
        person = Person(**person_data)
        session.add(person)
        session.commit()
        session.close()

    def select_all(self):
        session = self.Session()
        persons = session.query(Person).all()
        for person in persons:
            print(f'ID: {person.id}, First Name: {person.first_name}, Last Name: {person.last_name}')
        session.close()

    def select_by_id(self, id):
        session = self.Session()
        person = session.query(Person).filter_by(id=id).first()
        session.close()
        return person
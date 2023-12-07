import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import text
import datetime

# schemas
from .schemas import BasePostgreSQL, AccountInformationPostgreSQL, GeneratedDataPostgreSQL, SMSVerificationPostgreSQL, EmailVerificationPostgreSQL, VerificationDataPostgreSQL

from sqlalchemy.exc import ProgrammingError


load_dotenv()
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

class Database:
    connections = {}

    @classmethod
    def get_connection(cls, database_name):
        if database_name not in cls.connections:
            conn = psycopg2.connect(database=database_name, user=db_user, password=db_password, host="localhost", port="5432")
            cursor = conn.cursor()
            cls.connections[database_name] = (conn, cursor)
        return cls.connections[database_name]

    @classmethod
    def close_connection(cls, database_name):
        if database_name in cls.connections:
            cls.connections[database_name][0].close()
            del cls.connections[database_name]

    @classmethod
    def execute_query(cls, database_name, query, *args):
        conn, cursor = cls.get_connection(database_name)
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(query, args)

    @classmethod
    def fetch_data(cls, database_name, query, *args):
        conn, cursor = cls.get_connection(database_name)
        with conn:
            with cursor:
                cursor.execute(query, args)
                return cursor.fetchall()
            
    @classmethod
    def get_session(cls, database_name):
        engine = create_engine(f'postgresql://{db_user}:{db_password}@localhost:5432/{database_name}')
        Session = sessionmaker(bind=engine)
        return Session()
        
    # create engine to connect to the database
    @classmethod
    def init_database(cls, database_name):
        # Create the engine to connect to the database
        engine = create_engine(f'postgresql://{db_user}:{db_password}@localhost:5432/{database_name}')

        # Try to create the database tables tables if they don't already exist
        try:
            BasePostgreSQL.metadata.create_all(engine, checkfirst=True)
        except ProgrammingError as e:
            print(f'Error initializing database: {e}')
        except Exception as e:
            print(f'Error: {e}')

class DatabaseManager:

    # import schemas
    AccountInformationPostgreSQL = AccountInformationPostgreSQL
    GeneratedDataPostgreSQL = GeneratedDataPostgreSQL
    SMSVerificationPostgreSQL = SMSVerificationPostgreSQL
    EmailVerificationPostgreSQL = EmailVerificationPostgreSQL
    VerificationDataPostgreSQL = VerificationDataPostgreSQL

    def __init__(self, database_name):
        self.database_name = database_name
        
        # initialize database
        Database.init_database(database_name)
        
        # create session to connect to the database
        self.session = Database.get_session(database_name)

    # add, flush, get id, commit, close session
    def add_flush_get_id_commit_close_session(self, model_class):
        # add
        self.session.add(model_class)
        # flush
        self.session.flush()
        # get id
        id = model_class.id
        # commit
        self.session.commit()
        # close session
        self.session.close()
        # return id
        return id


    # Generated data

    ## Insert
    ### generated data
    def insert_generated_data(self, person, email, password, user_agent):
        generated_data = GeneratedDataPostgreSQL(
            first_name=person.name.first,
            last_name=person.name.last,
            birthdate=person.birthdate,
            company_name=person.company.name,
            occupation=person.company.occupation,
            phone=person.contact.phone,
            street_name=person.address.street.name,
            street_number=person.address.street.number,
            zip_code=person.address.zip_code,
            city=person.address.city,
            email=email,
            password=password,
            user_agent=user_agent
        )

        id = self.add_flush_get_id_commit_close_session(generated_data)

        # insert id into account_information table
        account_information = AccountInformationPostgreSQL(
            generated_data_id=id
        )

        self.session.add(account_information)
        self.session.commit()
        self.session.close()
        


    # Verification data
    ## Insert


    ### EMAIL
    def insert_email_verification_data(self, email, verification_link, status):

        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()

        verification_data = EmailVerificationPostgreSQL(
            email=email,
            verification_link=verification_link,
            status=status,
            created_at=created_at,
            updated_at=updated_at
        )

        verification_data_id = self.add_flush_get_id_commit_close_session(verification_data)

        # add verification_data_id to verification_status table
        self.session.add(VerificationDataPostgreSQL(
            email_verification_id = verification_data_id
        ))
        self.session.commit()
        self.session.close()
    
    ### SMS
    def insert_sms_verification_data(self, phone_number, verification_code, status):

        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()

        verification_data = SMSVerificationPostgreSQL(
            phone_number,
            verification_code,
            status,
            created_at,
            updated_at)
        

        verification_data_id = self.add_flush_get_id_commit_close_session(verification_data)

        # add verification_data_id to verification_status table
        self.session.add(VerificationDataPostgreSQL(
            sms_verification_id = verification_data_id
        ))

        self.session.commit()
        self.session.close()

    
    ## Update

    def update_verification_data(self, verification_data_id, model_class, **kwargs):
        verification_data = self.session.query(model_class).filter_by(id=verification_data_id).first()
        for attr, value in kwargs.items():
            setattr(verification_data, attr, value)
        verification_data.updated_at = datetime.datetime.now()

        self.session.commit()
        self.session.close()

    ### EMAIL
    def update_email_verification_status(self, verification_data_id, status):
        self.update_verification_data(verification_data_id, EmailVerificationPostgreSQL, status=status)

    def update_email_verification_link(self, verification_data_id, verification_link):
        self.update_verification_data(verification_data_id, EmailVerificationPostgreSQL, verification_link=verification_link)


    ### SMS
    def update_sms_verification_status(self, verification_data_id, status):
        self.update_verification_status(verification_data_id, status, SMSVerificationPostgreSQL)

    def update_sms_verification_phone_number(self, verification_data_id, phone_number):
        self.update_verification_data(verification_data_id, SMSVerificationPostgreSQL, phone_number=phone_number)

    def update_sms_verification_verification_code(self, verification_data_id, verification_code):
        self.update_verification_data(verification_data_id, SMSVerificationPostgreSQL, verification_code=verification_code)

    # Account information
    ## Insert
    def insert_account_information(self, account):
        
        query = text("""
        INSERT INTO account_information (generated_data_id, verification_data_id)
        VALUES (:generated_data_id, :verification_data_id)
        """)

        # execute query using plain string
        self.session.execute(query, {
            'generated_data_id': account['generated_data_id'],
            'verification_data_id': account['verification_data_id']
        }).scalar()

        self.session.commit()
        self.session.close()
    
    ## Update
    def update_verification_data_id(self, account_id, verification_data_id):
        query = text("""
        UPDATE account_information
        SET verification_data_id = :verification_data_id
        WHERE account_id = :account_id
        """)

        # execute query using plain string
        self.session.execute(query, {
            'account_id': account_id,
            'verification_data_id': verification_data_id
        })

        self.session.commit()
        self.session.close()
        
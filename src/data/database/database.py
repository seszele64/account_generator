import psycopg2
from psycopg2.errors import ProgrammingError
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from typing import TypeVar, Generic, Type
from sqlalchemy import create_engine
import datetime
from .db_init import BasePostgreSQL  # Import BasePostgreSQL from db_init.py

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

    @classmethod
    def init_database(cls, database_name):
        """
        Initializes the database schema for the given database name.
        Should be called explicitly when there's a need to ensure the database schema exists.
        
        Parameters:
            database_name (str): The name of the database to initialize.
        """

        engine = create_engine(f'postgresql://{db_user}:{db_password}@localhost:5432/{database_name}')
        try:
            BasePostgreSQL.metadata.create_all(engine, checkfirst=True)
        except ProgrammingError as e:
            print(f'Error initializing database: {e}')
        except Exception as e:
            print(f'Error: {e}')

T = TypeVar('T', bound='BasePostgreSQL')

class DatabaseManager(Generic[T]):
    
    def __init__(self, database_name):
        self.database_name = database_name
        self.session = Database.get_session(database_name)
    
    def add_flush_get_id_commit_close_session(self, model_instance: T) -> int:
        self.session.add(model_instance)
        self.session.flush()
        id = model_instance.id
        self.session.commit()
        self.session.close()
        return id
    
    def update_model_instance(self, model_class: Type[T], instance_id: int, **kwargs):
        instance = self.session.query(model_class).filter_by(id=instance_id).first()
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        instance.updated_at = datetime.datetime.now()
        self.session.commit()
        self.session.close()
    
    def query_model_instances(self, model_class: Type[T], **filters) -> list[T]:
        query = self.session.query(model_class).filter_by(**filters)
        instances = query.all()
        self.session.close()
        return instances

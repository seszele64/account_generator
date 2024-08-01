import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError

from .schemas import BasePostgreSQL

load_dotenv()
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

# create engine to connect to the database
def init_database(database_name):
    # Create the engine to connect to the database
    engine = create_engine(f'postgresql://{db_user}:{db_password}@localhost:5432/{database_name}')

    # Try to create the database tables tables if they don't already exist
    try:
        BasePostgreSQL.metadata.create_all(engine, checkfirst=True)
    except ProgrammingError as e:
        print(f'Error initializing database: {e}')
    except Exception as e:
        print(f'Error: {e}')
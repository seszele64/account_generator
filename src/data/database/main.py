# from . import database
# from . import db_init

from .database import DatabaseManager

DATABASE_NAME = 'accountgenerator'

# create database manager
database_manager = DatabaseManager(DATABASE_NAME)
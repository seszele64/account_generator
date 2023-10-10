from . import database
from . import db_init

DATABASE_NAME = 'accountgenerator'

# Initialize the database tables
db_init.init_database(DATABASE_NAME)

# You can access the imported modules using the module name as a prefix
conn, cursor = database.Database.get_connection(DATABASE_NAME)

# ProxyDatabase class, use PostgreSQL database to store proxies
# for storing proxies, and performing operations on them

import psycopg2
from psycopg2 import Error


class Database:

    # init
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name

        # create connection and cursor
        self.connection = None
        # self.cursor = None

        # adjust connection and cursor
        self.create_connection()
        # self.create_cursor()

    # create table

    def create_table(self):
        # create query
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id SERIAL PRIMARY KEY,
            ip VARCHAR(255) NOT NULL,
            port VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        );
        """

        # cursor
        cursor = self.connection.cursor()

        # execute query
        cursor.execute(query)

        # commit
        self.connection.commit()

    # find one
    def find_one(self, query):
        # cursor
        cursor = self.connection.cursor()

        # execute query
        cursor.execute(query)

        # get result
        result = cursor.fetchone()

        return result

    # create connection

    def create_connection(self):
        # connect to database
        self.connection = psycopg2.connect(
            user="postgres",
            password="solkan11",
            host="localhost",
            port="5432",
            database=self.db_name
        )

        # print success message or error
        if self.connection:
            print("Connection successful!")

        else:
            print("Connection failed!")

    # renumber ids

    def renumber_ids(self):
        # create query
        query = f"""
        ALTER SEQUENCE {self.table_name}_id_seq RESTART WITH 1;
        """

        # execute query
        self.execute_query(query)

    # make changes to database
    def execute_query(self, query):
        # cursor
        cursor = self.connection.cursor()

        # execute query
        cursor.execute(query)

        # commit
        self.connection.commit()

    # str

    def __str__(self):
        return f"""
        Database Name: {self.db_name}
        Table Name: {self.table_name}
        """

# ProxyDatabase


class ProxyDatabase(Database):

    # init
    def __init__(self, db_name, table_name):
        super().__init__(db_name, table_name)

        # create table
        self.create_table()

    # proxy exists
    def proxy_exists(self, proxy):

        # create query
        query = f"""
        SELECT * FROM {self.table_name}
        WHERE ip = '{proxy.ip}'
        AND port = '{proxy.port}'
        AND username = '{proxy.username}'
        AND password = '{proxy.password}';
        """

        # find one
        if self.find_one(query) != None:
            return True

        return False

    # add proxy

    def add_proxy(self, proxy):

        if self.proxy_exists(proxy):
            return

        # create query
        query = f"""
            INSERT INTO {self.table_name} (ip, port, username, password)
            VALUES ('{proxy.ip}', '{proxy.port}', '{proxy.username}', '{proxy.password}');
            """

        # execute query
        self.execute_query(query)

    # get proxy
    def get_proxy_by_id(self, id):
        # create query
        query = f"""
        SELECT * FROM {self.table_name}
        WHERE id = {id};
        """

        # find one
        proxy = self.find_one(query)

        return proxy

    # get all proxies

    def get_all_proxies(self):
        # create query
        query = f"""
        SELECT * FROM {self.table_name};
        """

        # execute query
        self.execute_query(query)

        # get proxies
        proxies = self.connection.cursor.fetchall()

        return proxies

    # delete proxy
    def delete_proxy(self, id):
        # create query
        query = f"""
        DELETE FROM {self.table_name}
        WHERE id = {id};
        """

        # execute query
        self.execute_query(query)

        # renumber ids
        self.renumber_ids()

    # delete all proxies
    def delete_all_proxies(self):
        # create query
        query = f"""
        DELETE FROM {self.table_name};
        """

        # execute query
        self.execute_query(query)

    # get random proxy

    def get_random_proxy(self):

        # create query
        query = f"""
        SELECT * FROM {self.table_name}
        ORDER BY RANDOM()
        LIMIT 1;
        """

        # find one
        proxy = self.find_one(query)

        return proxy

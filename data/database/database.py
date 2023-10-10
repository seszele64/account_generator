import psycopg2

class Database:
    connections = {}

    @classmethod
    def get_connection(cls, database_name):
        if database_name not in cls.connections:
            conn = psycopg2.connect(database=database_name, user="postgres", password="solkan11", host="localhost", port="5432")
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
            
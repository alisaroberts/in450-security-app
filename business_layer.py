import psycopg
from psycopg import errors


class BusinessLayer:

    def __init__(self, host, database, user, password):
        self.connection_string = {
            "host": host,
            "port": 5432,
            "dbname": database,
            "user": user,
            "password": password,
        }

    def test_connection(self):
        with psycopg.connect(**self.connection_string):
            pass

    def get_row_count_in450a(self):
        try:
            with psycopg.connect(**self.connection_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT COUNT(*) FROM in450a;")
                    return cur.fetchone()[0]
        except errors.InsufficientPrivilege:
            raise PermissionError("Access denied to in450a.")

    def get_names_in450b(self):
        try:
            with psycopg.connect(**self.connection_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT first_name, last_name FROM in450b;")
                    return cur.fetchall()
        except errors.InsufficientPrivilege:
            raise PermissionError("Access denied to in450b.")

    def get_row_count_in450c(self):
        try:
            with psycopg.connect(**self.connection_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT COUNT(*) FROM in450c;")
                    return cur.fetchone()[0]
        except errors.InsufficientPrivilege:
            raise PermissionError("Access denied to in450c.")

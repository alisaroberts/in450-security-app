import psycopg


class BusinessLayer:
    def __init__(self):
        self.connection_string = {
            "host": "localhost",
            "port": 5432,
            "dbname": "postgres",
            "user": "postgres",
            "password": "Py2026",
        }

    def get_row_count_in450a(self):
        with psycopg.connect(**self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM in450a;")
                result = cur.fetchone()
                return result[0]

    def get_names_in450b(self):
        with psycopg.connect(**self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT first_name, last_name FROM in450b;")
                return cur.fetchall()

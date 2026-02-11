"""
Database setup script for IN450 Unit 2 Assignment.
Creates the in450a, in450b, and in450c tables in PostgreSQL
and loads data from the corresponding CSV files.
"""

import os
import psycopg

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",
    "user": "postgres",
    "password": "Py2026",
}

CSV_DIR = os.path.dirname(os.path.abspath(__file__))

CREATE_TABLES = {
    "in450a": """
        CREATE TABLE IF NOT EXISTS in450a (
            id SERIAL PRIMARY KEY,
            time NUMERIC,
            source VARCHAR(45),
            destination VARCHAR(45),
            protocol VARCHAR(20),
            length INTEGER,
            info TEXT
        );
    """,
    "in450b": """
        CREATE TABLE IF NOT EXISTS in450b (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            email VARCHAR(255),
            source VARCHAR(45),
            destination VARCHAR(45)
        );
    """,
    "in450c": """
        CREATE TABLE IF NOT EXISTS in450c (
            id SERIAL PRIMARY KEY,
            appid VARCHAR(255),
            appname VARCHAR(255),
            appversion VARCHAR(20),
            source VARCHAR(45),
            destination VARCHAR(45),
            digsig VARCHAR(64)
        );
    """,
}

CSV_FILES = {
    "in450a": "IN450A.csv",
    "in450b": "IN450B.csv",
    "in450c": "IN450C.csv",
}

# Column lists for COPY (excludes the auto-generated id column)
COPY_COLUMNS = {
    "in450a": "(time, source, destination, protocol, length, info)",
    "in450b": "(first_name, last_name, email, source, destination)",
    "in450c": "(appid, appname, appversion, source, destination, digsig)",
}


def setup_database():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            for table, ddl in CREATE_TABLES.items():
                # Drop existing table to start fresh
                cur.execute(f"DROP TABLE IF EXISTS {table};")
                cur.execute(ddl)
                print(f"Created table: {table}")

            conn.commit()

            # Load CSV data using PostgreSQL COPY
            for table, filename in CSV_FILES.items():
                filepath = os.path.join(CSV_DIR, filename)
                columns = COPY_COLUMNS[table]

                with open(filepath, "r") as f:
                    with cur.copy(
                        f"COPY {table} {columns} FROM STDIN WITH (FORMAT csv, HEADER true)"
                    ) as copy:
                        for line in f:
                            copy.write(line)

                cur.execute(f"SELECT COUNT(*) FROM {table};")
                count = cur.fetchone()[0]
                print(f"Loaded {count} rows into {table}")

            conn.commit()

    print("\nDatabase setup complete.")


if __name__ == "__main__":
    setup_database()

import os
from contextlib import contextmanager
from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv

DATABASE_PROMPT = "Enter the DATABASE_URI value : "
#database_uri ='postgres://muqopthd:5-4ufrJrs89u6rxc-_uIa_SN427i8L92@tyke.db.elephantsql.com/muqopthd'
database_uri = input(DATABASE_PROMPT)
if not database_uri:
    load_dotenv()
    database_uri = os.environ["DATABASE_URI"]
    os.environ['DATABASE_URL']='<URI>'

pool = SimpleConnectionPool(minconn=1, maxconn=10, dsn=database_uri)


@contextmanager
def get_connection():
    connection = pool.getconn()

    try:
        yield connection
    finally:
        pool.putconn(connection)

@contextmanager
def get_cursor(connection):
    with connection:
        with connection.cursor() as cursor:
            yield cursor
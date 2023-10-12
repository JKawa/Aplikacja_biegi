from typing import List, Tuple
from contextlib import contextmanager
from Connection import get_cursor
from Connection import *
import datetime
import psycopg2

Wyniki = Tuple[int, str, int, float, float, str, int, int, str]


CREATE_TABLE = "CREATE TABLE IF NOT EXISTS wyniki (id SERIAL PRIMARY KEY,ID INT, nazwa TEXT, nr_start INT,dystans FLOAT ,czas FLOAT, data DATE, rok INT,lokalizacja TEXT);"

INSERT_wynik = """INSERT INTO wyniki ( nazwa, nr_start,dystans ,czas, data,rok, lokalizacja  )
                VALUES (%s, %s,%s,%s,%s,%s,%s) RETURNING id
             """
DELETE_wynik = "DELETE FROM wyniki WHERE id=%s"


SELECT_wyniki = "SELECT * FROM wyniki order by id ASC"
SELECT_wynik = "SELECT * FROM wyniki WHERE id=%s order by id ASC"
SELECT_wyniki_id = "SELECT * FROM wyniki WHERE id=%s  order by id ASC"
SELECT_wyniki_nazwa = "SELECT * FROM wyniki WHERE nazwa = %s order by id ASC"
SELECT_wyniki_nr = "SELECT * FROM wyniki WHERE nr_start=%s order by id ASC"
SELECT_wyniki_dystans = "SELECT * FROM wyniki WHERE dystans=%s order by id ASC"
SELECT_wyniki_czas = "SELECT * FROM wyniki WHERE czas=%s order by id ASC"
SELECT_wyniki_data = "SELECT * FROM wyniki WHERE data=%s order by id ASC"
SELECT_wyniki_rok = "SELECT * FROM wyniki WHERE rok=%s order by id ASC"
SELECT_wyniki_lokalizacja = "SELECT * FROM wyniki WHERE lokalizacja=%s order by id ASC"

UPDATE_wyniki = "UPDATE wyniki SET nazwa = %s, nr_start=%s, dystans=%s,czas=%s, data=%s, rok=%s , lokalizacja=%s  WHERE id=%s"
UPDATE_id = "UPDATE wyniki SET id = (SELECT MAX(id) + 1 FROM wyniki);"
ALTAR_id = "ALTER SEQUENCE wyniki_id_seq RESTART WITH 1;"


def create_tables(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_TABLE)


def reset_id(connection, table_name="wyniki", id_column="id"):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT MAX({id_column}) FROM {table_name}")
        max_id = cursor.fetchone()[0]
        cursor.execute(
            f"ALTER SEQUENCE {table_name}_{id_column}_seq RESTART WITH {max_id + 1}"
        )
    connection.commit()


def get_wyniki(connection) -> List[Wyniki]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_wyniki)
        return cursor.fetchall()


def get_wyniki_filtr_nazwa(connection, nazwa: str) -> List[Wyniki]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_wyniki_nazwa, (nazwa,))
        return cursor.fetchall()


def get_wyniki_filtr_nr(connection, nr: int) -> List[Wyniki]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_wyniki_nr, (nr,))
        return cursor.fetchall()


def get_wyniki_filtr_dystans(connection, dystans: float) -> List[Wyniki]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_wyniki_dystans, (dystans,))
        return cursor.fetchall()


def get_wyniki_filtr_czas(connection, czas: float) -> List[Wyniki]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_wyniki_czas, (czas,))
        return cursor.fetchall()


def get_wyniki_filtr_data(connection, data: datetime) -> List[Wyniki]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_wyniki_data, (data,))
        return cursor.fetchall()


def get_wyniki_filtr_rok(connection, rok: int) -> List[Wyniki]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_wyniki_rok, (rok,))
        return cursor.fetchall()


def get_wyniki_filtr_lokalizacja(connection, lokalizacja: str) -> List[Wyniki]:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_wyniki_lokalizacja, (lokalizacja,))
        return cursor.fetchall()


def get_wynik(connection, wynik_id: int) -> Wyniki:
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_wynik, (wynik_id,))
        return cursor.fetchone()


def dodaj_wynik(connection, nazwa, nr_start, dystans, czas, data, rok, lokalizacja):
    with get_cursor(connection) as cursor:
        cursor.execute(
            INSERT_wynik, (nazwa, nr_start, dystans, czas, data, rok, lokalizacja)
        )


def update_wynik(
    connection, id: int, nazwa, nr_start, dystans, czas, data, rok, lokalizacja
):
    with get_cursor(connection) as cursor:
        cursor.execute(
            UPDATE_wyniki, (id, nazwa, nr_start, dystans, czas, data, rok, lokalizacja)
        )


def usun_wynik(connection, wynik_id: int):
    with get_cursor(connection) as cursor:
        cursor.execute(DELETE_wynik, (wynik_id,))

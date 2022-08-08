from typing import List
import datetime

import psycopg2

from Connection import get_connection
import Database


class Wyniki:
    def __init__(self, nazwa: str, nr_start: str,dystans:float , czas:float, data:datetime,rok:int, lokalizacja:str, _id: int = None):
        self.id = _id
        self.nazwa = nazwa
        self.nr_start = nr_start
        self.dystans=dystans
        self.czas=czas
        self.data=data
        self.rok = rok
        self.lokalizacja=lokalizacja

    def __repr__(self) -> str:
        return f"({self.nazwa!r}, {self.nr_start!r},{self.dystans!r},{self.czas!r},{self.data!r},{self.rok!r},{self.lokalizacja!r}, {self.id!r})"


    def save(self):
        with get_connection() as connection:
            nowy_wynik_id = Database.dodaj_wynik(connection, self.nazwa, self.nr_start,self.dystans,self.czas,self.data,self.rok,self.lokalizacja)
            self.id = nowy_wynik_id

    def update(self,id):
        with get_connection() as connection:
            id = Database.update_wynik(connection, id,self.nazwa, self.nr_start, self.dystans, self.czas,
                                                 self.data, self.rok, self.lokalizacja)
            self.id = id



    def delete(id):
        with get_connection() as connection:
            usuniety_wynik_id = Database.usun_wynik(connection, id)
            id = usuniety_wynik_id

    @classmethod
    def all(cls) -> List["Wyniki"]:
        with get_connection() as connection:
            wyniki = Database.get_wyniki(connection)
            return [cls(wynik[1], wynik[2], wynik[3],wynik[4],wynik[5] ,wynik[6],wynik[7],wynik[0]) for wynik in wyniki]

    @classmethod
    def filtr_nazwa(cls,nazwa) -> List["Wyniki"]:
        with get_connection() as connection:
            wyniki = Database.get_wyniki_filtr_nazwa(connection,nazwa)
            return [cls(wynik[1], wynik[2], wynik[3],wynik[4],wynik[5] ,wynik[6],wynik[7],wynik[0]) for wynik in wyniki]

    @classmethod
    def filtr_lokalizacja(cls,lokalizacja) -> List["Wyniki"]:
        with get_connection() as connection:
            wyniki = Database.get_wyniki_filtr_lokalizacja(connection,lokalizacja)
            return [cls(wynik[1], wynik[2], wynik[3],wynik[4],wynik[5] ,wynik[6],wynik[7],wynik[0]) for wynik in wyniki]

    @classmethod
    def filtr_nr(cls,nr) -> List["Wyniki"]:
        with get_connection() as connection:
            wyniki = Database.get_wyniki_filtr_nr(connection,nr)
            return [cls(wynik[1], wynik[2], wynik[3],wynik[4],wynik[5] ,wynik[6],wynik[7],wynik[0]) for wynik in wyniki]


    @classmethod
    def filtr_dystans(cls,dystans) -> List["Wyniki"]:
        with get_connection() as connection:
            wyniki = Database.get_wyniki_filtr_dystans(connection,dystans)
            return [cls(wynik[1], wynik[2], wynik[3],wynik[4],wynik[5] ,wynik[6],wynik[7],wynik[0]) for wynik in wyniki]

    @classmethod
    def filtr_czas(cls,czas) -> List["Wyniki"]:
        with get_connection() as connection:
            wyniki = Database.get_wyniki_filtr_czas(connection,czas)
            return [cls(wynik[1], wynik[2], wynik[3],wynik[4],wynik[5] ,wynik[6],wynik[7],wynik[0]) for wynik in wyniki]

    @classmethod
    def filtr_data(cls,data) -> List["Wyniki"]:
        with get_connection() as connection:
            wyniki = Database.get_wyniki_filtr_data(connection,data)
            return [cls(wynik[1], wynik[2], wynik[3],wynik[4],wynik[5] ,wynik[6],wynik[7],wynik[0]) for wynik in wyniki]


    def one(id) :
        with get_connection() as connection:
            wynik = Database.get_wynik(connection,id)
            return  wynik



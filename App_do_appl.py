from typing import List
import random
import datetime
import pytz
import Database
from Connection import get_connection
from Class import Wyniki


def app_dodaj_wynik(nazwa,nr_start,dystans,czas,data,rok,lokalizacja):
    wynik = Wyniki(nazwa, nr_start,dystans,czas,data,rok,lokalizacja)
    wynik.save()

def app_update_wynik(id,nazwa,nr_start,dystans,czas,data,rok,lokalizacja):
    wynik = Wyniki(nazwa, nr_start,dystans,czas,data,rok,lokalizacja)
    wynik.update(id)


def app_usun_wynik(numer:int):
    Wyniki.delete(numer)

def app_update_id():
    with get_connection() as connection:
        Database.ALTAR_SEQ(connection)
        Database.update_id(connection)


app_update_id()
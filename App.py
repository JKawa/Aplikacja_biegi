from typing import List
import random
import datetime
import pytz
import Database
from Connection import get_connection
from Class import Wyniki
from Excel_data import dg

#id SERIAL PRIMARY KEY, nazwa TEXT, nr_start INT,dystans FLOAT ,czas FLOAT, data DATE, rok INT

app_MENU = """-- Menu --

1) Dodaj nowy wynik
2) Usuń wynik
) Wprowadź zmiany
3) Wyświetl wyniki
4) Wyświetl konkretny wynik
5) Koniec
"""
wybor=" Wybierz z poniższych opcji"

def app_import_data():

    for x in range(len(dg)-1):
        nazwa = str(dg['bieg'][x])
        nr_start = int(dg['nr startowy'][x])
        dystans = float(dg['dystans[km]'][x])
        czas = float(dg['czas[min]'][x])
        data = dg['data'][x]
        rok = int(dg['rok'][x])
        lokalizacja=str(dg['miasto'][x])
        wynik = Wyniki(nazwa, nr_start, dystans, czas, data,rok, lokalizacja)
        wynik.save()
        print(f"obiekt{nazwa}")




with get_connection() as connection:
    Database.create_tables(connection)

def app_lista_wynikow():
    for wynik in Wyniki.all():
        print(f"{wynik.id}: {wynik.nazwa},dystans: {wynik.dystans}, czas: {wynik.czas} , data: {wynik.data},rok: {wynik.rok}, lokalizacja: {wynik.lokalizacja}")

def app_lista_wynikow_filtr(nazwa):
    for wynik in Wyniki.all_filtr():
        print(f"{wynik.id}: {wynik.nazwa}, czas: {wynik.czas} , data: {wynik.data},rok: {wynik.rok}, lokalizacja: {wynik.lokalizacja}")


def app_wyswietlanie_wyniku():
    id=input("Podaj id wyniku który chcesz wyświetlić:")
    print(f"{Wyniki.one(id)[0]}: {Wyniki.one(id)[1]}, czas: {Wyniki.one(id)[2]} , data: {Wyniki.one(id)[3]}")

def app_dodaj_wynik():
    nazwa = input("Wprowadź nazwe biegu: ")
    nr_start = input("Dodaj nr startowy: ")
    dystans = input("Dodaj dystans: ")
    czas = input("Dodaj czas: ")
    data = input("Dodaj datę[yyyy-mm-dd]: ")
    lokalizacja=input("Dodaj lokalizacje biegu(miasto):")
    wynik = Wyniki(nazwa, nr_start,dystans,czas,data,lokalizacja)
    wynik.save()
    print(f"{nazwa} został dodany do bazy")

def app_usun_wynik():
    wynik_id=input("Wprowadź ID wyniku który chcesz usunąć")

    Wyniki.delete(wynik_id)


MENU = {
    "1": app_dodaj_wynik,
    "2": app_usun_wynik,
    "3": app_lista_wynikow,
    "4": app_wyswietlanie_wyniku
}

def utworzenie_bazy():
    with get_connection() as connection:
        Database.create_tables(connection)

def menu():
    print(app_MENU)
    while (selection := input(wybor)) != "5":
        try:
            MENU[selection]()
        except KeyError:
            print("Nieprawidłowy wybór. Prubuj dalej")



#utworzenie_bazy()
#app_dodaj_wynik()
#app_import_data()
#app_lista_wynikow()
#wyswietlanie_wyniku(1)
#menu()
#print(Wyniki.one(5))
#app_usun_wynik()

import Database
from Connection import get_connection
from Class import Wyniki
from Excel_data import dg



def utworzenie_bazy():
    with get_connection() as connection:
        Database.create_tables(connection)


def import_data():
    for x in range(len(dg)-1):
        nazwa = str(dg['bieg'][x])
        nr_start = int(dg['nr startowy'][x])
        dystans = float(dg['dystans[km]'][x])
        czas = float(dg['czas[min]'][x])
        data = dg['data'][x]
        rok=int(dg['rok'][x])
        lokalizacja=str(dg['miasto'][x])
        wynik = Wyniki(nazwa, nr_start, dystans, czas, data,rok, lokalizacja)
        wynik.save()
        print(f"obiekt{nazwa}")



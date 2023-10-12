# -*- coding: utf-8 -*-
from Class import Wyniki
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, date

# from create_database_table_import import *
import encodings


def app_dodaj_wynik(nazwa, nr_start, dystans, czas, data, rok, lokalizacja):
    wynik = Wyniki(nazwa, nr_start, dystans, czas, data, rok, lokalizacja)
    wynik.save()


def app_update_wynik(id, nazwa, nr_start, dystans, czas, data, rok, lokalizacja):
    wynik = Wyniki(nazwa, nr_start, dystans, czas, data, rok, lokalizacja)
    wynik.update(id)


def app_usun_wynik(numer: int):
    Wyniki.delete(numer)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikacja biegowa")
        self.geometry("700x480")

        self.frame0 = tk.Frame(self, bg="#6F7FEB", height=220, width=700)
        self.frame0.grid_propagate(0)
        self.frame01 = tk.LabelFrame(self.frame0, bg="#6F7FEB", height=210, width=200)
        self.frame01.grid_propagate(0)
        self.frame1 = tk.LabelFrame(
            self, bg="#6F7FEB", text="Okno wynikowe", fg="white", height=250, width=700
        )
        self.frame1.grid_propagate(0)
        self.frame02 = tk.Frame(self.frame0, bg="#6F7FEB", height=220, width=700)
        self.frame02.grid_propagate(0)

        self.wyniki_table = ttk.Treeview(self.frame1)
        self.wyniki_table.grid(row=0, column=0, sticky="s")
        self.wyniki_table.rowconfigure(0, weight=1)
        sb = tk.Scrollbar(
            self.frame1, orient="vertical", command=self.wyniki_table.yview, width=15
        )
        sb.grid(row=0, column=1, sticky="NS")
        self.wyniki_table.config(yscrollcommand=sb.set)
        sb.config(command=self.wyniki_table.yview)

        self.wyniki_table["columns"] = (
            "id",
            "nazwa",
            "nr_start",
            "dystans",
            "czas",
            "data",
            "rok",
            "lokalizacja",
        )

        self.wyniki_table.column("#0", width=0, stretch="no")
        self.wyniki_table.column("id", anchor="center", width=20)
        self.wyniki_table.column("nazwa", anchor="center", width=145)
        self.wyniki_table.column("nr_start", anchor="center", width=100)
        self.wyniki_table.column("dystans", anchor="center", width=80)
        self.wyniki_table.column("czas", anchor="center", width=80)
        self.wyniki_table.column("data", anchor="center", width=90)
        self.wyniki_table.column("rok", anchor="center", width=60)
        self.wyniki_table.column("lokalizacja", anchor="center", width=100)

        self.wyniki_table.heading("#0", text="", anchor="center")
        self.wyniki_table.heading("id", text="Id", anchor="center")
        self.wyniki_table.heading("nazwa", text="Nazwa", anchor="center")
        self.wyniki_table.heading("nr_start", text="Nr.startowy", anchor="center")
        self.wyniki_table.heading("dystans", text="Dystans", anchor="center")
        self.wyniki_table.heading("czas", text="Czas", anchor="center")
        self.wyniki_table.heading("data", text="Data", anchor="center")
        self.wyniki_table.heading("rok", text="Rok", anchor="center")
        self.wyniki_table.heading("lokalizacja", text="Lokalizacja", anchor="center")
        self.wyniki_table.grid(row=0, column=0)

        def clear_all():
            for item in self.wyniki_table.get_children():
                self.wyniki_table.delete(item)

        self.frame0.grid(row=0, column=0)
        self.frame01.grid(row=0, column=0)
        self.frame1.grid(row=4, column=0)
        self.frame02.grid(row=0, column=1)

        def clear_frame(frame):
            for widgets in frame.winfo_children():
                widgets.destroy()

        def window_all():
            clear_all()
            print(Wyniki.all())
            # app_update_id()
            for wynik in Wyniki.all():
                self.wyniki_table.insert(
                    parent="",
                    index="end",
                    values=(
                        wynik.id,
                        wynik.nazwa,
                        wynik.nr_start,
                        wynik.dystans,
                        wynik.czas,
                        wynik.data,
                        wynik.rok,
                        wynik.lokalizacja,
                    ),
                )

        def window_filtr():
            l1 = tk.Label(self.frame02, bg="#6F7FEB")
            nazwa_label = tk.Label(
                self.frame02, text="Nazwa biegu: ", bg="#6F7FEB", fg="white"
            )
            nazwa_entry = tk.Entry(self.frame02, width=20)
            nr_start_label = tk.Label(
                self.frame02, text="Nr startowy: ", bg="#6F7FEB", fg="white"
            )
            nr_start_entry = tk.Entry(self.frame02, width=20)
            dystans_label = tk.Label(
                self.frame02, text="Dystans: ", bg="#6F7FEB", fg="white"
            )
            dystans_entry = tk.Entry(self.frame02, width=20)
            czas_label = tk.Label(self.frame02, text="Czas: ", bg="#6F7FEB", fg="white")
            czas_entry = tk.Entry(self.frame02, width=20)
            data_label = tk.Label(
                self.frame02, text="Data[yyyy-mm-dd]: ", bg="#6F7FEB", fg="white"
            )
            data_entry = tk.Entry(self.frame02, width=20)
            rok_label = tk.Label(
                self.frame02, text="Rok[yyyy-mm-dd]: ", bg="#6F7FEB", fg="white"
            )
            rok_entry = tk.Entry(self.frame02, width=20)
            lokalizacja_label = tk.Label(
                self.frame02,
                text="Dodaj lokalizacje biegu(miasto):",
                bg="#6F7FEB",
                fg="white",
            )
            lokalizacja_entry = tk.Entry(self.frame02, width=20)
            l1.grid(row=0, column=0)
            nazwa_label.grid(row=3, column=0, sticky="W")
            nazwa_entry.grid(row=3, column=1, sticky="E")
            nr_start_label.grid(row=4, column=0, sticky="W")
            nr_start_entry.grid(row=4, column=1, sticky="E")
            dystans_label.grid(row=5, column=0, sticky="W")
            dystans_entry.grid(row=5, column=1, sticky="E")
            czas_label.grid(row=6, column=0, sticky="W")
            czas_entry.grid(row=6, column=1, sticky="E")
            data_label.grid(row=7, column=0, sticky="W")
            data_entry.grid(row=7, column=1, sticky="E")
            rok_label.grid(row=8, column=0, sticky="W")
            rok_entry.grid(row=8, column=1, sticky="E")
            lokalizacja_label.grid(row=9, column=0, sticky="W")
            lokalizacja_entry.grid(row=9, column=1, sticky="E")

            def click():
                if len(nazwa_entry.get()) != 0:
                    clear_all()
                    nazwa = str(nazwa_entry.get())
                    for wynik in Wyniki.filtr_nazwa(nazwa):
                        self.wyniki_table.insert(
                            parent="",
                            index="end",
                            values=(
                                wynik.id,
                                wynik.nazwa,
                                wynik.nr_start,
                                wynik.dystans,
                                wynik.czas,
                                wynik.data,
                                wynik.rok,
                                wynik.lokalizacja,
                            ),
                        )
                else:
                    pass
                if len(nr_start_entry.get()) != 0:
                    clear_all()
                    nr = int(nr_start_entry.get())
                    for wynik in Wyniki.filtr_nr(nr):
                        self.wyniki_table.insert(
                            parent="",
                            index="end",
                            values=(
                                wynik.id,
                                wynik.nazwa,
                                wynik.nr_start,
                                wynik.dystans,
                                wynik.czas,
                                wynik.data,
                                wynik.rok,
                                wynik.lokalizacja,
                            ),
                        )
                else:
                    pass
                if len(dystans_entry.get()) != 0:
                    clear_all()
                    dystans = float(dystans_entry.get())
                    for wynik in Wyniki.filtr_dystans(dystans):
                        self.wyniki_table.insert(
                            parent="",
                            index="end",
                            values=(
                                wynik.id,
                                wynik.nazwa,
                                wynik.nr_start,
                                wynik.dystans,
                                wynik.czas,
                                wynik.data,
                                wynik.rok,
                                wynik.lokalizacja,
                            ),
                        )

                else:
                    pass
                if len(czas_entry.get()) != 0:
                    clear_all()
                    czas = czas_entry.get()
                    for wynik in Wyniki.filtr_czas(czas):
                        self.wyniki_table.insert(
                            parent="",
                            index="end",
                            values=(
                                wynik.id,
                                wynik.nazwa,
                                wynik.nr_start,
                                wynik.dystans,
                                wynik.czas,
                                wynik.data,
                                wynik.rok,
                                wynik.lokalizacja,
                            ),
                        )

                else:
                    pass
                if len(data_entry.get()) != 0:
                    clear_all()
                    data = str(data_entry.get())
                    for wynik in Wyniki.filtr_data(data):
                        self.wyniki_table.insert(
                            parent="",
                            index="end",
                            values=(
                                wynik.id,
                                wynik.nazwa,
                                wynik.nr_start,
                                wynik.dystans,
                                wynik.czas,
                                wynik.data,
                                wynik.rok,
                                wynik.lokalizacja,
                            ),
                        )

                else:
                    pass
                if len(lokalizacja_entry.get()) != 0:
                    clear_all()
                    lokalizacja = str(lokalizacja_entry.get())
                    for wynik in Wyniki.filtr_lokalizacja(lokalizacja):
                        self.wyniki_table.insert(
                            parent="",
                            index="end",
                            values=(
                                wynik.id,
                                wynik.nazwa,
                                wynik.nr_start,
                                wynik.dystans,
                                wynik.czas,
                                wynik.data,
                                wynik.rok,
                                wynik.lokalizacja,
                            ),
                        )

                else:
                    pass

            one_button = tk.Button(
                self.frame02, text="Ok", bg="#9EAAF2", fg="white", command=click
            )
            one_button.grid(row=11, column=1)

        def window_one():
            one_message = tk.Message(
                self.frame02,
                text="Wybierz id wyniku który chcesz wyświetlić",
                bg="#6F7FEB",
                fg="white",
                justify="center",
                aspect=500,
            )
            one_entry = tk.Entry(self.frame02, width=5)
            label_frame = tk.LabelFrame(
                self.frame02,
                bg="#6F7FEB",
                text="Wynik",
                fg="white",
                height=220,
                width=200,
            )
            label_frame.grid_propagate(0)
            nr_label = tk.Label(
                label_frame, text="Nr.startowy", bg="#6F7FEB", fg="white"
            )
            dystans_label = tk.Label(
                label_frame, text="Dystans", bg="#6F7FEB", fg="white"
            )
            czas_label = tk.Label(label_frame, text="Czas", bg="#6F7FEB", fg="white")
            data_label = tk.Label(label_frame, text="Data", bg="#6F7FEB", fg="white")
            rok_label = tk.Label(label_frame, text="Rok", bg="#6F7FEB", fg="white")
            lokalizacja_label = tk.Label(
                label_frame, text="Lokalizacja", bg="#6F7FEB", fg="white"
            )
            nazwa_label = tk.Label(label_frame, text="Nazwa", bg="#6F7FEB", fg="white")

            nr_label_put = tk.Label(label_frame, text=" ", bg="#6F7FEB", fg="white")
            dystans_label_put = tk.Label(
                label_frame, text=" ", bg="#6F7FEB", fg="white"
            )
            czas_label_put = tk.Label(label_frame, text=" ", bg="#6F7FEB", fg="white")
            data_label_put = tk.Label(label_frame, text=" ", bg="#6F7FEB", fg="white")
            rok_label_put = tk.Label(label_frame, text=" ", bg="#6F7FEB", fg="white")
            lokalizacja_label_put = tk.Label(
                label_frame, text=" ", bg="#6F7FEB", fg="white"
            )
            nazwa_label_put = tk.Label(label_frame, text=" ", bg="#6F7FEB", fg="white")

            label_frame.grid(row=3, column=0)
            nazwa_label.grid(row=0, column=0)
            nr_label.grid(row=1, column=0)
            dystans_label.grid(row=2, column=0)
            czas_label.grid(row=3, column=0)
            data_label.grid(row=4, column=0)
            rok_label.grid(row=5, column=0)
            lokalizacja_label.grid(row=6, column=0)
            nazwa_label_put.grid(row=0, column=1)
            nr_label_put.grid(row=1, column=1)
            dystans_label_put.grid(row=2, column=1)
            czas_label_put.grid(row=3, column=1)
            data_label_put.grid(row=4, column=1)
            rok_label_put.grid(row=5, column=1)
            lokalizacja_label_put.grid(row=6, column=1)

            one_message.grid(row=0, column=0)
            one_entry.grid(row=0, column=1)

            def click():
                while True:
                    try:
                        nr_ = int(one_entry.get())
                    except ValueError:
                        messagebox.showinfo(" ", "Nieprawidłowa wartość")
                        one_entry.delete(0, "end")
                        break
                    else:
                        numer = int(one_entry.get())
                        if numer not in range(len(Wyniki.all())):
                            messagebox.showinfo(
                                " ", "Wynik o takim id nie znajduje się w bazie"
                            )
                            break
                        else:
                            nazwa_label_put.config(text=Wyniki.one(numer)[1])
                            nr_label_put.config(text=Wyniki.one(numer)[2])
                            dystans_label_put.config(text=Wyniki.one(numer)[3])
                            czas_label_put.config(text=Wyniki.one(numer)[4])
                            data_label_put.config(text=Wyniki.one(numer)[5])
                            rok_label_put.config(text=Wyniki.one(numer)[6])
                            lokalizacja_label_put.config(text=Wyniki.one(numer)[7])
                            break

            one_button = tk.Button(
                self.frame02,
                text="Ok",
                width=5,
                bg="#9EAAF2",
                fg="white",
                command=click,
            )
            one_button.grid(row=0, column=2)

        def window_add():
            l1 = tk.Label(self.frame02, bg="#6F7FEB")
            nazwa_label = tk.Label(
                self.frame02, text="Wprowadź nazwe biegu: ", bg="#6F7FEB", fg="white"
            )
            nazwa_entry = tk.Entry(self.frame02, width=20)
            nr_start_label = tk.Label(
                self.frame02, text="Dodaj nr startowy: ", bg="#6F7FEB", fg="white"
            )
            nr_start_entry = tk.Entry(self.frame02, width=20)
            dystans_label = tk.Label(
                self.frame02, text="Dodaj dystans: ", bg="#6F7FEB", fg="white"
            )
            dystans_entry = tk.Entry(self.frame02, width=20)
            czas_label = tk.Label(
                self.frame02, text="Dodaj czas (min): ", bg="#6F7FEB", fg="white"
            )
            czas_entry = tk.Entry(self.frame02, width=20)
            data_label = tk.Label(
                self.frame02, text="Dodaj datę[yyyy-mm-dd]: ", bg="#6F7FEB", fg="white"
            )
            data_entry = tk.Entry(self.frame02, width=20)
            rok_label = tk.Label(
                self.frame02, text="Dodaj rok: ", bg="#6F7FEB", fg="white"
            )
            rok_entry = tk.Entry(self.frame02, width=20)
            lokalizacja_label = tk.Label(
                self.frame02,
                text="Dodaj lokalizacje biegu(miasto):",
                bg="#6F7FEB",
                fg="white",
            )
            lokalizacja_entry = tk.Entry(self.frame02, width=20)
            l1.grid(row=0, column=0)
            nazwa_label.grid(row=3, column=0, sticky="W")
            nazwa_entry.grid(row=3, column=1, sticky="E")
            nr_start_label.grid(row=4, column=0, sticky="W")
            nr_start_entry.grid(row=4, column=1, sticky="E")
            dystans_label.grid(row=5, column=0, sticky="W")
            dystans_entry.grid(row=5, column=1, sticky="E")
            czas_label.grid(row=6, column=0, sticky="W")
            czas_entry.grid(row=6, column=1, sticky="E")
            data_label.grid(row=7, column=0, sticky="W")
            data_entry.grid(row=7, column=1, sticky="E")
            rok_label.grid(row=8, column=0, sticky="W")
            rok_entry.grid(row=8, column=1, sticky="E")
            lokalizacja_label.grid(row=9, column=0, sticky="W")
            lokalizacja_entry.grid(row=9, column=1, sticky="E")

            def click():
                while True:
                    if len(nazwa_entry.get()) == 0:
                        nazwa = None
                    else:
                        nazwa = str(nazwa_entry.get())
                    if len(nr_start_entry.get()) == 0:
                        nr_start = None
                    else:
                        try:
                            id_ = int(nr_start_entry.get())
                        except ValueError:
                            messagebox.showinfo(" ", "Nieprawidłowa wartość")
                            nr_start_entry.delete(0, "end")
                            break
                        else:
                            nr_start = int(nr_start_entry.get())
                    if len(dystans_entry.get()) == 0:
                        dystans = None
                    else:
                        try:
                            dyst_ = float(dystans_entry.get())
                        except ValueError:
                            messagebox.showinfo(" ", "Nieprawidłowa wartość")
                            dystans_entry.delete(0, "end")
                            break
                        else:
                            dystans = float(dystans_entry.get())
                    if len(czas_entry.get()) == 0:
                        czas = None
                    else:
                        try:
                            czas_ = float(czas_entry.get())
                        except ValueError:
                            messagebox.showinfo(" ", "Nieprawidłowa wartość")
                            czas_entry.delete(0, "end")
                            break
                        else:
                            czas = float(czas_entry.get())
                    if len(data_entry.get()) == 0:
                        data = None
                    else:
                        try:
                            data_ = datetime.strptime(data_entry.get(), "%Y-%m-%d")
                        except ValueError:
                            messagebox.showinfo(
                                " ",
                                "Nieprawidłowa forma daty bądź wartość. Użyj formatu rok-miesiąc-dzień",
                            )
                            data_entry.delete(0, "end")
                            break
                        else:
                            data = datetime.strptime(data_entry.get(), "%Y-%m-%d")
                    if len(rok_entry.get()) == 0:
                        rok = None
                    else:
                        try:
                            rok_ = int(rok_entry.get())
                        except ValueError:
                            messagebox.showinfo(" ", "Nieprawidłowa wartość")
                            rok_entry.delete(0, "end")
                            break
                        else:
                            rok = int(rok_entry.get())
                    if len(lokalizacja_entry.get()) == 0:
                        lokalizacja = None
                    else:
                        lokalizacja = str(lokalizacja_entry.get())

                    app_dodaj_wynik(
                        nazwa, nr_start, dystans, czas, data, rok, lokalizacja
                    )
                    tk.messagebox.showinfo(
                        " ", f" Obiekt {nazwa} został dodany do bazy"
                    )
                    break

            one_button = tk.Button(
                self.frame02, text="Ok", bg="#9EAAF2", fg="white", command=click
            )
            one_button.grid(row=11, column=1)

        def window_update():
            id_label = tk.Label(
                self.frame02,
                text="Wprowadź id wyniky do aktualizacji: ",
                bg="#6F7FEB",
                fg="white",
            )
            nazwa_label = tk.Label(
                self.frame02, text="Wprowadź nazwe biegu: ", bg="#6F7FEB", fg="white"
            )
            id_entry = tk.Entry(self.frame02, width=15)
            nazwa_entry = tk.Entry(self.frame02, width=15)
            nr_start_label = tk.Label(
                self.frame02, text="Wprowadź  nr startowy: ", bg="#6F7FEB", fg="white"
            )
            nr_start_entry = tk.Entry(self.frame02, width=15)
            dystans_label = tk.Label(
                self.frame02, text="Wprowadź dystans: ", bg="#6F7FEB", fg="white"
            )
            dystans_entry = tk.Entry(self.frame02, width=15)
            czas_label = tk.Label(
                self.frame02, text="Wprowadź czas(min): ", bg="#6F7FEB", fg="white"
            )
            czas_entry = tk.Entry(self.frame02, width=15)
            data_label = tk.Label(
                self.frame02,
                text="Wprowadź datę[yyyy-mm-dd]: ",
                bg="#6F7FEB",
                fg="white",
            )
            data_entry = tk.Entry(self.frame02, width=15)
            rok_label = tk.Label(
                self.frame02, text="Wprowadź  rok: ", bg="#6F7FEB", fg="white"
            )
            rok_entry = tk.Entry(self.frame02, width=15)
            lokalizacja_label = tk.Label(
                self.frame02,
                text="Wprowadź lokalizacje biegu:",
                bg="#6F7FEB",
                fg="white",
            )
            lokalizacja_entry = tk.Entry(self.frame02, width=15)
            id_label.grid(row=2, column=0, sticky="W")
            nazwa_label.grid(row=3, column=0, sticky="W")
            id_entry.grid(row=2, column=1, sticky="W")
            nazwa_entry.grid(row=3, column=1, sticky="W")
            nr_start_label.grid(row=4, column=0, sticky="W")
            nr_start_entry.grid(row=4, column=1, sticky="W")
            dystans_label.grid(row=5, column=0, sticky="W")
            dystans_entry.grid(row=5, column=1, sticky="W")
            czas_label.grid(row=6, column=0, sticky="W")
            czas_entry.grid(row=6, column=1, sticky="W")
            data_label.grid(row=7, column=0, sticky="W")
            data_entry.grid(row=7, column=1, sticky="W")
            rok_label.grid(row=8, column=0, sticky="W")
            rok_entry.grid(row=8, column=1, sticky="W")
            lokalizacja_label.grid(row=9, column=0, sticky="W")
            lokalizacja_entry.grid(row=9, column=1, sticky="W")

            def click():
                while True:
                    if len(id_entry.get()) == 0:
                        break
                    else:
                        id = int(id_entry.get())
                    if len(nazwa_entry.get()) == 0:
                        nazwa = Wyniki.all()[id].nazwa
                    else:
                        nazwa = str(nazwa_entry.get())
                    if len(nr_start_entry.get()) == 0:
                        nr_start = Wyniki.all()[id].nr_start
                    else:
                        try:
                            nr_start_ = int(nr_start_entry.get())
                        except ValueError:
                            messagebox.showinfo(" ", "Nieprawidłowa wartość")
                            nr_start_entry.delete(0, "end")
                            break
                        else:
                            nr_start = int(nr_start_entry.get())
                    if len(dystans_entry.get()) == 0:
                        dystans = Wyniki.all()[id].dystans
                    else:
                        try:
                            dyst_ = float(dystans_entry.get())
                        except ValueError:
                            messagebox.showinfo(" ", "Nieprawidłowa wartość")
                            dystans_entry.delete(0, "end")
                            break
                        else:
                            dystans = float(dystans_entry.get())
                    if len(czas_entry.get()) == 0:
                        czas = Wyniki.all()[id].czas
                    else:
                        try:
                            czas_ = float(czas_entry.get())
                        except ValueError:
                            messagebox.showinfo(" ", "Nieprawidłowa wartość")
                            czas_entry.delete(0, "end")
                            break
                        else:
                            czas = float(czas_entry.get())
                    if len(data_entry.get()) == 0:
                        data = Wyniki.all()[id].data
                    else:
                        try:
                            data_ = datetime.strptime(data_entry.get(), "%Y-%m-%d")
                        except ValueError:
                            messagebox.showinfo(
                                " ",
                                "Nieprawidłowa forma daty bądź wartość. Użyj formatu rok-miesiąc-dzień",
                            )
                            data_entry.delete(0, "end")
                            break
                        else:
                            data = datetime.strptime(data_entry.get(), "%Y-%m-%d")
                    if len(rok_entry.get()) == 0:
                        rok = Wyniki.all()[id].rok
                    else:
                        try:
                            rok_ = int(rok_entry.get())
                        except ValueError:
                            messagebox.showinfo(" ", "Nieprawidłowa wartość")
                            rok_entry.delete(0, "end")
                            break
                        else:
                            rok = int(rok_entry.get())
                    if len(lokalizacja_entry.get()) == 0:
                        lokalizacja = Wyniki.all()[id].lokalizacja
                    else:
                        lokalizacja = str(lokalizacja_entry.get())

                    app_update_wynik(
                        nazwa, nr_start, dystans, czas, data, rok, lokalizacja, id
                    )
                    tk.messagebox.showinfo(
                        " ", f" Obiekt {nazwa} został zaktualizowany"
                    )
                    break

            one_button = tk.Button(
                self.frame02, text="Ok", bg="#9EAAF2", fg="white", command=click
            )
            one_button.grid(row=11, column=1)

        def window_delete():
            l1 = tk.Label(self.frame02, bg="#6F7FEB")
            l2 = tk.Label(self.frame02, bg="#6F7FEB")
            l3 = tk.Label(self.frame02, bg="#6F7FEB")
            l4 = tk.Label(self.frame02, bg="#6F7FEB")
            one_message = tk.Message(
                self.frame02,
                text="Wybierz id wyniku który chcesz usunąć",
                bg="#6F7FEB",
                fg="white",
                justify="center",
                aspect=500,
            )
            one_entry = tk.Entry(self.frame02, width=5)
            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0)
            l3.grid(row=2, column=0)
            l4.grid(row=3, column=0)
            one_message.grid(row=4, column=0)
            one_entry.grid(row=4, column=1)

            def click():
                try:
                    numer = int(one_entry.get())
                except ValueError:
                    messagebox.showinfo(" ", "Nieprawidłowa wartość")
                    one_entry.delete(0, "end")
                else:
                    if numer not in range(len(Wyniki.all())):
                        messagebox.showinfo(" ", "Id nie znajduje się w bazie")
                    else:
                        app_usun_wynik(numer)
                        tk.messagebox.showinfo(
                            " ", f" Obiekt {numer} został usunięty z bazy"
                        )

            one_button = tk.Button(
                self.frame02, text="Ok", bg="#9EAAF2", fg="white", command=click
            )
            one_button.grid(row=4, column=4)

        def click1():
            clear_frame(self.frame02)
            window_add()

        def click2():
            clear_frame(self.frame02)
            window_update()

        def click3():
            clear_frame(self.frame02)
            window_delete()

        def click4():
            clear_frame(self.frame02)
            window_all()

        def click5():
            clear_frame(self.frame02)
            window_one()

        def click6():
            clear_frame(self.frame02)
            window_filtr()

        def click7():
            App.quit(self)

        self.Button1 = tk.Button(
            self.frame01,
            text="Dodaj nowy wynik",
            width=24,
            bg="#8895EB",
            fg="white",
            command=click1,
        )
        self.Button2 = tk.Button(
            self.frame01,
            text="Aktualizacja wyniku",
            width=24,
            bg="#8895EB",
            fg="white",
            command=click2,
        )
        self.Button3 = tk.Button(
            self.frame01,
            text="Usuń wynik",
            width=24,
            bg="#8895EB",
            fg="white",
            command=click3,
        )
        self.Button4 = tk.Button(
            self.frame01,
            text="Wyświetl wyniki",
            width=24,
            bg="#8895EB",
            fg="white",
            command=click4,
        )
        self.Button5 = tk.Button(
            self.frame01,
            text="Wyświetl konkretny wynik",
            width=24,
            bg="#8895EB",
            fg="white",
            command=click5,
        )
        self.Button6 = tk.Button(
            self.frame01,
            text="Filtr",
            width=24,
            bg="#8895EB",
            fg="white",
            command=click6,
        )
        self.Button7 = tk.Button(
            self.frame01,
            text="Koniec",
            width=24,
            bg="#8895EB",
            fg="white",
            command=click7,
        )

        self.Button1.grid(row=0, column=0)
        self.Button2.grid(row=1, column=0)
        self.Button3.grid(row=2, column=0)
        self.Button4.grid(row=3, column=0)
        self.Button5.grid(row=4, column=0)
        self.Button6.grid(row=5, column=0)
        self.Button7.grid(row=6, column=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()

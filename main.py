import copy
from Logic.crud import adaugare_obiect
from Tests.run_all import run_all
from UserInterface.console import run_menu


def main():
    lista = []
    lista = adaugare_obiect(lista, 1, "Obiect intai", "Descriere1", 150, "loc1")
    lista = adaugare_obiect(lista, 2, "Obiect doi", "Descriere2", 150, "loc2")
    lista = adaugare_obiect(lista, 3, "Obiect trei", "Descriere3", 10.9, "loc3")
    lista = adaugare_obiect(lista, 4, "Obiect patru", "Descriere4", 89.8, "loca")
    undo_lista = copy.deepcopy(lista)
    run_menu(lista,undo_lista)


run_all()
main()
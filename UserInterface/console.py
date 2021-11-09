from Domain.obiect import toString
from Logic.crud import *
from Logic.Functionalitati import *


def printMenu():
    print("1. Adaugare obiect ")
    print("2. Stergere obiect ")
    print("3. Modificare obiect ")
    print("4. Mutati obiectele dintr-o locatie in alta ")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.")
    print("6. Determinarea celui mai mare preț pentru fiecare locație")
    print("7. Ordonarea obiectelor crescator dupa pretul de achizitie ")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("u.Undo")
    print("r.Redo")
    print("a. Afisare obiect ")
    print("X. Iesire")


def uiAdaugaObiect(lista,undo_list,redo_list):
    try:
        id=input("Dati id-ul ")
        nume=input("Dati numele ")
        descriere=input("Dati descrierea ")
        pret=float(input("Dati pretul "))
        locatie=input("Dati locatia ")
        rezultat= adaugare_obiect(id, nume, descriere, pret, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeObiect(lista,undo_list, redo_list):
    try:
        id = input("Dati id-ul obiectului pe care vreti sa il stergeti ")
        rezultat=sterge_obiect(id,lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaObiect(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul obiectului de modificat ")
        nume = input("Dati noul nume ")
        descriere = input("Dati noua descriere ")
        pret = float(input("Dati noul pret "))
        locatie = input("Dati noua locatie ")
        if len(locatie) != 4:
            raise ValueError("Locatia introdusa trebuie sa contina exact 4 caractere")

        rezultat= modificare_obiect(id, nume, descriere, pret, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiMutaObiecte(lista,undo_list,redo_list):
    locatie1 = input("Dati locatia din care vreti sa mutati obiectele ")
    locatie2 = input("Dati locatia in care vreti sa mutati obiectele: ")
    if len(locatie2) != 4:
        raise ValueError("Locatia introdusa trebuie sa contina exact 4 caractere")

    rezultat= mutare_obiecte(locatie1, lista, locatie2)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def uiConcatenare(lista,undo_list,redo_list):
    try:
        string=input("Dati stringul de la tastatura: ")
        pret=float(input("Dati pretul: "))
        rezultat= concatenare_obiect(string,lista,pret)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiLocatie(lista):
    rezultat=pretmaximloc(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie, rezultat[locatie]))


def uiOrdoneaza(lista,undo_list,redo_list):
    rezultat=Ordonare_Pret(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def uiSumaPreturilor(lista):
    rezultat = suma_preturi(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))


def runMenu(lista):
    undo_list = []
    redo_list = []
    while True:
        printMenu()
        cmd=input("Dati optiunea: ")
        if cmd=="1":
            lista=uiAdaugaObiect(lista,undo_list,redo_list)
        elif cmd=="2":
            lista=uiStergeObiect(lista,undo_list, redo_list)
        elif cmd=="3":
            lista=uiModificaObiect(lista, undo_list, redo_list)
        elif cmd=="4":
            lista=uiMutaObiecte(lista,undo_list,redo_list)
        elif cmd=="5":
            lista=uiConcatenare(lista,undo_list,redo_list)
        elif cmd=="6":
            uiLocatie(lista)
        elif cmd=="7":
            lista=uiOrdoneaza(lista,undo_list,redo_list)
        elif cmd=="8":
            lista=uiSumaPreturilor(lista)
        elif cmd=="u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif cmd=="r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif cmd=="a":
            showAll(lista)
        elif cmd=="x":
            break
        else:
            print("Optiune invalida! Reincercati!")
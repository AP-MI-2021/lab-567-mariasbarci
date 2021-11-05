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
    print("a. Afisare obiect ")
    print("X. Iesire")


def uiAdaugaObiect(lista):
    try:
        id=input("Dati id-ul ")
        nume=input("Dati numele ")
        descriere=input("Dati descrierea ")
        pret=float(input("Dati pretul "))
        locatie=input("Dati locatia ")

        return adaugare_obiect(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeObiect(lista):
    try:
        id = input("Dati id-ul obiectului pe care vreti sa il stergeti ")
        return sterge_obiect(id,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaObiect(lista):
    try:
        id = input("Dati id-ul obiectului de modificat ")
        nume = input("Dati noul nume ")
        descriere = input("Dati noua descriere ")
        pret = float(input("Dati noul pret "))
        locatie = input("Dati noua locatie ")
        return modificare_obiect(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiMutaObiecte(lista):
    locatie1 = input("Dati locatia din care vreti sa mutati obiectele ")
    locatie2 = input("Dati locatia in care vreti sa mutati obiectele: ")
    return mutare_obiecte(locatie1, lista, locatie2)


def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def uiConcatenare(lista):
    try:
        string=input("Dati stringul de la tastatura: ")
        pret=float(input("Dati pretul: "))
        return concatenare_obiect(string,lista,pret)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiLocatie(lista):
    rezultat=pretmaximloc(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie, rezultat[locatie]))


def uiOrdoneaza(lista):
    showAll(Ordonare_Pret(lista))


def uiSumaPreturilor(lista):
    rezultat = suma_preturi(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))


def runMenu(lista):
    while True:
        printMenu()
        cmd=input("Dati optiunea: ")
        if cmd=="1":
            lista=uiAdaugaObiect(lista)
        elif cmd=="2":
            lista=uiStergeObiect(lista)
        elif cmd=="3":
            lista=uiModificaObiect(lista)
        elif cmd=="4":
            lista=uiMutaObiecte(lista)
        elif cmd=="5":
            lista=uiConcatenare(lista)
        elif cmd=="6":
            lista=uiLocatie(lista)
        elif cmd=="7":
            uiOrdoneaza(lista)
        elif cmd=="8":
            uiSumaPreturilor(lista)
        elif cmd=="a":
            showAll(lista)
        elif cmd=="x":
            break
        else:
            print("Optiune invalida! Reincercati!")
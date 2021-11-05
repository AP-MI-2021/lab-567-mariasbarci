from Domain.obiect import *
from Logic.crud import *
from Logic.Functionalitati import *


def test_mutare_obiecte():
    lista=[]
    lista=adaugare_obiect("1","carte", "roz", 90, "loc1",lista)
    lista=adaugare_obiect("2","portofel", "alb", 5000, "loc1",lista)
    lista=adaugare_obiect("3", "cana", "pt cafea", 4, "loc2",lista)
    lista=mutare_obiecte("loc1", lista, "loc2")

    assert get_locatie(get_by_id("1", lista)) == "loc2"
    assert get_locatie(get_by_id("2", lista)) == "loc2"
    assert get_locatie(get_by_id("3", lista)) == "loc2"



def test_concatenre_obiect():
    lista = []
    lista = adaugare_obiect("1", "Telefon", "Faciliteaza comunicarea intre oameni", 1000, "ASPC", lista)
    lista = adaugare_obiect("2", "Laptop", "Asigura o buna desfasurare a proiectelor online", 3000, "ASPC", lista)
    lista = adaugare_obiect("3", "Masina", "Deplasarea angajatilor", 20000, "AFCD", lista)
    lista=concatenare_obiect(" asa", lista, 2000)
    assert get_descriere(get_by_id("1", lista))=="Faciliteaza comunicarea intre oameni"
    assert get_descriere(get_by_id("2", lista))=="Asigura o buna desfasurare a proiectelor online asa"
    assert get_descriere(get_by_id("3", lista))=="Deplasarea angajatilor asa"

def test_pretmaximloc():
    lista = []
    lista = adaugare_obiect("1", "carte", "roz", 90, "loc1", lista)
    lista = adaugare_obiect("2", "portofel", "alb", 5000, "loc1", lista)
    lista = adaugare_obiect("3", "cana", "pt cafea", 4, "loc2", lista)
    lista = adaugare_obiect("4", "caiet", "roz", 5, "loc2", lista)
    lista = adaugare_obiect("5", "Pix", "obiect de scris", 10, "loc0", lista)
    lista = adaugare_obiect("6", "creion ", "obiect de scris ", 90, "loc0", lista)

    rezultat=pretmaximloc(lista)
    assert len(rezultat)==3
    assert rezultat["loc1"]==5000
    assert rezultat["loc2"]==5
    assert rezultat["loc0"]==90

def test_Ordonare_Pret():
    lista=[]
    lista = adaugare_obiect("1", "caiet", "roz", 1000, "loc1", lista)
    lista = adaugare_obiect("2", "telefon", "desc", 3000, "locC", lista)
    lista = adaugare_obiect("3", "carte", "de citit", 21000, "loca", lista)
    lista = adaugare_obiect("4", "Pix", "obiect de scris", 10, "locd", lista)
    lista = adaugare_obiect("5", "stilou ", "Obiect de scris ", 3000, "ssss", lista)
    lista = adaugare_obiect("6", "ceas", "pt ora", 20000, "locd", lista)
    rezultat=Ordonare_Pret(lista)
    assert get_id(rezultat[0])=="4"
    assert get_id(rezultat[1])=="1"
    assert get_id(rezultat[2])=="2"
    assert get_id(rezultat[3])=="5"
    assert get_id(rezultat[4])=="6"
    assert get_id(rezultat[5])=="3"

def test_suma_preturi():
    lista=[]
    lista = adaugare_obiect("1", "carte", "pt scris", 1000, "loc1", lista)
    lista = adaugare_obiect("2", "telefon", "negru", 3000, "loc1", lista)
    lista = adaugare_obiect("3", "ceas", "albastru", 21000, "loc2", lista)
    rezultat=suma_preturi(lista)
    assert len(rezultat)==2
    assert rezultat["loc1"]==4000
    assert rezultat["loc2"]==21000
from Logic.crud import *


def test_adaugare_obiect():
    lista = []
    lista = adaugare_obiect(lista, 1, "pix", "negru", 22, "in penar")

    assert get_id(lista[0]) == 1
    assert get_nume(lista[0]) == "pix"
    assert get_descriere(lista[0]) == "negru"
    assert get_pret(lista[0]) == 22
    assert get_locatie(lista[0]) == "in penar"


def test_sterge_obiect():
    obj1 = creare_obiect(1, "nume1", "galben", 33, "locatie1")
    obj2 = creare_obiect(2, "Carte", "de bucate", 80, "in bucatarie")

    lista_obiecte = [obj1, obj2]
    lista_obiecte = sterge_obiect(lista_obiecte, 1)

    assert len(lista_obiecte) == 1
    assert get_by_id(lista_obiecte, 2) == obj2
    assert get_by_id(lista_obiecte, 1) is None

def test_modificare_obiect():
    obj1 = creare_obiect(1, "nume1", "galben", 33, "locatie1")
    obj2 = creare_obiect(2, "Carte", "de bucate", 80, "in bucatarie")

    lista_obiecte = [obj1, obj2]
    lista_obiecte = modificare_obiect(lista_obiecte,1,"nume2","",10,"")

    obj_update=get_by_id(lista_obiecte,1)
    assert get_nume(obj_update) == "nume2"
    assert get_descriere(obj_update) == "galben"
    assert get_pret(obj_update) == 10
    assert get_locatie(obj_update) == "locatie1"
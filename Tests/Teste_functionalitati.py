from Domain.obiect import get_locatie,get_descriere,get_id
from Logic.crud import get_by_id,adaugare_obiect
from Logic.Functionalitati import mutare_locatie,concatenare_descriere, ordonare_dupa_pret
def lista_teste():
    lista = []
    lista = adaugare_obiect(lista, 2, "Obiect doi", "Desc1", 2005.9, "loc")
    lista = adaugare_obiect(lista, 3, "Obiect trei", "desc2", 20.8, "loc1")
    lista = adaugare_obiect(lista, 4, "Obiect patru", "desc3", 205.8, "loc")
    lista = adaugare_obiect(lista, 5, "Obiect patru", "desc4", 5.89, "loc4")
    lista = adaugare_obiect(lista, 6, "Obiect patru", "desc5", 50.5, "loc5")
    return lista


def test_mutare_locatie():
    lista = lista_teste()
    lista = mutare_locatie(lista, "loc", "locatie")

    assert get_locatie(get_by_id(lista, 2)) == "locatie"
    assert get_locatie(get_by_id(lista, 4)) == "locatie"
    assert get_locatie(get_by_id(lista, 3)) == "loc1"
    assert get_locatie(get_by_id(lista, 5)) == "loc4"
    assert get_locatie(get_by_id(lista, 6)) == "loc5"


def test_concatenare_descriere():
    lista = lista_teste()
    lista = concatenare_descriere(lista, 67, " Yyy Yyy")

    assert get_descriere(get_by_id(lista, 2)) == "Desc1 Yyy Yyy"
    assert get_descriere(get_by_id(lista, 4)) == "desc3 Yyy Yyy"
    assert get_descriere(get_by_id(lista, 3)) == "desc2"
    assert get_descriere(get_by_id(lista, 6)) == "desc5"


def test_ordonare_dupa_pret():
    lista =lista_teste()
    lista = ordonare_dupa_pret(lista)

    assert get_id(lista[0]) == 5
    assert get_id(lista[1]) == 3
    assert get_id(lista[2]) == 6
    assert get_id(lista[3]) == 4
    assert get_id(lista[4]) == 2
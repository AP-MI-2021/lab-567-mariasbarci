from Domain.obiect import get_locatie, get_id, get_pret, get_descriere
from Logic.crud import modificare_obiect


def mutare_locatie(lista_obiecte,locatie1, locatie2):
    """
    Muta obiectele dintr-o locatie in alta
    :param lista_obiecte:
    :param locatie1: locatia initiala
    :param locatie2: locatia in care trebuie sa ajunga obiectele
    :return: lista modificata
    """
    for obiect in lista_obiecte:
        if get_locatie(obiect) == locatie1:
            lista_obiecte = modificare_obiect(lista_obiecte, get_id(obiect), "", "", -1, locatie2)
    return lista_obiecte


def concatenare_descriere(lista_obiecte, pret, string):
    """
    Concateneaza la descrierea unui obiect un sir dat daca pretul obiectului este mai mare decat pretul dat
    :param lista_obiecte: lista obiectelor
    :param pret: pretul dat
    :param sir: sirul dat
    :return: lista modificata
    """
    for obiect in lista_obiecte:
        if get_pret(obiect) > pret:
            obiect["descriere"] = get_descriere(obiect) + string
    return lista_obiecte

def ordonare_dupa_pret(lista_obiecte):
    '''
    Returneaza lista ordonata in functie de pret
    :param lista_obiecte: lista cu obiecte
    :return: ordonarea obiectelor dupa pret
    '''
    return sorted(lista_obiecte,key=lambda p: p['pret'])
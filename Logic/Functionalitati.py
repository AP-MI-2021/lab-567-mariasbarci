from Domain.obiect import *

def mutare_obiecte(locatie1, lista, locatie2):
    '''
    Mutarea tuturor obiectelor dintr-o locație în alta.
    :param substringLocatie: stringul dupa care se cauta locatia
    :param lista: lista de obiecte
    :return: lista in care obiectele care apartin de locatia data sunt mutate in alta locatie
    '''

    listaNoua=[]
    for obiect in lista:
        if locatie1==get_locatie(obiect):
            obiectNou=creare_obiect(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect),
                get_pret(obiect),
                get_locatie(obiect).replace(get_locatie(obiect), locatie2)
            )
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua

def concatenare_obiect(string, lista, pret):
    '''
    Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită
    :param text: stringul care trebuie adaugat la descrierile obiectelor cu pretul mai mare decat o valoare citita
    :param lista: lista de obiecte
    :param pret: valoarea dupa care comparam pretul fiecarui obiect pt a verifica daca ii modificam descrierea
    :return: o lista noua in care toate descrierile obiectelor cu pretul mai mare decat valoarea data au fost modificate, concatenandu-se un string
    '''
    listaNoua=[]
    for obiect in lista:
        if get_pret(obiect)>pret:
            obiectNou=creare_obiect(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect) + str(string),
                get_pret(obiect),
                get_locatie(obiect)
             )
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua


def pretmaximloc(lista):
    '''
    Determinarea celui mai mare preț pentru fiecare locație
    :param lista: lista de obiecte
    :return: un dictionar cu cel mai mare pret pentru fiecare locatie
    '''
    rezultat={}
    for obiect in lista:
        locatie=get_locatie(obiect)
        if locatie in rezultat:
            if get_pret(obiect)>rezultat[locatie]:
                rezultat[locatie]=get_pret(obiect)
        else:
            rezultat[locatie]=get_pret(obiect)
    return rezultat

def Ordonare_Pret(lista):
    '''
    Ordonarea obiectelor crescător după prețul de achiziție.
    :param lista: lista de obiecte
    :return: Obiectele ordonate crescator dupa pretul de achizitie
    '''
    return sorted(lista, key=lambda obiect: get_pret(obiect))

def suma_preturi(lista):
    '''
    Afișarea sumelor prețurilor pentru fiecare locație.
    :param lista: lista de obiecte
    :return: suma preturilor pentru fiecare locatie
    '''
    rezultat={}
    for obiect in lista:
            locatie=get_locatie(obiect)
            if locatie in rezultat:
                rezultat[locatie]=rezultat[locatie]+get_pret(obiect)
            else:
                rezultat[locatie]=get_pret(obiect)
    return rezultat
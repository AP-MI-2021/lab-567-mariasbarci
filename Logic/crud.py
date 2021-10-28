from Domain.obiect import creare_obiect, get_id, get_nume, get_pret, get_descriere, get_locatie


def get_by_id(lista_obiecte, id):
    """
    Returnarea obiectului cu id ul dat
    :param lista_obiecte: lista cu obiecte
    :param id: id ul obiectului cautat
    :return: obiectul cu id ul cerut sau None daca nu exista
    """
    for obiect in lista_obiecte:
        if get_id(obiect) == id:
            return obiect
    return None


def adaugare_obiect(lista_obiecte, id, nume, descriere, pret, locatie):
    """
    Adauga in lista cu obiecte un obiect dat
    :param lista_obiecte: lista cu obiecte
    :param id: id-ul obiectului ce trebuie adaugat listei obiectelor
    :param nume:
    :param descriere:
    :param pret:
    :param locatie:
    :return: lista cu obiectul cerut adaugat
    """
    obiect = creare_obiect(id, nume, descriere, pret, locatie)
    return lista_obiecte + [obiect]


def sterge_obiect(lista_obiecte, id):
    """
    Sterge din lista cu obiecte un obiectu cu id-ul dat
    :param lista_obiecte: lista cu obiecte
    :param id: id-ul obiectului ce trebuie sters
    :return: lista cu obiectul dat sters
    """
    return [obiect for obiect in lista_obiecte if get_id(obiect) != id]


def modificare_obiect(lista_obiecte, id, nume, descriere, pret, locatie):
    """
    Modifica in lista cu obiecte obiectul cu id-ul dat
    :param lista_obiecte: lista cu obiecte
    :param id: id-ul obiectului ce trebuie modificat
    :param nume: numele modicat sau "" daca nu se modifica
    :param descriere: descrierea modificata sau "" daca nu se modifica
    :param pret: pretul modificat sau -1 daca nu se modifica
    :param locatie: locatie modificata sau "" daca nu se modifica
    :return: lista cu obiecte in care obiectul cu id-ul dat este modificat
    """
    lista_modificata = []
    for obiect in lista_obiecte:
        if get_id(obiect) == id:
            obiect_nou = creare_obiect(
                id,
                nume if nume != "" else get_nume(obiect),
                descriere if descriere != "" else get_descriere(obiect),
                pret if pret != -1 else get_pret(obiect),
                locatie if locatie != "" else get_locatie(obiect)
            )
            lista_modificata.append(obiect_nou)
        else:
            lista_modificata.append(obiect)
    return lista_modificata
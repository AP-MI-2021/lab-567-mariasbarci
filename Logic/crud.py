from Domain.obiect import creare_obiect, get_id


def adaugare_obiect(id, nume, descriere, pret, locatie, lista):
    '''
    Adauga un obiect intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: o lista continand vechile obiecte si noul obiect
    '''
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja! ")
    if pret < 0:
        raise ValueError("Pretul trebuie sa fie pozitiv!")
    if len(locatie)!=4:
        raise ValueError("Locatia trb sa aiba 4 caractere")
    obiect=creare_obiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]


def get_by_id(id, lista):
    '''
    Da elementul din lista cu un id dat
    :param id: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat sau None daca nu exista
    '''
    for obiect in lista:
        if get_id(obiect) == id:
            return obiect
    return None

def sterge_obiect(id, lista):
    '''
    Sterge obiectul cu id-ul dat dintr-o lista
    :param id: id-ul obiectului care se va sterge
    :param lista: lista de obiecte
    :return: o lista de obiecte fara obiectul cu id-ul dat
    '''
    if get_by_id(id,lista) is None:
        raise ValueError("Id-ul nu exista")
    return [obiect for obiect in lista if get_id(obiect)!= id]

def modificare_obiect(id, nume, descriere, pret, locatie, lista):
    '''
    Modifica obiectul cu id-ul dat
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret: pretul obiectului
    :param locatie: locatia obiectului
    :param lista: o lista de obiecte
    :return: lista modificata
    '''
    if len(locatie)!=4:
        raise ValueError("Locatia trb sa aiba 4 caractere")
    if pret < 0:
        raise ValueError("Pretul trebuie sa fie pozitiv!")

    if get_by_id(id,lista) is None:
        raise ValueError("Id-ul nu exista! ")
    listaNoua=[]
    for obiect in lista:
        if get_id(obiect)==id:
            obiectNou=creare_obiect(id, nume, descriere, pret, locatie)
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua
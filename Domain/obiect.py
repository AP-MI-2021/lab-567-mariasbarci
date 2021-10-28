def creare_obiect(id, nume, descriere, pret, locatie):
    '''

    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return:
    '''
    return {
        "id":id,
        "nume":nume,
        "descriere":descriere,
        "pret":pret,
        "locatie":locatie
    }
    return [id, nume, descriere, pret, locatie]
    #return {
    #    "id": id,
    #    "nume": nume,
    #    "descriere": descriere,
    #    "pret": pret,
    #    "locatie": locatie
    #}


def get_id(obiect):
    """
    Da id-ul unui obiect
    :param obiect: dict
    :return:
    """
    return obiect["id"]
    return obiect[0]
    #return obiect["id"]

def set_id(obiect, id):
    '''
    :param obiect: dict
    :param id: string
    :return:
    '''
    obiect["id"] = id
    obiect[0] = id
    # obiect["id"] = id


def get_nume(obiect):
    """
    Da numele obiectului
    :param nume: string
    :return:
    """
    return obiect["nume"]
    return obiect[1]
    # return obiect["nume"]


def set_nume(obiect, nume):
    """
    :param nume: string
    :return:
    """
    obiect["nume"] = nume
    obiect[1] = nume
    #obiect["nume"] = nume

def get_descriere(obiect):
    """
    Da descrierea unui obiect
    :param obiect: dict
    :return:
    """
    return obiect["descriere"]
    return obiect[2]
    #return obiect["descriere"]

def set_descriere(obiect, descriere):
    """
    :param descriere: string
    :return:
    """
    obiect["descriere"] = descriere
    obiect[2] = descriere
    #obiect["descriere"] = descriere

def get_pret(obiect):
    """
    Da pretul  obiectului
    :param obiect: dict
    :return:
    """
    return obiect["pret"]
    return obiect[3]
    #return obiect["pret"]

def set_pret(obiect, pret):
    """
    :param pret: float
    :return:
    """
    obiect["pret"] = pret
    obiect[3] = pret
    # obiect["pret"] = pret

def get_locatie(obiect):
    """
    Da locatia unui obiect
    :param obiect: dict
    :return: locatie obiect - string
    """
    return obiect["locatie"]
    return obiect[4]
    #return obiect["locatie"]


def set_locatie(obiect, locatie):
    """
    :param locatie: string
    :return:
    """
    obiect["locatie"] = locatie
    obiect[4] = locatie
    #obiect["locatie"] = locatie


def format_afisare(obiect):
    return f"id: {get_id(obiect)} \n nume: {get_nume(obiect)} \n" \
           f"descriere: {get_descriere(obiect)} \n" \
           f"pret: {get_pret(obiect)}\n" \
           f"locatie: {get_locatie(obiect)}"
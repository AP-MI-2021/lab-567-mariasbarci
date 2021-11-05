from Domain.obiect import *
from Logic.crud import adaugare_obiect, get_by_id, sterge_obiect, modificare_obiect


def testAdaugaObiect():
    lista=[]
    lista=adaugare_obiect("1", "telefon", "negru", 1000, "loc1",lista)
    assert len(lista) == 1
    assert get_id(get_by_id("1",lista))=="1"
    assert get_nume(get_by_id("1",lista))=="telefon"
    assert get_descriere(get_by_id("1",lista))=="negru"
    assert get_pret(get_by_id("1",lista))== 1000
    assert get_locatie(get_by_id("1",lista))=="loc1"

def testStergeObiect():
    lista = []
    lista = adaugare_obiect("1", "telefon", "negru", 1000, "loc1", lista)
    lista=adaugare_obiect("2", "masa", "de sticla", 100, "came", lista)

    lista=sterge_obiect("1",lista)
    assert len(lista)==1
    assert get_by_id("1",lista) is None
    assert get_by_id("2", lista) is not None

    try:
        lista = sterge_obiect("100", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert get_by_id("2", lista) is not None
    except Exception:
        assert False


def testModificaObiect():
    lista = []
    lista = adaugare_obiect("1", "telefon", "negru", 1000, "loc1", lista)
    lista = adaugare_obiect("2", "carte", "verde", 80, "dulp", lista)

    lista = modificare_obiect("1", "caiet", "roz",6,"masa", lista)

    obiect_nou = get_by_id("1", lista)
    assert get_id(obiect_nou) == "1"
    assert get_nume(obiect_nou) == "caiet"
    assert get_descriere(obiect_nou) == "roz"
    assert get_pret(obiect_nou) == 6
    assert get_locatie(obiect_nou) == "masa"

    obiect_nou2 = get_by_id("2", lista)
    assert get_id(obiect_nou2) == "2"
    assert get_nume(obiect_nou2) == "carte"
    assert get_descriere(obiect_nou2) == "verde"
    assert get_pret(obiect_nou2) ==80
    assert get_locatie(obiect_nou2) == "dulp"

    lista = []
    lista = adaugare_obiect("1", "telefon", "negru", 1000, "loc1", lista)
    lista = adaugare_obiect("2", "carte", "verde", 80, "dulp", lista)
    obiect_nou = get_by_id("1", lista)
    assert get_id(obiect_nou) == "1"
    assert get_nume(obiect_nou) == "telefon"
    assert get_descriere(obiect_nou) == "negru"
    assert get_pret(obiect_nou) == 1000
    assert get_locatie(obiect_nou) =="loc1"
from Domain.obiect import *


def test_domeniu():
    obj = creare_obiect(1, "pahar", "transparent", 15, "pe tava")

    assert get_id(obj) == 1
    assert get_nume(obj) == "pahar"
    assert get_descriere(obj) == "transparent"
    assert get_pret(obj) == 15
    assert get_locatie(obj) == "pe tava"
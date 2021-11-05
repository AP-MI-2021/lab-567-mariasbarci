from Domain.obiect import creare_obiect, get_id,get_pret,get_descriere,get_locatie,get_nume



def testObiect():
    obiect = creare_obiect("1", "pahar", "transparent",4, "locd")

    assert get_id(obiect) == "1"
    assert get_nume(obiect) == "pahar"
    assert get_descriere(obiect) == "transparent"
    assert get_pret(obiect) == 4
    assert get_locatie(obiect) == "locd"
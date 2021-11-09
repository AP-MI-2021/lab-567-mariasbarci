from Domain.obiect import get_id
from Logic.crud import adaugare_obiect, modificare_obiect


def test_undo_redo():
    lista = []
    undo_list = []
    redo_list = []

    # 2. se adauga primul obiect
    rezultat = adaugare_obiect("1", "ob1", "desc1", 20.0, "loc1", lista)
    undo_list.append(lista)
    lista = rezultat

    # 3. se adauga al doilea
    rezultat = adaugare_obiect("2", "ob2", "desc2", 30, "loc2", lista)
    undo_list.append(lista)
    lista = rezultat

    # 4. se adauga al treilea
    rezultat = adaugare_obiect("3", "ob3", "desc3", 15, "loc3", lista)
    undo_list.append(lista)
    lista = rezultat

    assert get_id(lista[0]) == "1"
    assert get_id(lista[1]) == "2"
    assert get_id(lista[2]) == "3"

    # 5. primul undo scoate ultimul obiect adaugata
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert get_id(lista[1]) == "2"
    assert get_id(lista[0]) == "1"
    # assert undo_list == [[], [['1', "ob1", "desc1", 20.0, "loc1"]]]

    # 6. inca un undo scoate penultimul obiect adaugat
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert undo_list == [[]]

    # 7. inca un undo scoate primul obiect adaugat
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert undo_list == []

    # 8. inca un undo care nu face nimic
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list
    assert len(lista) == 0
    assert undo_list == []

    # 9. se adauga trei obiecte
    rezultat = adaugare_obiect("1", "ob1", "desc1", 20.0, "loc1", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()

    rezultat = adaugare_obiect("2", "ob2", "desc2", 30, "loc2", lista)
    undo_list.append(lista)
    lista = rezultat

    rezultat = adaugare_obiect("3", "ob3", "desc3", 15, "loc3", lista)
    undo_list.append(lista)
    lista = rezultat

    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3

    # 10. se face redo (fara sa faca nimic)
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3

    # 11. se fac 2 undo-uri
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert get_id(lista[1]) == "2"
    assert get_id(lista[0]) == "1"
    # assert undo_list == [[], [["1", "ob1", "desc1", 20.0, "loc1"]]]

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert undo_list == [[]]

    # 12. se face redo
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert len(lista) == 2

    # 13. se face redo
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3

    # 14. se fac 2 undo-uri
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert get_id(lista[1]) == "2"
    assert get_id(lista[0]) == "1"
    # assert undo_list == [[], [["1", "ob1", "desc1", 20.0, "loc1"]]]

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert undo_list == [[]]

    # 15. se adauga al patru lea obiect
    rezultat = adaugare_obiect("4", "ob4", "desc4", 25.50, "loc4", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()

    # 16. se face redo (fara sa faca nimic)
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert len(undo_list) == 2
    # assert undo_list == [[], [["1", "ob1", "desc1", 20.0, "loc1"]]]

    # 17. se face undo
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert len(undo_list) == 1
    assert len(redo_list) == 1

    # 18. se face undo
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert len(undo_list) == 0
    assert len(redo_list) == 2

    # 19. se face 2 redo-uri
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 1

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2
    assert len(redo_list) == 0

    # 20. se face ultimul redo, care nu face nimic
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert len(redo_list) == 0
    assert len(undo_list) == 2


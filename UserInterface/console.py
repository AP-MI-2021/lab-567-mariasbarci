from Domain.obiect import get_id, format_afisare
from Logic.crud import adaugare_obiect, modificare_obiect, get_by_id,sterge_obiect
from Logic.Functionalitati import mutare_locatie, concatenare_descriere ,ordonare_dupa_pret
import copy


def ui_adauga_obiect(lista):
    undo_lista = copy.deepcopy(lista)
    # id
    try:
        id = int(input("Introduceti id-ul:"))
        for obiect in lista:
            if get_id(obiect) == id:
                raise KeyError("Valoare repetata")
        if id <= 0:
            raise ValueError("Valoare nula id")  # inainte / pasi
    except ValueError:
        print("Valoare incorecta. Id-ul trebuie sa fie un numar intreg nenul")
        return lista, undo_lista
    except KeyError:
        print("Id-ul dat apartine deja altui obiect.")
        return lista, undo_lista
    # nume
    try:
        nume = input("Introduceti numele:")
        if len(nume) == 0:
            raise ValueError("Valoare nula nume")
    except ValueError:
        print("Valoare incorecta. Numele trebuie sa fie nenul.")
        return lista, undo_lista
    # descriere
    try:
        descriere = input("Introduceti descrierea:")
        if len(descriere) == 0:
            raise ValueError("Valoare nula descriere")
    except ValueError:
        print("Valoare incorecta. Descrierea trebuie sa fie nenula.")
        return lista, undo_lista
    # pret
    try:
        pret = float(input("Introduceti pretul:"))
        if pret < 0:
            raise ValueError
        # ValueError prinde si cazul in care se citeste un string in loc de float
    except ValueError:
        print("Pretul trebuie sa fie un numar pozitiv de tip float.")
        return lista, undo_lista
    # locatie
    try:
        locatie = input("Introduceti locatia:")
        if len(locatie) != 4:
            raise ValueError("Lungime incorecta a locatiei")
    except ValueError:
        print("Valoare incorecta. Locatia trebuie sa aiba 4 caractere.")
        return lista, undo_lista
    # returnare lista cu obiectul adaugat
    return adaugare_obiect(lista, id, nume, descriere, pret, locatie), undo_lista


def ui_sterge_obiect(lista):
    undo_lista = copy.deepcopy(lista)
    try:
        id = int(input("Introduceti id-ul obiectului pe are vreti sa il stergeti:\n"))
        if get_by_id(lista, id) is None:
            raise KeyError("Nu exista obiect cu cheia dat")
    except KeyError:
        print("Nu exista un obiect cu id-ul dat.")
        return lista, undo_lista
    # returnare lista modificata
    return sterge_obiect(lista, id), undo_lista


def ui_afisare(lista):
    for obiect in lista:
        print(format_afisare(obiect) + "\n")


def ui_modificare(lista):
    undo_lista = copy.deepcopy(lista)
    # id
    try:
        id = int(input("Introduceti id-ul obiectului pe are vreti sa il modificati:\n"))
        if get_by_id(lista, id) is None:
            raise KeyError("Nu exista obiect cu cheia data")
    except KeyError:
        print("Nu exista un obiect cu id-ul dat.")
        return lista, undo_lista
    # nume
    nume = input("Introduceti un nume nou sau nimic pentru a nu schimba:\n")
    # descriere
    descriere = input("Introduceti o descriere noua sau nimic pentru a nu schimba:\n")
    # pret
    pret = float(input("Introduceti un pret nou sau -1 pentru a nu schimba:\n"))
    # locatie
    try:
        locatie = input("Introduceti o locatie noua sau nimic pentru a nu schimba:\n")
        if locatie != "" and len(locatie) != 4:
            raise ValueError("Lungime incorecta a locatiei")
    except ValueError:
        print("Valoare incorecta. Locatia trebuie sa aiba 4 caractere.")
        return lista, undo_lista
    # returnare lista modificata
    return modificare_obiect(lista, id, nume, descriere, pret, locatie), undo_lista


def ui_mutare(lista):
    undo_lista = copy.deepcopy(lista)
    ok = False
    while ok is False:
        ok = True
        try:
            locatie1 = input("Introduceti din ce sala vreti sa mutati obiectele.\n")
            if len(locatie1) != 4:
                raise ValueError("Lungime incorecta a locatiei")

        except ValueError:
            print("Sala trebuie sa aiba 4 caractere.")
            ok = False
    ok = False
    while ok is False:
        ok = True
        try:
            locatie2 = input("Introduceti in care sala vreti sa mutati obiectele.\n")
            if len(locatie2) != 4:
                raise ValueError("Lungime incorecta a locatiei")

        except ValueError:
            print("Sala trebuie sa aiba 4 caractere.")
            ok = False
    return mutare_locatie(lista, locatie1, locatie2), undo_lista


def ui_concatenare(lista):
    undo_lista = copy.deepcopy(lista)
    try:
        pret = float(input("Introduceti pretul:"))
        if pret < 0:
            raise ValueError
        # ValueError prinde si cazul in care se citeste un string in loc de float
    except ValueError:
        print("Pretul trebuie sa fie un numar pozitiv de tip float.")
        return lista, undo_lista
    string = input("Introduceti sirul pe care vreti sa il atasati obiectelor "
                "cu pret mai mare decat valoare data.\n")
    return concatenare_descriere(lista, pret, string), undo_lista


def printare_lista_pret_locatie(dictionare):
   pass


def ui_cel_mai_mare_pret_per_locatie(lista):
   pass


def ui_ordonare_pret(lista):
   undo_lista =copy.deepcopy(lista)
   return ordonare_dupa_pret(lista) , undo_lista


def printare_suma_preturi_per_locatie(dictionare):
    pass


def ui_suma_preturi_per_locatie(lista):
   pass


def f_undo_lista(undo_lista):
    pass


def meniu_principal():
    print("1.C.R.U.D.")
    print("f.Afisare lista")
    print("2.Mutare dintr-o sala in alta")
    print("3.Concatenare un string la descriere in functie de pret")
    print("4.Afisati cel mai mare pret per fiecare locatie")
    print("5.Ordonare crescatoare lista obiectelor dupa pret")
    print("6.Afisarea sumelor prețurilor pentru fiecare locație")
    print("7.Undo")
    print("x.Iesire\n")


def meniu_crud():
    print("a.Adaugare obiect la lista")
    print("b.Stergere obiect din lista")
    print("c..Modificare unui obiect din lista")
    print("x.Inapoi\n")


def run_menu_crud(lista, undo_lista):
    meniu_crud()
    cmd = input('Alegeti o optiune:\n')
    if cmd == "a":
        lista, undo_lista=ui_adauga_obiect(lista)
        return lista, undo_lista, True
    elif cmd == "b":
        lista, undo_lista=ui_sterge_obiect(lista)
        return lista, undo_lista, True
    elif cmd == "c":
        lista,undo_lista=ui_modificare(lista)
        return lista, undo_lista, True
    elif cmd == "x":
        return lista, undo_lista, False
    else:
        print("Optiune invalida.")
        return lista, undo_lista, False


def run_menu(lista, undo_lista):
    lists = []
    while True:
        meniu_principal()
        cmd = input('Comanda:\n')
        if cmd == "1":
            lista, undo_lista, done = run_menu_crud(lista, undo_lista)
            if done == True:
                lists.append(undo_lista)
        elif cmd == "f":
            ui_afisare(lista)
        elif cmd == "2":
            lista, undo_lista = ui_mutare(lista)
            lists.append(undo_lista)
            print("Obiectele au fost mutate in sala data!")
        elif cmd == "3":
            lista, undo_lista = ui_concatenare(lista)
            lists.append(undo_lista)
            print("Sirul dat a fost concatenat la obiectele cu pret mai mare decat cel dat!")
        elif cmd == "4":
            pass
        elif cmd == "5":
            lista, undo_lista=ui_ordonare_pret(lista)
            lists.append(undo_lista)
        elif cmd == "6":
           pass
        elif cmd == "7":
            pass
        elif cmd== "x":
            break
        else:
            print("Optiune invalida.")
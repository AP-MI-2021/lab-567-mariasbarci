from Tests.Teste_functionalitati import  test_mutare_locatie, test_concatenare_descriere,test_ordonare_dupa_pret
from Tests.tests_domain import test_domeniu
from Tests.tests_logic_crud import test_adaugare_obiect,test_modificare_obiect,test_sterge_obiect


def run_all():
    test_sterge_obiect()
    test_adaugare_obiect()
    test_modificare_obiect()
    test_domeniu()
    test_mutare_locatie()
    test_concatenare_descriere()
    test_ordonare_dupa_pret()
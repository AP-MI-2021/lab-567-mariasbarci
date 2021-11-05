from Tests.Teste_functionalitati import test_concatenre_obiect,test_pretmaximloc,test_suma_preturi,test_mutare_obiecte,test_Ordonare_Pret
from Tests.tests_logic_crud import testAdaugaObiect, testStergeObiect, testModificaObiect
from Tests.tests_domain import testObiect


def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()
    test_mutare_obiecte()
    test_concatenre_obiect()
    test_pretmaximloc()
    test_Ordonare_Pret()


test_suma_preturi()
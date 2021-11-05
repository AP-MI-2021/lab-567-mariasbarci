
from Tests.run_all import runAllTests
from UserInterface.console import runMenu
from UserInterface.command_line_console import command_line_console

def main():
    lista=[]
    while True:
        optiune=input("Dati optiunea: ")
        if optiune=="1":
            lista=runMenu(lista)
        elif optiune=="2":
            command_line_console(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune invalida! Reincercati!")

runAllTests()
main()
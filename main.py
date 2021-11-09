
from Tests.run_all import runAllTests
from UserInterface.console import runMenu
from UserInterface.command_line_console import command_line_console


def print_choose_ui():
    print("1. Console")
    print("2. Command line (functionalitati limitate)")
    print("x. Iesire")

def main():
    lista=[]
    while True:
        print_choose_ui()
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
from rich.console import Console
from rich.table import Table

from add import add
from subtract import subtract
from multiply import multiply
from split import split
from advanced_add import advanced_add

console = Console()

def display_menu():
    table = Table(title="Calculadora en Python")
    table.add_column("Opción", justify="center", no_wrap=True)
    table.add_column("Operación")

    table.add_row("1", "Sumar 2 números")
    table.add_row("2", "Restar 2 números")
    table.add_row("3", "Multiplicar 2 números")
    table.add_row("4", "Dividir 2 números")
    table.add_row("5", "Sumar N números")
    table.add_row("6", "Salir")

    console.print(table)

def logic_menu(status):
    option = int(input("\nIngresa tu opción: "))
    if option == 1:
        add()
    elif option == 2:
        subtract()
    elif option == 3:
        multiply()
    elif option == 4:
        split()
    elif option == 5:
        advanced_add
        pass
    elif option == 6:
        status = False
        return status
    else:
        print("Error de sintaxis")

status = True
while status:
    display_menu()
    status = logic_menu(status)
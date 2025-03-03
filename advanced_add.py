def advanced_add():
    numbers_str = input("\nIngresa la cadena de números a sumar seguida de comas (ej. 1, 2, 3...): ")
    number_list = [int(n.strip()) for n in numbers_str.split(',')]
    total = 0
    for n in number_list:
        total += n
    print(f"El resultado de {number_list} es: {total}\n")
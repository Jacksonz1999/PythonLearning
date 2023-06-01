def suma(n1, n2):
    return n1 + n2, "La funcion retorna 2 valores"

numero_uno = int(input("Ingresa un num entero: "))
numero_dos = int(input("Ingresa un num entero: "))


resultado = suma(numero_uno,numero_dos)
print("El resultado es:",resultado)
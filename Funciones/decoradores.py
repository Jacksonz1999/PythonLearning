"""
a-> funcion principal(decorador)
b-> funcion a decorar
c-> funcion decorada

a(b) -> c
"""
def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print(">>> Antes de llamado")

        resultado = funcion_b(*args, **kwargs)

        print(">>> Despues de llamado")

        print(resultado)


    return funcion_c

@funcion_a
def saludar():
    print("Hola, nos encontramos en una funcion")

@funcion_a
def suma(numero_1 , numero_2):
    return numero_1 + numero_2

resultado =suma(10,3)
print(resultado)
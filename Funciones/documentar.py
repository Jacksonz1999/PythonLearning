# Docstring
#__doc__(Modulos,Clases,Metodos,Funciones)

def suma(numero_1 , numero_2):
    """
    La funcion suma 2 numeros enteros

    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la suma de lso parametros.

    >>> suma(10,20)
    30

    >>> suma(30,40)
    70

    TODO:
        *
    """
    return numero_1 + numero_2

#print(suma.__doc__)
#print(help(suma))


# Terminal para hacer test

    #python -m doctest documentar.py

def resta(numero_1, numero_2):
    """
    >>> resta(100,200)
    -100
    """
    return numero_1 - numero_2
    


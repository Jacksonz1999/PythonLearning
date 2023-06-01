def pares(): # Generador -> Lazy iterator
    for numero in range(0,100,2):
        yield numero # La funcion suspende su ejecucion 

        print("Se reanuda la ejecucion")
    
""" for par in pares():
    print(par) """

generador = pares()

while True:
    try:
        par = next(generador)
        print (par)
    except StopIteration:
        print("El generador finalizo.")
        break
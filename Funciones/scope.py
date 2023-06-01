#Scope
animal = "Leon" #Variable global -> Funcion, Condicion o ciclo

def imprimir_animal():
    global animal # usar la variable global
    
    #animal = "Ballena" #Variable local

    tipo = "Mamifero"  #Variable local

    print(animal)
    print(id(animal))

imprimir_animal()
print(animal)
print(id(animal))
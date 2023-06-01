""" 
e= "e" #Variable global

def function_principal():
    a = "a" #variable local superior
    b = "b" 

    def function_anidada():
        c="c" #variable local
        nonlocal b
        b = "Cambio de valor"

        print(a)
        print(b) # podemos usar variable superior
        print(id(b))
        print(e)
    function_anidada()
    print(b)
    print(id(b))

function_principal()
 """

""" def saludar():

    def mostrar_mensaje():
        print("Hola, nos encontramos en el curso de Python")

    return mostrar_mensaje

respuesta = saludar()
print(respuesta)
print(type(respuesta)) """

def saludar(username):
    mensaje = f"Hola {username}" #variable local

    def mostrar_mensaje(): #Anidada
        print(mensaje)
    
    return mostrar_mensaje

username = "Cody"
respuesta = saludar(username)

username = "Eduardo"

respuesta()
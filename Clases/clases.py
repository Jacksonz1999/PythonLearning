"""
class Usuario:
    pass #Bloque no hara nada de momento

cody = Usuario()
print(cody)
"""


#Attrs de clase

class Usuario:

    #__init__

    def inicializar(self, username, password):
        # Añadiendo attrs al objeto
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

user1.inicializar("User1","password1")
user2.inicializar("User2", "password2")
user3.inicializar("Cody","password3")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)



"""     username = "Username por default"
    email = ""

Usuario.username = "User1"
Usuario.email = "info@idk.com"

#print(Usuario.username,Usuario.email)


#Attrs de instancia

class Usuario:
    username = "Username por default"
    email = ""

#__dict__

user1 = Usuario()
user2 = Usuario()
# 1. Verifica si el attr existe dentro de objeto
# 2. Verifica si el attr existe dentro de clase. -> Lectura
# 3. Lanzar un error

user1.username = "Cody" # Añadimos el attr al objeto
user1.password = "password"
print(user1.username) #De instancia

user1.password = "1234"

print(user1.__dict__) #Dict
print(user2.password)

 """

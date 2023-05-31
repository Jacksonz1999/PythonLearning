diccionario = {"a":1,"b":2,"c":3,"d":4}

print(len(diccionario))

del diccionario["a"]
valor = diccionario.pop("b")

diccionario.clear()

print(valor)
print(diccionario)
print(len(diccionario))

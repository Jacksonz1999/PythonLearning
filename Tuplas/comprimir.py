lista  = [1,2,3,4,5,6,7] # 6,7 omitidos
tupla = (10,20,30,40,50)
lista2 = [100,200,300,400,500]
tupla2 = (1000,2000,3000,4000,5000)
resultado= zip(lista,tupla,lista2,tupla2) # -> zip
resultado = tuple(resultado)
print(resultado)
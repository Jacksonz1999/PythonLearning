# * -> Lista
# _ -> Omitir valor

numeros = (1,2,3,4,5,6,7,8,9,10)

uno, _ ,tres, cuatro,*_,nueve,diez = numeros

""" uno = numeros[0]
dos = numeros[1]
tres = numeros[2]
cuatro = numeros[3]
cinco = numeros[4] """

print(uno)

print(tres)
print(cuatro)
print(nueve)
print(diez)
#print(resto_numeros)
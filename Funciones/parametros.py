def area_circulo(radio,pi=3.14): #derecha a izquierda
    return pi * (radio ** 2)

resultado = area_circulo(pi=3.141592,radio = 10) # no importa el orden
print(resultado)
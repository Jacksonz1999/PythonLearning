""" def promedio(*args): # Tupla
    return sum(args) / len(args)

resultado = promedio(10,10,5,10,7)

print(resultado) """


def combinacion(p1,p2,*args,p4=500): #Recuerda que esto es de derecha a izquierda
    print(p1,p2,args,p4)

#combinacion(10,20,46,2,4,5,6,7,8,p4=1000)

def usuarios(**kwargs): #Dic.
    print(kwargs)
    print((type(kwargs)))

def combinacion(*args, **kwwargs):
    print(args)
    print(kwwargs)

usuarios(jackson =[10,10,10],otro=[9,9,9])
combinacion(1,2,3,4,5,cody ="String",boby =True)
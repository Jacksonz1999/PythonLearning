#labmda <parametros> : <Cuerpo de la funcion>
""" def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

mi_funcion = centigrados_a_farhenheit # type function

print(type(mi_funcion))
print(mi_funcion(10))
 """

#Convertir este funcion a labmda

funcion_grados = lambda grados : grados * 1.8 + 32

print(funcion_grados(10))

"""
sin_parametros = labmda : True
parametros_default = labmda p1=10,p2=20,p3=30 : p1 + p2 + p3
asterisco = lambda *args, **kwargs: len(args)+ len(kwargs)
"""


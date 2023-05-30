#           0       1   2   3
lista = ["String", 10,0.36,True] #list()

#La lista si puede ser solo almacene un unico valor

#                  -5        -4       -3       -2     -1
lista_cursos = ["Python", "Django","Flask", "Ruby","Java"]
lista_cursos_2 = ["C","C++","Docker"]
print(len(lista_cursos))

primer_curso = lista_cursos[0]
print(primer_curso)
segundo_curso = lista_cursos[1]
print(segundo_curso)
tercero_curso = lista_cursos[2]
print(tercero_curso)
cuarto_curso = lista_cursos[3]
print(cuarto_curso)
quinto_curso = lista_cursos[-1] #4
print(quinto_curso)


#Actualizar un elemento en una lista
lista_cursos[4] = "Rust"
print(lista_cursos)

#Sublista

#[start:end];
#[start:]-> Obtenemos los ultimos elementos de la lista
#[:end]-> Obtenemos los primeros elementos de la lista
#[start:end:skip]

sub_lista = lista_cursos[1:3]
print(sub_lista)

#Modificar Lista

#en el ultimo

lista_cursos.append("MongoDB")
lista_cursos.append("C#")
lista_cursos.append("JavaScript")

#indice particular
lista_cursos.insert(1, "Rails")
lista_cursos.insert(0, "PyGame")

#Extender
lista_cursos.extend(lista_cursos_2)
print(lista_cursos)
print(lista_cursos_2)

#Remover un string de la lista
lista_cursos.remove("MongoDB")
del lista_cursos[0]

#Eliminar toda la lista
lista_cursos.clear()
print(len(lista_cursos))


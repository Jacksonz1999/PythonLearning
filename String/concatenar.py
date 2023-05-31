nombre = "Jackson"
apellido = "Zhou"

#nombre_completo ="Mr."+ nombre + " " + apellido.

#nombre_completo = "Mr. %s %s." %(nombre,apellido)

""" nombre_completo = "Mr. {nombre} {primer_apellido}.".format(
    nombre=nombre,
    primer_apellido= apellido
    ) """
#nombre_completo = "Mr. {} {}.".format(nombre,apellido)

#FString

nombre_completo = f"Mr. {nombre} {apellido} {10*3/3}"

print(nombre_completo)

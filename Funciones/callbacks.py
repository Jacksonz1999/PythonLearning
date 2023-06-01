promedio = lambda *args : sum(args)/ len(args)

aprobatorio = lambda calificacion : calificacion >=7

def es_aprobatorio(calificacion):
    return calificacion >= 90

def mostrar_mensaje(func_promedio, *args):
    promedio = func_promedio(*args)
    
    if func_promedio(promedio):
        print(f"Has aprobado la materia con {promedio}")
    else:
        print(f"No has superado la materia")

mostrar_mensaje(promedio, es_aprobatorio ,10,8,8,9)
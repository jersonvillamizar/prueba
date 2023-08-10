dicc = {
    "undecimo": {
        "1097": {"nombre": "Brayan", "sexo": "masculino", "notas": {"nota1": 5.0, "nota2": 3.0}, "nota_promedio": 4.0},
        "1098": {"nombre": "Pedro", "sexo": "masculino", "notas": {"nota1": 3.5, "nota2": 2.5}, "nota_promedio": 3.0}
    },
    "noveno": {
        "2112": {"nombre": "Julia", "sexo": "femenino", "notas": {"nota1": 2.0, "nota2": 3.0}, "nota_promedio": 2.5},
        "11113": {"nombre": "juan", "sexo": "masculino", "notas": {"nota1": 5.0}, "nota_promedio": 5.0},
        "11114": {"nombre": "klee", "sexo": "femenino", "notas": {"nota1": 0.5}, "nota_promedio": 0.5},
        "11112": {"nombre": "lian", "sexo": "masculino", "notas": {"nota1": 1.0}, "nota_promedio": 1.0}
    },
    "decimo": {
        "3224": {"nombre": "Kamile", "sexo": "otro", "notas": {"nota1": 2.0, "nota2": 1.0, "nota3": 4.0}, "nota_promedio": 2.3333333333333335}
    }
}

# Crear una lista para almacenar las mejores notas promedio
mejores_notas = []

# Recorrer el diccionario y almacenar las notas promedio en la lista
for nivel1, nivel2 in dicc.items():
    for subllave, subvalor in nivel2.items():
        if "nota_promedio" in subvalor:
            mejores_notas.append((subvalor["nota_promedio"], nivel1, subllave, subvalor["nombre"]))

# Ordenar la lista de las mejores notas promedio en orden descendente
mejores_notas.sort(reverse=True)

# Imprimir las 5 mejores notas promedio con sus respectivas llaves, subllaves y nombres
for nota, nivel1, subllave, nombre in mejores_notas[:5]:
    print(f"Llave: {nivel1}")
    print(f"Subllave: {subllave}")
    print(f"Nombre: {nombre}")
    print(f"Nota Promedio: {nota}")
    print("-----------------")

#-------------------------------------------------------------------------------------------------------------
# Imprimir las entradas ordenadas para cada llave
for nivel1, nivel2 in dicc.items():
        print(f"Llave: {nivel1}")
        print("-----------------")
        sorted_entries = sorted(nivel2.items(), key=lambda x: x[1]["nota_promedio"], reverse=True)
        print(sorted_entries)
        for subllave, subvalor in sorted_entries:
            print(f"Subllave: {subllave}")
            print(f"Nombre: {subvalor['nombre']}")
            print(f"Nota Promedio: {subvalor['nota_promedio']}")
            print("-----------------")

#-------------------------------------------------------------------------------------------------------------
# Imprimir las dos mejores notas promedio para cada llave
for nivel1, nivel2 in dicc.items():
    if isinstance(nivel2, dict) and "nombre" in nivel2 and "nota_promedio" in nivel2:
        print(f"Llave: {nivel1}")
        print("-----------------")
        sorted_entries = sorted(nivel2.items(), key=lambda x: x[1]["nota_promedio"], reverse=True)
        for subllave, subvalor in sorted_entries[:2]:
            print(f"Subllave: {subllave}")
            print(f"Nombre: {subvalor['nombre']}")
            print(f"Nota Promedio: {subvalor['nota_promedio']}")
            print("-----------------")
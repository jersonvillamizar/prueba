estudiantes = {}
total = 0
while True:
    print("-" * 50)
    codigo = float(input("Codigo del estudiante: "))
    if codigo == 999:
        break
    nombre = input("Nombre del estudiante: ")
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("ingrese la nota 3: "))
    estudiantes[codigo] = {}
    estudiantes[codigo]["nombre"] = nombre
    estudiantes[codigo]["nota1"] = nota1
    estudiantes[codigo]["nota2"] = nota2
    estudiantes[codigo]["nota3"] = nota3

print("-" * 50)
for k in estudiantes.keys():
    total = (estudiantes[k]["nota1"] + estudiantes[k]["nota2"]  + estudiantes[k]["nota3"]) / 3
    estudiantes[k]["definitiva"] = total
    if total >= 3 :
        estudiantes[k]["Estado"] = "Aprobado"
    else:
        estudiantes[k]["Estado"] = "Reprobado"

    name = estudiantes[k]["nombre"]
    status = estudiantes[k]["Estado"] 
    note = estudiantes[k]["definitiva"]
    
    print(f"el estudiante {name} {status} con nota de: {note:.2}")
    print("-" * 50)
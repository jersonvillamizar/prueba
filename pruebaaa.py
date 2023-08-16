import json
import os
os.system("clear")

with open("Simulacro/PetShopping.json", "r") as archivo:
    dicc = json.load(archivo)
    nuevos = {}
    opciones = "tipo"
    unico = []
    for mascotas in dicc["pets"]:
        for llaves in mascotas.keys():
            if llaves == str(opciones):
                unico.append(mascotas[f"{opciones}"]) 
    unico = tuple(unico)
    print("\nPuede escoger una de las opciones ya creadas o realizar una nueva: ")
    j = 0
    for i in unico:
        j += 1
        print(f"{j} - {i}")
    fijar = input("Ingrese el numero de las opciones, de lo contrario se creará una nueva: ")
    if 0 < fijar < j:
        return unico[fijar-1]
    else: 
        return input("Ingrese la nueva raza")



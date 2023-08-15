import json
import os
os.system("clear")
dicc = {}
dicc["Vendedores"] = []
contador = 0
with open('15_08_23_review/texto.txt', 'r') as f:
    for linea in f:
        contador += 1
        if contador > 1:
            linea = linea.strip().split(',')
            ventas = {}
            ventas["Apellido"] = linea[0]
            ventas["Id"] = linea[1]
            ventas["Ventas"] = linea[2:]
            dicc["Vendedores"].append(ventas)
    with open('15_08_23_review/vendedores.txt', 'w') as f:
        json.dump(dicc, f)
        print(" Se ha creado el archivo vendedores.txt ".center(100,"-") + "\n")

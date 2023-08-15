import json
import os
os.system("clear")
dicc = {}
dicc["Vendedores"] = []
contador = 0
with open('texto.txt', 'r') as f:
    for linea in f:
        contador += 1
        if contador > 1:
            linea = linea.strip().split(',')
            ventas = {}
            ventas["Apellido"] = linea[0]
            ventas["Id"] = linea[1]
            ventas["Ventas"] = []
            for i in range(2, len(linea)):
                ventas["Ventas"].append(linea[i])
            dicc["Vendedores"].append(ventas)
    with open('vendedores.txt', 'w') as f:
        json.dump(dicc, f)
        print(" Se ha creado el archivo vendedores.txt ".center(100,"-") + "\n")

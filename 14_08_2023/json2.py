import json 
import os

data = {}
try:
    with open("14_08_2023/jugadores.json", "r") as archivo:
        data = json.load(archivo)
except:
    with open("14_08_2023/jugadores.json", "w") as archivo:
        pass

contador = 0
for i in data.keys():
    contador += 1

os.system("clear")
print("\nEl programa se cierra si el nombre no contiene nada o al final con la opcion de salida")
input("Presione cualquier tecla para continuar al programa: ")
while True:
    os.system("clear")
    contador += 1
    data[contador] = {}
    data[contador]["nombre"] = str(input("\nIngrese el nombre: "))
    data[contador]["edad"] = int(input("Ingrese la edad: "))
    data[contador]["peso"] = float(input("Ingrese su peso: "))
    if data[contador]["nombre"].isspace() or data[contador]["nombre"] == "":
        with open("14_08_2023/jugadores.json", "w") as fd:
            json.dump(data, fd)
        exit()
    salir = str(input(("\nPresione cualquier tecla para continuar o ingrese 'S' para salir: ")))
    if salir.lower() == "s":
        with open("14_08_2023/jugadores.json", "w") as fd:
            json.dump(data, fd)
        exit()



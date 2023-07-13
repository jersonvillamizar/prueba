import json

with open("12_07_2023/lista.json", "r") as archivo:
    lista = json.load(archivo)

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

for elem in lista:
    print(elem, end=", ")
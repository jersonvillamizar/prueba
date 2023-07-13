import json

with open("12_07_2023/diccionario.json", "r") as archivo:
    diccionario = json.load(archivo)

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

print("Diccionario", diccionario)
print("\nDiccionario[Influencers][1][name]:", diccionario["influencers"][1]["name"])
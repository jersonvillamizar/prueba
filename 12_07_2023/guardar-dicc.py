import json

dicc2 = {1:"Lapiz", 2:"Borrador", 3:"Cuaderno", 4:"Lapicero", "Valor":2500}

""" dicc2 = {
    "influencers": [
        {
            "name": "Jaxon",
            "edad": "42",
            "work at": "Tech News"
        },
        {
            "name": "Miller",
            "edad": "35",
            "work at": "IT Day"
        }
    ]
} """

with open("12_07_2023/diccionario.json", "w") as archivo:
    # json.dump(dicc, archivo)
    json.dump(dicc2, archivo)
    print("Se ha escrito en disco")

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

print("Se ha cerrado el archivo")
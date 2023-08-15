import json

with open("14_08_2023/Ahorradores.json", "r") as archivo:
    data = json.load(archivo)

lista = []
contador = 0
for i in range(len(data["cliente"])):
    if data["cliente"][i]["Saldo"] > 35_000_000 :
        contador += 1
        lista.append({
            "Contador": contador, 
            "NumCuenta": data["cliente"][i]["NumCuenta"], 
            "Saldo": data["cliente"][i]["Saldo"]
            })

with open("14_08_2023/Dian.json", "w") as fd:
    json.dump(lista, fd)
with open("11_08_23/datos.txt", "r") as fd:
    with open("11_08_23/datos_destino.txt", "w") as fd2:
        for linea in fd:
            lista = linea.strip().split(",")
            total = 0
            fd2.write(",".join(lista))
            for i in range (1, len(lista)):
                total += int(lista[i])
            total = total / len(lista)
            fd2.write(f"**{round(total, 2)}\n")
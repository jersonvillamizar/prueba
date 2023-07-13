#encoding="utf-8"
import io

#abrirlo

#if linea.starswitch("FROM"):

""" fd = open("JersonVillamizar/10_07_2023/mbox-short.txt", "r")
cont = 0
for linea in fd:
    cont += 1
fd.close()

print(f"Cantidad de lineas: {cont}") """

""" fd = open("JersonVillamizar/10_07_2023/mbox-short.txt", "r")
cont = 0
for linea in fd:
    if "from" in linea.lower():
        cont += 1
fd.close()

print(f"Cantidad de lineas que inicia con From: {cont}")  """

""" fd = open("JersonVillamizar/10_07_2023/mbox-short.txt", "r")
cont = 0
for linea in fd:
    line = linea.rstrip()
    if not "@uct.ac.za" in linea :
        continue
    print(line)
fd.close() """

""" fd = open("JersonVillamizar/10_07_2023/mbox-short.txt", "r")
cont = 0
for linea in fd:
    if "Subject" in linea:
        cont += 1
fd.close()

print(f"Cantidad de lineas que inicia con From: {cont}")  """

#fd = open("JersonVillamizar/10_07_2023/prueba2.txt", "w")  #Crear archivo
#lst = ["Primera linea\n", "Segunda linea\n"]
#fd.writelines(lst)
""" fd.write("Primera linea\n")
fd.write("Segunda linea\n") """
#fd.close
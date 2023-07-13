#Dado nombre de la compañia imprima las 3 letras mas comunes
contador = 0

def validacion_t(msg):
    while True:
        try:
            texto = input(msg)
            if texto.isalpha() or not texto.isspace():
                return texto
            else:
                print("-" * 50)
                print("Solo se permiten letras")
                print("-" * 50)
        except Exception as e:
            print("-" * 50)
            print(f"{e}")
            print("-" * 50)

def validacion(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero

        except ValueError:
            print("-" * 50)
            print("Solo se permiten numeros enteros")
            print("-" * 50)
        except Exception as e:
            print("-" * 50)
            print(f"{e}")
            print("-" * 50)

nombre_compañia = validacion_t("Ingrese el nombre de la compañia: ")
nombre_compañia = nombre_compañia.replace(" ","")
lista = list(nombre_compañia)

letra1 = lista.count(lista[0])
nombre1 = ""
letra2 = lista.count(lista[0])
nombre2 = ""
letra3 = lista.count(lista[0])
nombre3 = ""
mayor = ""

dicc = {}

for k in lista:
    dicc[k] = lista.count(k)

print("La cantidad de veces repetidas una palabra se ve en: ")
print(dicc)
lista2 = []

for i in dicc.keys():

    lista2.append(i)

lista2 = sorted(lista2)

print("Ordenando alfabeticamente")
print(lista2)


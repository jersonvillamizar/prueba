#Dado nombre de la compañia imprima las 3 letras mas comunes
contador = 0

def validacion_t(msg):
    while True:
        try:
            texto = input(msg)
            if texto.isalpha() or not texto.isspace():
                return texto
            else:
                print("-" * 100)
                print("Solo se permiten letras")
                print("-" * 100)
        except Exception as e:
            print("-" * 100)
            print(f"{e}")
            print("-" * 100)

print("-" * 100)
nombre_compañia = validacion_t("Ingrese el nombre de la compañia: ")
nombre_compañia = nombre_compañia.replace(" ","")
lista = list(nombre_compañia)
print(lista)

dicc = {}

for k in lista:
    dicc[k] = lista.count(k)

print(dicc)
    
ordenado = sorted(dicc.keys(), key = lambda x: (-dicc[x], x))[:3]

print("-" * 100)
print(f"Las 3 letras más repetidas son: {ordenado}")
print("-" * 100)
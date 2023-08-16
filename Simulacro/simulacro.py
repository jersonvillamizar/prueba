import json
import os

os.system("clear")

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

def validacion_f(msg):
    while True:
        try:
            numero = float(input(msg))
            return numero

        except ValueError:
            print("-" * 50)
            print("Solo se permiten numeros enteros o decimales")
            print("-" * 50)
        except Exception as e:
            print("-" * 50)
            print(f"{e}")
            print("-" * 50)

def cargar_ruta(ruta):    
    with open(ruta, "r") as archivo:
        dicc = json.load(archivo)
    return dicc

def escribir_en_disco(ruta, dicc):
    with open(ruta, "w") as archivo:
        json.dump(dicc, archivo)
    if not archivo.closed:
        archivo.close()

def menu():
    print("\n")
    print(" PET SHOPPING ".center(100,"="))
    print(" MENU ".center(100,"="))
    print("1 - MOSTRAS MASCOTAS DISPONIBLES")
    print("2 - NUEVA MASCOTA")
    print("3 - DATOS DE MASCOTA")
    print("4 - ACTUALIZAR DATOS DE MASCOTA")
    print("5 - ELIMINAR MASCOTA")
    print("6 - SALIR")
    print("\n")

def escoger(opcion):
    print("\n")
    mascotas = {1: mostrar_mascota, 2: nueva_mascota, 3: datos, 4: modificar_mascota, 5: eliminar_mascota, 6: salida}
    mascotas[opcion](dicc)
    if 7 < opcion < 1:
        print("Opción inválida. Intente nuevamente.")

def mostrar_mascota(dicc):
    print("|"+"TIPO".center(15, " ")+"|"+"RAZA".center(20, " ")+"|"+"PRECIO".center(15, " ")+"|"+"SERVICIOS".center(40, " ")+"|")
    for mascotas in dicc["pets"]:
        tipo = mascotas["tipo"]
        raza = mascotas["raza"]
        precio = mascotas["precio"]
        lista = mascotas["servicios"]
        servicios = ", ".join(lista)
        print("|"+tipo.center(15, " ")+"|"+raza.center(20, " ")+"|"+str(precio).center(15, " ")+"|"+servicios.title().center(40, " ")+"|")

def nueva_mascota(dicc):
    nuevos = {}
    nuevos["tipo"] = recorrer(dicc, "tipo")
    nuevos["raza"] = recorrer(dicc, "raza")
    nuevos["talla"] = recorrer(dicc, "talla")
    nuevos["precio"] = recorrer(dicc, "precio")
    nuevos["servicios"] = rec_serv(dicc, "servicios")
    return dicc["pets"].append(nuevos)
    
    

def recorrer(dicc, opciones):
    unico = []
    for mascotas in dicc["pets"]:
        for llaves in mascotas.keys():
            if llaves == str(opciones):
                unico.append(mascotas[f"{opciones}"]) 
    tupla = set(unico)
    unico = []
    for k in tupla:
        unico.append(k)
    print("\nPuede escoger una de las opciones ya creadas o realizar una nueva: ")
    j = 0
    for i in unico:
        j += 1
        print(f"{j} - {i}")
    fijar = input("\nIngrese el numero de las opciones, de lo contrario se creará una nueva: ")
    if 0 < fijar < j+1:
        return unico[fijar-1]
    else: 
        return input("Ingrese la nueva opcion: ")
        
def rec_serv(dicc, opciones):
    unico = []
    for mascotas in dicc["pets"]:
        for servi in mascotas["servicios"]:
            unico.append(servi) 
    unico = tuple(unico)
    devolver = []
    print("\nAquí se muestran los servicios disponibles: ")
    j = 0
    for i in unico:
        j += 1
        print(f"{j} - {i}")
    while True:
        fijar = validacion("\nIngrese el numero de el servicio que desea ingresar: ")
        if 0 < fijar < j+1:
            devolver.append(unico[fijar])
            cortar = validacion_t("Desea agregar otra opcion? Cualquier tecla para continuar o N para salir")
            if cortar.lower() == "n":
                return devolver
        else:
            print("Opcion no valida".center(100, "*"))
        
def datos(dicc):
    pass

def modificar_mascota(dicc):
    pass

def eliminar_mascota(dicc):
    pass

def salida():
        salir = validacion_t("Presione cualquier tecla para salir o ingrese 'R' para regresar: ")
        if not salir.lower() == "r":
            exit()

ruta = "Simulacro/PetShopping.json"

while True:
    dicc = cargar_ruta(ruta)
    input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
    menu()
    escoger(validacion("Opcion 1 a 6: "))
    print("\n")
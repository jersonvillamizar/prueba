import json
from datetime import date

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

def crear_diccionario(dicc, id_cliente):
            try:
                for llaves in dicc.keys():
                    if llaves == id_cliente:
                        break
                    else:
                        dicc[id_cliente] = {}
                        break
                dicc[id_cliente] = {}
            except:
                dicc[id_cliente] = {}

def menu():
    print("\n")
    print("*** TIENDA ACME ***")
    print("MENU")
    print("1- CLIENTES")
    print("2- PRODUCTOS")
    print("3- SALIR")
    print("\n")

def escoger(opcion):
    if opcion == 1:
        print("CLIENTES".center(100,"="))
        id_cliente = validacion("Ingrese el ID del cliente: ")
        ingresar_clientes(dicc, id_cliente)
    elif opcion == 2:
        print("PRODUCTOS".center(100,"="))
        id_cliente = validacion("Ingrese el ID del cliente: ")
        ingresar_productos(dicc, id_cliente)
    elif opcion == 3:
        print("¡Hasta luego!".center(100,"="))
        salir = validacion_t("Presione cualquier tecla para salir o ingrese 'M' para regresar: ")
        if not salir.lower() == "m":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")

def cargar_ruta(ruta):    
    dicc = {}
    try:
        with open(ruta, "r") as archivo:
            leer_dicc = json.load(archivo)
            for llaves in leer_dicc.keys():
                id_cliente = int(llaves)
                dicc[id_cliente] = {}
                dicc[id_cliente] = leer_dicc[llaves]
        return dicc
    except:
        with open(ruta, "w") as archivo:
            return dicc

def escribir_en_disco(ruta, dicc):
    with open(ruta, "w") as archivo:
        json.dump(dicc, archivo)
        print("Se ha escrito en disco")

    if not archivo.closed:
        print("Cerrando archivo")
        archivo.close()

def ingresar_clientes(dicc, id_cliente):
    while True:        
        for llaves in dicc.keys():
            if llaves == id_cliente:
                return print("\nYa existe un cliente con ese ID".center(100,"="))   
        crear_diccionario(dicc, id_cliente)
        nombre = validacion_t("Ingrese el nombre del cliente: ")
        dicc[id_cliente]["nombre"] = nombre 

        ciclo_p = validacion_t("\nCualquier tecla para AGREGAR otro cliente, NO para volver al menú: ")
        if ciclo_p.lower().strip() == "no":
            return dicc

def ingresar_productos(dicc, id_cliente):
    dicc_productos = {}
    while True:
        id_producto = validacion("Ingrese el codigo del producto: ")
        try:
                for llaves in dicc[id_cliente].keys():
                    if llaves == "compras":
                        break
                    else:
                        dicc[id_cliente]["compras"] = {}
                        dicc[id_cliente]["compras"]["cantidad"] = 1
                        break
                dicc[id_cliente]["compras"] = {}
                dicc[id_cliente]["compras"]["cantidad"] = 1
        except:
                dicc[id_cliente]["compras"] = {}
                dicc[id_cliente]["compras"]["cantidad"] = 1
        valor = validacion("Ingrese el valor del producto: ")
        cantidad = validacion("Ingrese la cantidad comprada: ")
        while True: 
            dicc_iva = {1:0, 2:5, 3:19}
            iva_condicion= validacion("Ingrese opcion 1,2 ó 3 para IVA(1:Exento, 2:Bienes ó 3:General): ")
            if 0 < iva_condicion < 4:
                iva = dicc_iva[iva_condicion]
                break
            else:
                print("Opcion inválida".center(100,"="))

        dicc_productos[id_producto] = {}
        dicc_productos[id_producto]["valor"] = valor 
        dicc_productos[id_producto]["cantidad"] = cantidad 
        dicc_productos[id_producto]["iva"] = iva 
        
        ciclo_p = validacion_t("Cualquier tecla para AGREGAR otro producto, NO para volver al menú: ")
        if ciclo_p.lower().strip() == "no":
            compras_r = dicc[id_cliente]["compras"]["cantidad"]
            dicc[id_cliente]["compras"][compras_r] = {}
            dicc[id_cliente]["compras"][compras_r] = dicc_productos
            compras_r += 1
            dicc[id_cliente]["compras"]["cantidad"] = compras_r
            return dicc_productos

fecha = date.today()
ruta = f"13_07_2023\emlacme_{fecha}.json"

while True:
  dicc = cargar_ruta(ruta)
  input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
  menu()
  escoger(validacion("Opcion 1 a 3: "))
  print("\n")






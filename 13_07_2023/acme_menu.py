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
    print("3- VENTAS")
    print("4- SALIR")
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
        print("TOTAL DEL DIA".center(100,"="))
        total_dia(lista)
    elif opcion == 4:
        print("¡Hasta luego!".center(100,"="))
        salir = validacion_t("Presione cualquier tecla para salir o ingrese 'M' para regresar: ")
        if not salir.lower() == "m":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")

def cargar_ruta(ruta):    
    lista = []
    try:
        with open(ruta, "r") as archivo:
            lista = json.load(archivo)
        return lista
    except:
        with open(ruta, "w") as archivo:
            return lista

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
        valor = validacion("Ingrese el valor del producto: ")
        cantidad = validacion("Ingrese la cantidad comprada: ")
        while True: 
            dicc_iva = {1:0, 2:0.05, 3:0.19}
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
        
        ciclo_p = validacion_t("\nCualquier tecla para AGREGAR otro producto, NO para volver al menú: ")
        print("\n")
        print(f"ID cliente: {id_cliente}".center(100, "="))
        if ciclo_p.lower().strip() == "no":
            lista = cargar_ruta(ruta)
            print(lista)
            if lista:
                guardar_cantidad = lista[0]
                guardar_total = lista[1]
                guardar_total2 = lista[2]
                guardar_iva = lista[3]
            else:
                guardar_cantidad = 0
                guardar_total = 0
                guardar_total2 = 0
                guardar_iva = 0

            for llaves in dicc_productos.keys():
                id = llaves
                valor = dicc_productos[id_producto]["valor"] 
                cantidad = dicc_productos[id_producto]["cantidad"] 
                iva = dicc_productos[id_producto]["iva"]
                total = valor * cantidad
                iva_t = iva*total
                total2 = total + iva_t
                print(f"\nProducto: {id}, Valor: {total}, Iva: {iva_t}, TOTAL: {total2}")
                guardar_cantidad += cantidad
                guardar_total += total
                guardar_total2 += total2
                guardar_iva += iva_t
            lista.clear()
            lista = [guardar_cantidad, guardar_total, guardar_total2, guardar_iva]
            escribir_en_disco(ruta, lista)
            return lista

def total_dia(lista):
    total_vendidos = lista[0]
    valor_siniva = lista[1]
    valor_iva = lista[3]
    valor_tiva = lista[2]
    print(f"\nCantidad de productos vendidos: {total_vendidos}")
    print(f"Total sin iva: {valor_siniva}")
    print(f"Valor total del IVA: {valor_iva}")
    print(f"Valor total productos con iva: {valor_tiva}")

fecha = date.today()
ruta = f"13_07_2023\emlacme_{fecha}.json"
dicc = {}
while True:
  lista = cargar_ruta(ruta)
  input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
  menu()
  escoger(validacion("Opcion 1 a 4: "))
  print("\n")






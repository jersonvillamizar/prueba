#{id:{"nombre":'jerson',"compras":{"cantidad":85, 1:{id_producto:{}}}}}
#dicc[id_cliente]["compras"][compras_r] = {}

#import json

"""from datetime import date

ahora = date.today()
print(ahora)"""

"""fecha = input("Ingrese la fecha: ")
ruta = f"13_07_2023\emlacme_{fecha}.json"
print(ruta)
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
            return dicc"""
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

def ingresar_productos(dicc, id_cliente):
    dicc_productos = {}
    while True:
        id_producto = validacion("Ingrese el codigo del producto: ")
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
        dicc[id_cliente]["productos"] = dicc_productos

        ciclo_p = validacion_t("Cualquier tecla para AGREGAR otro producto, NO para volver al menú: ")
        if ciclo_p.lower().strip() == "no":
            return dicc_productos

"""dicc = {}
id_cliente = validacion("Ingrese el ID del cliente: ")
dicc[id_cliente] = {}
dicc[id_cliente]["productos"] = {}
ingresar_productos(dicc,id_cliente)

print(dicc)"""

"""for clientes in dicc.keys():
            if id_cliente == clientes:
                return print("Ya existe un cliente con ese ID")"""
"""def crear_diccionario(dicc, id_cliente):
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

def ingresar_clientes(dicc):
    while True:
        id_cliente = validacion("Ingrese el ID del cliente: ")
        crear_diccionario(dicc, id_cliente)

        nombre = validacion_t("Ingrese el nombre del cliente: ")
        dicc[id_cliente]["nombre"] = nombre 

        ciclo_p = validacion_t("Cualquier tecla para AGREGAR otro cliente, NO para volver al menú: ")
        if ciclo_p.lower().strip() == "no":
            return dicc
        """
"""dicc = {}
print(dicc)
ingresar_clientes(dicc)
print(dicc)"""
import json

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
    dicc = {}
    try:
        with open(ruta, "r") as archivo:
            dicc = json.load(archivo)
        return dicc
    except:
        with open(ruta, "w") as archivo:
            return dicc

def escribir_en_disco(ruta, dicc):
    with open(ruta, "w") as archivo:
        json.dump(dicc, archivo)
    if not archivo.closed:
        archivo.close()

def comprobar_dicc(dicc, id_cliente):
    try:
        if dicc[id_cliente]:
            return False
        else:
            dicc[id_cliente] = {}
    except:
        dicc[id_cliente] = {}

    return dicc

def comprobar_dicc1(dicc, tipo, id_tarjeta):
    try:
        for tipos in dicc.keys():
            for tarjetas in dicc[tipos].keys():
                if int(tarjetas) == id_tarjeta:
                    return False
        dicc[tipo][id_tarjeta] = {}
    except:
        dicc[tipo][id_tarjeta] = {}

    return dicc

def telefono_val():
    while True:
            telefono = validacion("Ingrese el numero de telefono de cliente(10 digitos): ")
            if len(str(telefono).strip()) == 10:
                return telefono
            else: 
                print("No contiene 10 digitos")

def menu():
    print("\n")
    print(" INSTITUCION BANCARIA ACME ".center(100,"="))
    print(" MENU ".center(100,"="))
    print("1 - CLIENTES")
    print("2 - TARJETAS")
    print("3 - INFORMES")
    print("4 - SALIR")
    print("\n")

def menu_tarjetas():
    print(" MENU ".center(100,"="))
    print("1 - Añadir")
    print("2 - Modificar")
    print("3 - Eliminar")
    print("4 - Regresar al menú")
    print("\n")

def escoger(opcion):
    print("\n")
    if opcion == 1:
        print("CLIENTES".center(100,"="))
        ingresar_cliente(dicc_clientes)

    elif opcion == 2:
        ciclo = True
        while ciclo != 4:
            input("\nPresione cualquier tecla para continuar al menú TARJETAS: ")
            dicc = cargar_ruta(ruta)
            print("TARJETAS".center(100,"="))
            menu_tarjetas()
            ciclo = escoger_tarjetas(validacion("Opcion 1 a 6: "), dicc)

    elif opcion == 3:
        ciclo = True
        while ciclo != 6:
            input("\nPresione cualquier tecla para continuar al menú INFORMES: ")
            dicc = cargar_ruta(ruta)
            print("INFORMES".center(100,"="))
            menu_informes()
            ciclo = escoger_informes(validacion("Opcion 1 a 6: "), dicc, dicc_clientes)

    elif opcion == 4:
        print("¡Hasta luego!".center(100,"="))
        salir = validacion_t("Presione cualquier tecla para salir o ingrese 'R' para regresar: ")
        if not salir.lower() == "r":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")

def menu_informes():
    print(" MENU ".center(100,"="))
    print("1 - Tarjetas de un cliente")
    print("2 - Informacion de tarjeta")
    print("3 - Listado de tarjetas")
    print("4 - Clientes con tarjetas")
    print("5 - Cantidad de cierto tipo de tarjetas")
    print("6 - Regresar al menú")
    print("\n")

def escoger_tarjetas(opcion, dicc):
    print("\n")
    if opcion == 1:
        print(" Ingresar tarjeta ".center(50,"="))
        ingresar_tarjetas(dicc)
    elif opcion == 2:
        print(" Modificar tarjeta ".center(50,"="))
        modificar_tarjeta(dicc)
    elif opcion == 3:
        print(" Eliminar tarjeta ".center(50,"="))
        eliminar_tarjeta(dicc)
    elif opcion == 4:
        print(" Regresando al menú ".center(50,"="))
        salir = validacion_t("Presione cualquier tecla para ir a menú principal o ingrese 'R' para regresar: ")
        if not salir.lower() == "r":
            return opcion
    else:
        print("Opción inválida. Intente nuevamente.")

def escoger_informes(opcion, dicc, dicc_clientes):
    print("\n")
    if opcion == 1:
        print(" Tarjetas de un cliente ".center(50,"="))
        tarjetas_cliente(dicc, dicc_clientes)
    elif opcion == 2:
        print(" Informacion de tarjeta ".center(50,"="))
        info_tarjeta(dicc, dicc_clientes)
    elif opcion == 3:
        print(" Listado de tarjetas ".center(50,"="))
        listado_tarjeta(dicc, dicc_clientes)
    elif opcion == 4:
        print(" Clientes con tarjetas ".center(50,"="))
        listado_cliente(dicc, dicc_clientes)
    elif opcion == 5:
        print(" Cantidad de cierto tipo de tarjetas ".center(50,"="))
        cantidad_tipo(dicc, dicc_clientes)
    elif opcion == 6:
        print(" Regresando al menú ".center(50,"="))
        salir = validacion_t("Presione cualquier tecla para ir a menú principal o ingrese 'R' para regresar: ")
        if not salir.lower() == "r":
            return opcion
    else:
        print("Opción inválida. Intente nuevamente.")

def opcional(curso, msg):
    while True:
        grado = validacion(msg)
        if 0 < grado < 4:
            grado = curso[grado]
            return grado
        else:
            print("*****Opcion invalida*****")

def opcional_global(minimo, maximo, msg):
    while True:
        num_valido = validacion(msg)
        if minimo < num_valido < maximo:
            return num_valido
        else:
            print(f"*****El rango es desde {minimo+1} hasta {maximo-1} *****")

def ingresar_cliente(dicc_clientes):
    id_cliente = validacion("Ingrese la ID del cliente: ")
    existente = True
    existente = comprobar_dicc(dicc_clientes, id_cliente)
    if not existente:
        return print("*****Ya se ha ingresado este ID de cliente*****")
    nombre = validacion_t("Ingrese el nombre del cliente: ")
    telefono = telefono_val()
    genero = {1: "masculino", 2: "femenino", 3: "otro"}
    sexo = opcional(genero, "Genero 1:Masculino, 2:Femenino, 3:Otro -> ")
    dicc_clientes[id_cliente]["nombre"] = nombre
    dicc_clientes[id_cliente]["telefono"] = telefono
    dicc_clientes[id_cliente]["sexo"] = sexo
    escribir_en_disco(ruta2, dicc_clientes)
    print("Proceso realizado".center(50, "-"))

def ing_id_cl():
        while True:
            id_cli = validacion("A que ID de cliente pertenece la tarjeta: ")
            if dicc_clientes:
                for ids in dicc_clientes.keys():
                    if int(ids) == id_cli:
                        return id_cli
                return print("*****No se ha ingresado ese ID en cliente*****")

            else:
                return print("*****No ha ingresado clientes*****")

def ingresar_tarjetas(dicc):
    tipos_tarjetas = {1: "Master Card", 2: "Visa", 3: "American Express"}
    tipo = opcional(tipos_tarjetas, "Tipo de tarjeta = 1:Master Card, 2:Visa, 3:American Express = ")
    comprobar_dicc(dicc, tipo)
    id_tarjeta = validacion("Ingrese la ID de la tarjeta: ")
    existente = True
    existente = comprobar_dicc1(dicc, tipo, id_tarjeta)
    if not existente:
        return print("*****Ya se ha ingresado este ID de tarjeta*****")
    mes = opcional_global(0, 13, "Ingrese el MES de validez(1-12): ")
    año = opcional_global(2022, 2034, "Ingrese el AÑO de validez(2023-2033): ")
    codigo = opcional_global(99, 1000, "Ingrese el codigo de verificacion(100-999): ")
    id_cli = ing_id_cl()
    if dicc_clientes:
        dicc[tipo][id_tarjeta]["mes"] = mes
        dicc[tipo][id_tarjeta]["age"] = año
        dicc[tipo][id_tarjeta]["codigo"] = codigo
        dicc[tipo][id_tarjeta]["id_cliente"] = id_cli
        escribir_en_disco(ruta, dicc)
        print("Proceso realizado".center(50, "-"))

def buscar_tarjeta(dicc):
    encontrado = False
    if dicc:
        id_tarjeta = validacion("\nIngrese el ID de la tarjeta a buscar: ")
        try:
            for tipos in dicc.keys():
                for tarjetas in dicc[tipos].keys():
                    if int(tarjetas) == id_tarjeta:
                        encontrado = True
                        print(f"ID:{id_tarjeta} - Tipo:{tipos}")
                        return (encontrado, tarjetas, tipos)
            if not encontrado:
                print("*****No se encontró ninguna tarjeta con el ID ingresado.*****")
        except:
            print("*****No se han ingresado tarjetas.*****")
    else: 
        print("*****No se han ingresado tipos de tarjeta.*****")

def buscar_cliente(dicc):
    encontrado = False
    if dicc:
        id_clientes = validacion("\nIngrese el ID del cliente a buscar: ")
        try:
            for id_cliente in dicc.keys():
                if int(id_cliente) == id_clientes:
                    encontrado = True
                    return (id_clientes)
            if not encontrado:
                print("*****No se encontró ningun cliente con el ID ingresado.*****")
        except:
            print("*****No se han ingresado clientes.*****")
    else: 
        print("*****No se han ingresado clientes.*****")

def modificar_tarjeta(dicc):
    encontrado = False
    try:
        (encontrado, id_tarjeta, tipos)  = buscar_tarjeta(dicc)
        if encontrado:
            dicc[tipos].pop(id_tarjeta)
            ingresar_tarjetas(dicc)
    except:
        print("Volviendo al menú...")
    escribir_en_disco(ruta, dicc)

def eliminar_tarjeta(dicc):
    encontrado = False
    try:
        (encontrado, id_tarjeta, tipos)  = buscar_tarjeta(dicc)
        if encontrado:
            dicc[tipos].pop(id_tarjeta)
            print("Proceso realizado".center(50, "-"))
    except:
        print("Volviendo al menú...")
    escribir_en_disco(ruta, dicc)

def tarjetas_cliente(dicc, dicc_clientes):
    cliente = buscar_cliente(dicc_clientes)
    cliente_str = str(cliente)
    nombre = dicc_clientes[cliente_str]["nombre"]
    print(f"ID:{cliente}, Nombre:{nombre}")
    for tipo in dicc.keys():
        for id_tarjetas in dicc[tipo].keys():
            if dicc[tipo][id_tarjetas]["id_cliente"] == cliente:
                print(f"Tarjeta {tipo} - {id_tarjetas}")

def info_tarjeta(dicc, dicc_clientes):
    encontrado = False
    try:
        (encontrado, id_tarjeta, tipos)  = buscar_tarjeta(dicc)
        if encontrado:
            mes = dicc[tipos][id_tarjeta]["mes"] 
            año = dicc[tipos][id_tarjeta]["age"] 
            codigo = dicc[tipos][id_tarjeta]["codigo"] 
            id_cli  = dicc[tipos][id_tarjeta]["id_cliente"]
            print(f"Mes y año de validacion:{mes} / {año} - codigo:{codigo} - ID cliente: {id_cli}")
            nombre = dicc_clientes[str(id_cli)]["nombre"] 
            telefono = dicc_clientes[str(id_cli)]["telefono"] 
            sexo = dicc_clientes[str(id_cli)]["sexo"] 
            print(f"Nombre cliente:{nombre}, telefono:{telefono}, sexo:{sexo}")
    except:
        print("Volviendo al menú...")

def listado_tarjeta(dicc, dicc_clientes):
    for tipos in dicc.keys():
        for id_tarjetas in dicc[tipos].keys():
            mes = dicc[tipos][id_tarjetas]["mes"] 
            año = dicc[tipos][id_tarjetas]["age"] 
            id_cli  = dicc[tipos][id_tarjetas]["id_cliente"]
            nombre = dicc_clientes[str(id_cli)]["nombre"]
            print(f"\nTarjeta {tipos} - {id_tarjetas}")
            print(f"Mes y año: {mes} / {año} ")
            print(f"ID cliente: {id_cli} - Nombre: {nombre}")

def listado_cliente(dicc, dicc_clientes):
    lista = []
    for tipos in dicc.keys():
        for id_tarjetas in dicc[tipos].keys():
            id_cli  = dicc[tipos][id_tarjetas]["id_cliente"]
            lista.append(id_cli)
    unico = set(lista)
    for i in unico:
        nombre = dicc_clientes[str(id_cli)]["nombre"]
        telefono = dicc_clientes[str(id_cli)]["telefono"]
        print(f"ID cliente: {i} - Nombre: {nombre} - telefono: {telefono}")
                
def cantidad_tipo(dicc, dicc_clientes):
    tipos_tarjetas = {1: "Master Card", 2: "Visa", 3: "American Express"}
    tipo = opcional(tipos_tarjetas, "Tipo de tarjeta = 1:Master Card, 2:Visa, 3:American Express = ")
    contador = 0
    try:
        for tarjetas in dicc[tipo].keys():
            contador += 1
        print(f"La cantidad de tarjetas tipo {tipo} son {contador}")
    except:
        print(f"No hay tarjetas de ese tipo en existencia")


ruta = "17_01_2023/tarjetas.json"
ruta2 = "17_01_2023/clientes.json"
while True:
  dicc_clientes = cargar_ruta(ruta2)
  dicc = cargar_ruta(ruta)
  input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
  menu()
  escoger(validacion("Opcion 1 a 4: "))
  print("\n")
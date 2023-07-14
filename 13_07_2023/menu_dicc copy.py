import json

def menu():
    print("\n")
    print("*** NOMINA ACME ***")
    print("MENU")
    print("1- Agregar empleado")
    print("2- Modificar empleado")
    print("3- Buscar empleado")
    print("4- Eliminar empleado")
    print("5- Listar empleados")
    print("6- Listar nómina de un empleado")
    print("7- Listar nómina de todos los empleados")
    print("8- Salir")
    print("\n")

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

def escoger(opcion):
    if opcion == 1:
        print("AGREGAR".center(50,"-"))
        agregar(dicc, ruta)
    elif opcion == 2:
        print("MODIFICAR".center(50,"-"))
        modificar(dicc)
    elif opcion == 3:
        print("BUSCAR EMPLEADO".center(50,"-"))
        buscar(dicc)
    elif opcion == 4:
        print("ELIMINAR".center(50,"-"))
        eliminar(dicc)
    elif opcion == 5:
        print("LISTAR EMPLEADO".center(50,"-"))
        listar(dicc)
    elif opcion == 6:
        print("LISTAR NOMINA".center(50,"-"))
        listar_nomina(dicc)
    elif opcion == 7:
        print("LISTAR NOMINA DE TODOS LOS EMPLEADOS".center(50,"-"))
        listar_nomina_todos(dicc)
    elif opcion == 8:
        print("¡Hasta luego!".center(50,"-"))
        salir = validacion_t("Presione cualquier tecla para volver al menú o ingrese 'S' para salir: ")
        if salir.lower() == "s":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")
        input("Presione cualquier tecla para continuar")

def agregar(dicc, ruta):    
    id_empleado = validacion("\nIngrese la id del empleado: ")

    for empleados in dicc.keys():
        if str(id_empleado) == empleados:
            return print("Ya existe un empleado con ese ID")
    
    nombre = validacion_t("Ingrese el nombre del empleado: ")

    while True:
        horas = validacion("Ingrese las horas trabajadas: ")
        if horas > 160 or horas < 1:
            print("-" * 50)
            print("La cantidad de horas trabajadas debe ser de 1 a 160")
            print("-" * 50)
        else:
            break

    while True:
        valor = validacion("Ingrese el valor por hora: ")
        if valor > 150_000 or valor < 8_000:
            print("-" * 50)
            print("El valor por hora debe ser entre 8000 y 150000")
            print("-" * 50)
        else:
            break
    
    dicc[id_empleado] = {}
    dicc[id_empleado]["nombre"] = nombre
    dicc[id_empleado]["horas"] = horas
    dicc[id_empleado]["valor"] = valor

    escribir_en_disco(ruta, dicc)

    print("-" * 50)
    print("El empleado fue ingresado con exito")
    print("-" * 50)

def modificar(dicc):
    if dicc:
        id_empleado = validacion("\nIngrese el ID del empleado a modificar: ")
        encontrado = False
        for empleado in dicc.keys():
            if empleado == id_empleado:
                encontrado = True
                
                nombre = validacion_t("Ingrese el nuevo nombre del empleado: ")
                horas = validacion("Ingrese las nuevas horas trabajadas: ")
                valor = validacion("Ingrese el nuevo valor de la hora: ")

                dicc[id_empleado]["nombre"] = nombre
                dicc[id_empleado]["horas"] = horas
                dicc[id_empleado]["valor"] = valor

                escribir_en_disco(ruta, dicc)

                print("-" * 50)
                print("Empleado modificado con éxito.")
                print("-" * 50)
                input("Presione cualquier tecla para continuar")
                break
        if not encontrado:
            print("-" * 50)
            print("El empleado NO ha sido ingresado.")
            print("-" * 50)
            input("Presione cualquier tecla para continuar")

def buscar(dicc):    
    if dicc:
        id_empleado = validacion("\nIngrese el ID del empleado a buscar: ")
        encontrado = False
        for empleado in dicc.keys():
            if empleado == id_empleado:
                encontrado = True
                nombree = dicc[empleado]["nombre"] 
                horas = dicc[empleado]["horas"]  
                valor = dicc[empleado]["valor"] 
                print("Información del empleado:")
                print(f"ID:  {empleado}")
                print(f"Nombre: {nombree}")
                print(f"Horas trabajadas: {horas}")
                print(f"Valor de la hora: {valor}")
                activador = 1
                return activador 
        if not encontrado:
            print("No se encontró ningún empleado con el ID ingresado.")
    else:
        print("No se han ingresado empleados.")

def eliminar(dicc):
    if dicc:
        id_empleado = validacion("\nIngrese el ID del empleado a eliminar: ")
        encontrado = False
        for empleado in dicc.keys():
            if empleado == id_empleado:
                encontrado = True
                dicc.pop(empleado)
                escribir_en_disco(ruta, dicc)
                print("Empleado eliminado con éxito.")
                break
        if not encontrado:
            print("No se encontró ningún empleado con el ID ingresado.")
    else:
        print("No se han ingresado empleados.")

def listar(dicc):
    if dicc:
        lista = []
        for l in dicc.keys():
            lista.append(l)
        total_empleados = len(dicc)
        pagina = 1
        contador = 0
        continuar = True
        
        while continuar:
            print(f"\n--- Página {pagina} ---")
            for i in range(contador, contador + 5):
                if i < total_empleados:
                    empleado = lista[i]
                    nombre = dicc[empleado]["nombre"] 
                    horas = dicc[empleado]["horas"]  
                    valor = dicc[empleado]["valor"] 
                    print(f"ID: {empleado}")
                    print(f"Nombre: {nombre}")
                    print(f"Horas trabajadas: {horas}")
                    print(f"Valor de la hora: {valor}")
                    print("-" * 50)
                    
                else:
                    break

            contador += 5
            opcion = input("Presione 'Enter' para ver más empleados o ingrese 'M' para volver al menú: ")
            if opcion.lower() == "m":
                break

            if contador >= total_empleados:
                opcion = input("No hay mas empleadospara mostrar. ")
                break


            pagina += 1
    else:
        print("No se han ingresado empleados.")

def listar_nomina(dicc):
    if dicc:
        id_empleado = validacion("\nIngrese el ID del empleado a buscar: ")
        encontrado = False
        for empleado in dicc.keys():
            if empleado == id_empleado:
                encontrado = True
                nombree = dicc[empleado]["nombre"] 
                horas = dicc[empleado]["horas"]  
                valor = dicc[empleado]["valor"] 
                print("Información del empleado:")
                print(f"ID:  {empleado}")
                print(f"Nombre: {nombree}")
                print(f"Horas trabajadas: {horas}")
                print(f"Valor de la hora: {valor}")
                salario_bruto = dicc[id_empleado]["horas"] * dicc[id_empleado]["valor"] 
                salario_minimo = 1028545  # Salario mínimo legal vigente en Colombia en 2023

                if salario_bruto < salario_minimo:
                        transporte = 106454
                else:
                    transporte = 0
                eps = salario_bruto * 0.04
                pension = salario_bruto * 0.04
                salario_neto = salario_bruto + transporte - eps - pension

                print("-" * 50)
                print(f"Salario Bruto: {salario_bruto}")
                print(f"Subsidio de transporte: {transporte}")
                print(f"Descuento EPS (4%): {eps:.0f}")
                print(f"Descuento Pensión (4%): {pension:.0f}")
                print(f"Salario Neto: {salario_neto:.0f}")
                
                return True 
        if not encontrado:
            print("No se encontró ningún empleado con el ID ingresado.")
    else:
        print("No se han ingresado empleados.")

def listar_nomina_todos(dicc):
    if dicc:
        lista = []
        for l in dicc.keys():
            lista.append(l)
        total_empleados = len(dicc)
        pagina = 1
        contador = 0
        continuar = True
        
        while continuar:
            print(f"\n--- Página {pagina} ---")
            for i in range(contador, contador + 5):
                if i < total_empleados:
                    id_empleado = lista[i]
                    print("-" * 50)
                    print("-" * 50)
                    nombre = dicc[id_empleado]["nombre"] 
                    horas = dicc[id_empleado]["horas"]  
                    valor = dicc[id_empleado]["valor"] 
                    print(f"ID: {id_empleado}")
                    print(f"Nombre: {nombre}")
                    print(f"Horas trabajadas: {horas}")
                    print(f"Valor de la hora: {valor}")
                    print("-" * 50)
                    salario_bruto = horas* valor
                    salario_minimo = 1028545  # Salario mínimo legal vigente en Colombia en 2023

                    if salario_bruto < salario_minimo:
                            transporte = 106454
                    else:
                        transporte = 0
                    eps = salario_bruto * 0.04
                    pension = salario_bruto * 0.04
                    salario_neto = salario_bruto + transporte - eps - pension

                    print(f"Salario Bruto: {salario_bruto}")
                    print(f"Subsidio de transporte: {transporte}")
                    print(f"Descuento EPS (4%): {eps:.0f}")
                    print(f"Descuento Pensión (4%): {pension:.0f}")
                    print(f"Salario Neto: {salario_neto:.0f}")
                else:
                    break

            contador += 5

            opcion = input("\nPresione 'Enter' para ver más empleados o ingrese 'M' para volver al menú: ")
            if opcion.lower() == "m":
                break

            if contador >= total_empleados:
                opcion = input("No hay mas empleadospara mostrar. ")
                break

            pagina += 1

def cargar_ruta(ruta):    
    dicc = {}
    try:
        with open(ruta, "r") as archivo:
            leer_dicc = json.load(archivo)
            for llaves in leer_dicc.keys():
                id_empleado = int(llaves)
                dicc[id_empleado] = {}
                dicc[id_empleado] = leer_dicc[llaves]
        return dicc
    except:
        with open(ruta, "w") as archivo:
            return dicc

    return dicc

def escribir_en_disco(ruta, dicc):
    with open(ruta, "w") as archivo:
        json.dump(dicc, archivo)
        print("Se ha escrito en disco")

    if not archivo.closed:
        print("Cerrando archivo")
        archivo.close()


#Inicio
ruta = "13_07_2023/emlacme.json"

while True:
  dicc = cargar_ruta(ruta)
  print(dicc)
  activador = 0
  id_empleado = 0
  input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
  menu()
  escoger(validacion("Opcion 1 a 8: "))
  print("\n")
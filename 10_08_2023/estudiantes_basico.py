def menu():
    print("\n")
    print(" MENU PRINCIPAL ".center(100," "))
    print(" "*6 + "1- Agregar un nuevo registro")
    print(" "*6 + "2- Buscar un estudiante")
    print(" "*6 + "3- Actualizar datos del estudiante")
    print(" "*6 + "4- Borrar estudiante")
    print(" "*6 + "5- Calcular notas definitivas")
    print(" "*6 + "6- Listar estudiantes con notas definitivas y ver promedio general")
    print(" "*6 + "7- Salir")
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
        print("BUSCAR".center(50,"-"))
        buscar(dicc)
    elif opcion == 3:
        print("ACTUALIZAR".center(50,"-"))
        modificar(dicc)
    elif opcion == 4:
        print("ELIMINAR".center(50,"-"))
        eliminar(dicc)
    elif opcion == 5:
        print("NOTAS DEFINITIVAS".center(50,"-"))
        listar(dicc)
    elif opcion == 6:
        print("LISTAR NOTAS".center(50,"-"))
        listar_nomina(dicc)
    elif opcion == 7:
        print("¡Hasta luego!".center(50,"-"))
        salir = validacion_t("Presione cualquier tecla para volver al menú o ingrese 'S' para salir: ")
        if salir.lower() == "s":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")
        input("Presione cualquier tecla para continuar")

def agregar(dicc, ruta):    
    id_empleado = validacion("\nIngrese el codigo del estudiante: ")
    for empleados in dicc.keys():
        if str(id_empleado) == empleados:
            return print("Ya existe un estudiante con ese codigo")
    
    nombre = validacion_t("Ingrese el nombre del estudiante: ")
    dicc[id_empleado] = {}
    dicc[id_empleado]["nombre"] = nombre
    dicc[id_empleado]["notas"] = {}
    for i in range(1, 4):
        while True:
            horas = validacion(f"Ingrese la {i}.Nota del estudiante: ")
            if horas > 5 or horas < 0:
                print("-" * 50)
                print("La nota debe estar entre 1 a 5")
                print("-" * 50)
            else:
                break
        dicc[id_empleado]["notas"][i] = horas

    escribir_en_disco(ruta, dicc)

    print("-" * 50)
    print("Se realizó el proceso con exito")
    print("-" * 50)


def buscar(dicc):    
    if dicc:
        id_empleado = validacion("\nIngrese el codigo del estudiante a buscar: ")
        encontrado = False
        for empleado in dicc.keys():
            if int(empleado) == id_empleado:
                encontrado = True
                nombree = dicc[empleado]["nombre"] 
                nota1 = dicc[empleado]["notas"][1] 
                nota2 = dicc[empleado]["notas"][2]
                nota3 = dicc[empleado]["notas"][3]

                print("Información del estudiante:")
                print(f"Codigo:  {empleado}")
                print(f"Nombre: {nombree}")
                print(f"Nota 1: {nota1}")
                print(f"Nota 2: {nota2}")
                print(f"Nota 3: {nota3}")
                activador = 1
                return activador 
        if not encontrado:
            print("No se encontró ningún estudiante con el codigo ingresado.")
    else:
        print("No se han ingresado estudiantes.")

def modificar(dicc):
    if dicc:
        id_empleado = validacion("\nIngrese el ID del empleado a modificar: ")
        encontrado = False
        for empleado in dicc.keys():
            if empleado == id_empleado:
                encontrado = True
                nota1 = dicc[id_empleado]["notas"][1]
                nota2 = dicc[id_empleado]["notas"][2]
                nota3 = dicc[id_empleado]["notas"][3]
                print("Encontrado. Qué desea modificar?")
                print(f"1:Nombre - 2:Nota {nota1} - 3:Nota {nota2}  - 4:Nota {nota3}  - 5:Todo - 6:Salir")

                seguir = True
                while seguir == True:
                    opc = int(input("Opcion: "))
                    if opc == 1:
                        nombre = str(input("Ingrese el nuevo nombre: "))
                        dicc[id_empleado]["nombre"] = nombre 
                    elif opc == 2:
                        nota = str(input("Ingrese la nueva nota: "))
                        dicc[id_empleado]["notas"][1] = nota 
                    elif opc == 3:
                        nota = str(input("Ingrese la nueva nota: "))
                        dicc[id_empleado]["notas"][2] = nota 
                    elif opc == 4:
                        nota = str(input("Ingrese la nueva nota: "))
                        dicc[id_empleado]["notas"][3] = nota 
                    elif opc == 5:
                        dicc.pop(id_empleado)
                        agregar(dicc, ruta)
                    elif opc == 6:
                        return input("Presione cualquier tecla para salir: ")
                    else:
                        print("Opcion invalida, solo de 1 a 6")
                        input("Presione cualquier tecla para continuar: ")
                        continue
                    seguir = False
                

                escribir_en_disco(ruta, dicc)

                print("-" * 50)
                print("Estudiante modificado con éxito.")
                print("-" * 50)
                
                break
        if not encontrado:
            print("-" * 50)
            print("El estudiante NO ha sido ingresado.")
            print("-" * 50)
            input("Presione cualquier tecla para continuar")

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
    with open(ruta, "a+") as archivo:
        contador = 0
        dicc ={}
        archivo.seek(0)
        for lineas in archivo:
            contador +=1
            if contador > 1:
                lin = lineas.rstrip()
                lista_disco = lin.split(";")
                lista_disco[0] = int(lista_disco[0])
                dicc[lista_disco[0]] = {}
                dicc[lista_disco[0]]["nombre"] = lista_disco[1]
                dicc[lista_disco[0]]["horas"] = int(lista_disco[2])
                dicc[lista_disco[0]]["valor"] = int(lista_disco[3])

    if contador < 2:
        dicc = {}

    return dicc

def escribir_en_disco(ruta, dicc):
    with open(ruta, "w") as archivo:
        archivo.write("ID;NOMBRE;HORASTRAB;VALHORA")

        for id in dicc.keys():
            nombre = dicc[id]["nombre"]
            horas = dicc[id]["horas"]
            valor = dicc[id]["valor"]

            lista_emple = [str(id), nombre, str(horas), str(valor)]
            texto_empleados = "\n" + ";".join(lista_emple)
            archivo.write(texto_empleados)

#Inicio
ruta = "C:/Users/Usuario/Desktop/pythonWork/Codigos/emplacme.dat"

while True:
  dicc = cargar_ruta(ruta)
  activador = 0
  id_empleado = 0
  input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
  menu()
  escoger(validacion("Opcion 1 a 8: "))
  print("\n")
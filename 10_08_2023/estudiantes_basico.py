import json 
import os 

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
        cal_def(dicc)
    elif opcion == 6:
        print("LISTAR NOTAS".center(50,"-"))
        listar_notas(dicc)
    elif opcion == 7:
        print("¡Hasta luego!".center(50,"-"))
        salir = validacion_t("Presione cualquier tecla para volver al menú o ingrese 'S' para salir: ")
        if salir.lower() == "s":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")

def agregar(dicc, ruta):    
    id_empleado = validacion("\nIngrese el codigo del estudiante: ")
    for empleados in dicc.keys():
        if str(id_empleado) == empleados:
            return print("Ya existe un estudiante con ese codigo")
    
    nombre = validacion_t("Ingrese el nombre del estudiante: ")
    dicc[id_empleado] = {}
    dicc[id_empleado]["nombre"] = nombre
    dicc[id_empleado]["notas"] = {}
    total = 0
    for i in range(1, 4):
        while True:
            horas = validacion_f(f"Ingrese la {i}.Nota del estudiante: ")
            if horas > 5 or horas < 0:
                print("-" * 50)
                print("La nota debe estar entre 0 a 5")
                print("-" * 50)
            else:
                break
        dicc[id_empleado]["notas"][i] = horas
        total += horas
    dicc[id_empleado]["definitiva"] = total

    escribir_en_disco(ruta, dicc)

    print("-" * 50)
    print("Se realizó el proceso con exito")
    print("-" * 50)

def buscar(dicc):   
    encontrado = False 
    if dicc:
        id_empleado = validacion("\nIngrese el codigo del estudiante a buscar: ")
        print()
        for empleado in dicc.keys():
            if int(empleado) == id_empleado:
                encontrado = True
                nombree = dicc[empleado]["nombre"] 
                nota1 = dicc[empleado]["notas"]["1"] 
                nota2 = dicc[empleado]["notas"]["2"]
                nota3 = dicc[empleado]["notas"]["3"]

                print("|"+"CODIGO".center(15, " ")+"|"+"NOMBRE".center(15, " ")+"|"+"NOTA 1".center(15, " "),end="|")
                print("NOTA 2".center(15, " ")+ "|"+"NOTA 3".center(15, " "))
                print("|"+empleado.center(15, " ")+"|"+nombree.center(15, " ")+"|"+str(nota1).center(15, " "),end="|")
                print(str(nota2).center(15, " ")+ "|"+str(nota3).center(15, " ")+"|")
                return id_empleado
        if not encontrado:
            print("No se encontró ningún estudiante con el codigo ingresado.")
            return encontrado
    else:
        print("No se han ingresado estudiantes.")
        return encontrado

def modificar(dicc):
    if dicc:
        id_empleado = validacion("\nIngrese el codigo del estudiante a modificar: ")
        encontrado = False
        for empleado in dicc.keys():
            if int(empleado) == id_empleado:
                encontrado = True
                nota1 = dicc[empleado]["notas"]["1"]
                nota2 = dicc[empleado]["notas"]["2"]
                nota3 = dicc[empleado]["notas"]["3"]
                print("Encontrado. Qué desea modificar?")
                print(f"1:Nombre - 2:Nota {nota1} - 3:Nota {nota2}  - 4:Nota {nota3}  - 5:Todo - 6:Salir")
                seguir = True
                while seguir == True:
                    opc = int(input("Opcion: "))
                    if opc == 1:
                        nombre = str(input("Ingrese el nuevo nombre: "))
                        dicc[empleado]["nombre"] = nombre 
                    elif opc == 2:
                        nota = str(input("Ingrese la nueva nota: "))
                        dicc[empleado]["notas"]["1"] = nota 
                    elif opc == 3:
                        nota = str(input("Ingrese la nueva nota: "))
                        dicc[empleado]["notas"]["2"] = nota 
                    elif opc == 4:
                        nota = str(input("Ingrese la nueva nota: "))
                        dicc[empleado]["notas"]["3"] = nota 
                    elif opc == 5:
                        dicc.pop(empleado)
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
        id_empleado = validacion("\nIngrese el codigo del estudiante a eliminar: ")
        encontrado = False
        for empleado in dicc.keys():
            if int(empleado) == id_empleado:
                encontrado = True
                dicc.pop(empleado)
                escribir_en_disco(ruta, dicc)
                print("Estudiante eliminado con éxito.")
                break
        if not encontrado:
            print("No se encontró ningún estudiante con el codigo ingresado.")
    else:
        print("No se han ingresado estudiantes.")

def cal_def(dicc):
    empleado = buscar(dicc)
    if empleado == False: 
        return 
    else:
        empleado = str(empleado)
        total = dicc[empleado]["definitiva"]
        return print(f"La nota definitiva del estudiante es: {total}")

def listar_notas(dicc):
    print("|"+"CODIGO".center(15, " ")+"|"+"NOMBRE".center(15, " ")+"|"+"NOTA 1".center(15, " "),end="|")
    print("NOTA 2".center(15, " ")+"|"+"NOTA 3".center(15, " ")+"|"+"NOTA DEFINITIVA".center(15, " ")+"|")
    
    for codigos in dicc.keys():
        nombree = dicc[codigos]["nombre"] 
        nota1 = dicc[codigos]["notas"]["1"] 
        nota2 = dicc[codigos]["notas"]["2"]
        nota3 = dicc[codigos]["notas"]["3"]
        total = dicc[codigos]["definitiva"]
        print("|"+codigos.center(15, " ")+"|"+nombree.center(15, " ")+"|"+str(nota1).center(15, " "),end="|")
        print(str(nota2).center(15, " ")+"|"+str(nota3).center(15, " ")+"|"+str(total).center(15, " ")+"|")
    
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

#Inicio
ruta = "./diccionario.json"

os.system('clear')
while True:
  dicc = cargar_ruta(ruta)
  input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
  menu()
  escoger(validacion("Opcion 1 a 8: "))
  print("\n")
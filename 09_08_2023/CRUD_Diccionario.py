#[{"id": id, "nombre": nombre, "edad": edad, "doc": documento, "EPS": eps}, {}, {}. {}]
import os

def validarInput(mensaje):
    data = input(mensaje)
    while(data.strip() == ''):
        print("\nIngrese algún dato\n")
        data = input(mensaje)
    return data

def validaDocumento(id, empleados):
    for i in range(len (empleados)):
        if (empleados[i]['documento'] == id):
            return True
    return False
   
def tabla_inicio():
        print("|",end = " " )
        print("Documento".center(15, " "), end = " ")
        print("|",end = " " )
        print("Nombre".center(15, " "), end = " ")
        print("|",end = " " )
        print("Edad".center(15, " "), end = " ")
        print("|",end = " " )
        print("EPS".center(15, " "), end = " ")
        print("|")

def tabla_datos(doc, nombre, edad, eps):
                print("|",end = " " )
                print(f"{doc}".center(15, " "), end= " ")
                print("|",end = " " )
                print(f"{nombre}".center(15, " "), end= " ")
                print("|",end = " " )
                print(f"{edad}".center(15, " "), end= " ")
                print("|",end = " " )
                print(f"{eps}".center(15, " "), end = " ")
                print("|")

def ingresarDatos():
    os.system('clear')

    documento = validarInput("Digite el Documento: ")
    while(validaDocumento(documento,empleados)):
        print("\nEl documento ya existe\n")
        documento = validarInput("Digite el Documento: ")
        
    nombre = validarInput("Digite el Nombre: ")
    edad = validarInput("Digite el Edad: ")
    eps = validarInput("Digite el EPS: ")
   
    empleados.append({
        "documento": documento,
        "nombre": nombre,
        "edad": edad,
        "eps": eps
    })  
    input("\nIngresado. Presione cualquier tecla para continuar al programa: ")

def eliminarRegistro():
    os.system('clear')
    
    doc = input('Ingrese el documento que desea eliminar: ')

    for i in range(len(empleados)):
        if(empleados[i]['documento'] == doc):
            empl = empleados.pop(i)
            return print('\nSe ha eliminado el registro', empl, '\n')

    return print('\nNo existe el registro con ese documento\n')
   
def reportarListado():
    os.system('clear')
    tabla_inicio() 
    for empl in empleados:
        doc = empl["documento"]
        nombre = empl["nombre"]
        edad = empl["edad"]
        eps = empl["eps"] 
        tabla_datos(doc, nombre, edad, eps)
    input("\nPresione cualquier tecla para continuar al programa: ")

def BuscarRegistro():
    os.system('clear')
    
    doc = input('Ingrese el documento que desea buscar: ')

    for i in range(len(empleados)):
        if(empleados[i]['documento'] == doc):
            tabla_inicio()
            doc = empleados[i]["documento"]
            nombre = empleados[i]["nombre"]
            edad = empleados[i]["edad"]
            eps = empleados[i]["eps"] 
            tabla_datos(doc, nombre, edad, eps)
            
        input("\nPresione cualquier tecla para continuar al programa: ")

    return print('\nNo existe el registro con ese documento\n')

def ModificarRegistro():
    os.system('clear')
    
    doc = input('Ingrese el documento que desea modificar: ')

    for i in range(len(empleados)):
        if(empleados[i]['documento'] == doc):
            print("Encontrado. Qué desea modificar?")
            print("1:Nombre - 2:Edad - 3:Documento - 4:Eps - 5:Todo - 6:Salir")

            while True:
                opc = int(input("Opcion: "))
                if opc == 1:
                    nombre = str(input("Ingrese el nuevo nombre: "))
                    empleados[i]["nombre"] = nombre 
                elif opc == 2:
                    edad = str(input("Ingrese la nueva edad: "))
                    empleados[i]["edad"] = edad 
                elif opc == 3:
                    doc = str(input("Ingrese el nuevo documento: "))
                    empleados[i]["documento"] = doc
                elif opc == 4:
                    eps = str(input("Ingrese la nueva Eps: "))
                    empleados[i]["edad"] = eps
                elif opc == 5:
                    empleados.pop(i)
                    ingresarDatos()
                elif opc == 6:
                    return input("Presione cualquier tecla para salir: ")
                else:
                    print("Opcion invalida, solo de 1 a 6")
                    continue
                input("Modificado. Presione cualquier tecla para continuar: ")
                break
            
def menu():    
    seguir = True
    while seguir:
        os.system('clear')
        print("\n")
        print(" Selecciona la opción que desee ".center(100, "-"))
        print(" "*6 + "1) Ingresar un nuevo registro")
        print(" "*6 + "2) Eliminar un registro")
        print(" "*6 + "3) Mostrar listado total")
        print(" "*6 + "4) Buscar y mostrar un registro")  #****
        print(" "*6 + "5) Actualizar un registro")  #****
        print(" "*6 + "6) Salir del Programa\n")  #****
        print()
        opcion = int(input('Opcion: '))
        
        if(opcion == 6):
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 0 y 6\n')

        switch = { 1: ingresarDatos, 2: eliminarRegistro, 3: reportarListado, 4:BuscarRegistro, 5:ModificarRegistro}
        switch[opcion]()

os.system('clear')
empleados = []
menu()
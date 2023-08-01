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

def menu():
    print("\n")
    print(" INSTITUTO EDUCATIVO ACME ".center(100,"="))
    print(" MENU ".center(100,"="))
    print("1 - ESTUDIANTES")
    print("2 - NOTAS")
    print("3 - PROMEDIOS")
    print("4 - SALIR")
    print("\n")

def escoger(opcion):
    print("\n")
    if opcion == 1:
        ciclo = True
        while ciclo != 4:
            input("\nPresione cualquier tecla para continuar al menú ESTUDIANTES: ")
            dicc = cargar_ruta(ruta)
            print("ESTUDIANTES".center(100,"="))
            menu_estudiantes()
            ciclo = escoger_estudiantes(validacion("Opcion 1 a 4: "), dicc)
    elif opcion == 2:
        print("NOTAS".center(100,"="))
        ingresar_notas()
    elif opcion == 3:
        print("PROMEDIOS".center(100,"="))
        ciclo = True
        while ciclo != 4:
            input("\nPresione cualquier tecla para continuar al menú ESTUDIANTES: ")
            dicc = cargar_ruta(ruta)
            print("ESTUDIANTES".center(100,"="))
            menu_promedios()
            ciclo = escoger_promedios(validacion("Opcion 1 a 4: "), dicc)

    elif opcion == 4:
        print("¡Hasta luego!".center(100,"="))
        salir = validacion_t("Presione cualquier tecla para salir o ingrese 'M' para regresar: ")
        if not salir.lower() == "m":
            exit()
    else:
        print("Opción inválida. Intente nuevamente.")

#-------------------------------------------------------------------------

def comprobar_dicc(dicc, grado):
    try:
        if not dicc[grado]:
            dicc[grado] = {}
    except:
        dicc[grado] = {}

    return dicc

#------------------------------------------

def comprobar_dicc1(dicc, grado, id):
    try:
        for grados in dicc.keys():
            for ids in dicc[grados].keys():
                if int(ids) == id:
                    return False
        dicc[grado][id] = {}
    except:
        dicc[grado][id] = {}

    return dicc

def opcional(curso, msg):
    while True:
        grado = validacion(msg)
        if 0 < grado < 4:
            grado = curso[grado]
            return grado
        else:
            print("*****Opcion invalida*****")

def ingresar_estudiante(dicc):
    curso = {1: "noveno", 2: "decimo", 3: "undecimo"}
    grado = opcional(curso, "Curso: 1:Noveno, 2:Decimo, 3:Undecimo -> ")
    comprobar_dicc(dicc, grado)
    id = validacion("Ingrese el id del estudiante: ")
    seguir = True
    seguir = comprobar_dicc1(dicc, grado, id)
    if not seguir:
        return print("*****Ya se ha ingresado este ID*****")
    nombre = validacion_t("Ingrese el nombre del estudiante: ")
    genero = {1: "masculino", 2: "femenino", 3: "otro"}
    sexo = opcional(genero, "Genero 1:Masculino, 2:Femenino, 3:Otro -> ")
    dicc[grado][id]["nombre"] = nombre
    dicc[grado][id]["sexo"] = sexo
    escribir_en_disco(ruta, dicc)

def buscar_estudiante(dicc):
    encontrado = False
    if dicc:
        id_estudiante = validacion("\nIngrese el ID del estudiante a buscar: ")
        try:
            for grados in dicc.keys():
                for estudiantes in dicc[grados].keys():
                    if int(estudiantes) == id_estudiante:
                        encontrado = True
                        nombre = dicc[grados][estudiantes]["nombre"]
                        sexo = dicc[grados][estudiantes]["sexo"]
                        print(f"ID:{id_estudiante} - Nombre:{nombre} - Sexo:{sexo}")
                        return (encontrado, id_estudiante, grados)
            if not encontrado:
                print("No se encontró ningún estudiante con el ID ingresado.")
        except:
            print("No se han ingresado estudiantes.")
    else: 
        print("No se han ingresado grados.")

def modificar_estudiante(dicc):
    encontrado = False
    try:
        (encontrado, id_estudiante, grados)  = buscar_estudiante(dicc)
        if encontrado:
            dicc[str(grados)][str(id_estudiante)]["nombre"] = validacion_t("Nuevo nombre: ")
            genero = {1: "masculino", 2: "femenino", 3: "otro"}
            dicc[str(grados)][str(id_estudiante)]["sexo"] = opcional(genero, "Genero 1:Masculino, 2:Femenino, 3:Otro -> ")
    except:
        print("Volviendo al menú estudiantes...")
    escribir_en_disco(ruta, dicc)

def menu_estudiantes():
    print(" MENU ".center(100,"="))
    print("1 - Ingresar estudiante")
    print("2 - Modificar estudiante")
    print("3 - Buscar estudiante")
    print("4 - Regresar al menú")
    print("\n")

def menu_promedios():
    print(" MENU ".center(100,"="))
    print("1 - Promedios por grado")
    print("2 - Terna por grado")
    print("3 - Terna instituto")
    print("4 - Regresar al menú")
    print("\n")

def escoger_estudiantes(opcion, dicc):
    print("\n")
    if opcion == 1:
        print(" Ingresar estudiante ".center(50,"="))
        ingresar_estudiante(dicc)
    elif opcion == 2:
        print(" Modificar estudiante ".center(50,"="))
        modificar_estudiante(dicc)
    elif opcion == 3:
        print(" Buscar estudiante ".center(50,"="))
        buscar_estudiante(dicc)
    elif opcion == 4:
        print(" Regresando al menú ".center(50,"="))
        salir = validacion_t("Presione cualquier tecla para ir a menú principal o ingrese 'R' para regresar: ")
        if not salir.lower() == "r":
            return opcion
    else:
        print("Opción inválida. Intente nuevamente.")

def escoger_promedios(opcion, dicc):
    print("\n")
    if opcion == 1:
        print(" Promedios por grado ".center(50,"="))
        prom_grado(dicc)
    elif opcion == 2:
        print(" Terna por grados ".center(50,"="))
        terna_grado(dicc)
    elif opcion == 3:
        print(" Terna por instituto ".center(50,"="))
        
    elif opcion == 4:
        print(" Regresando al menú ".center(50,"="))
        salir = validacion_t("Presione cualquier tecla para ir a menú principal o ingrese 'R' para regresar: ")
        if not salir.lower() == "r":
            return opcion
    else:
        print("Opción inválida. Intente nuevamente.")

def prom_grado(dicc):
        for nivel1, nivel2 in dicc.items():
            if nivel1 != "promedio":
                for subllave, subvalor in nivel2.items():
                    if subllave != "promedio":
                        print(f"Llave: {nivel1} - ID: {subllave}")
                        print(f"Nombre: {subvalor['nombre']}")
                        print(f"Nota Promedio: {subvalor['nota_promedio']}")
                        print("-----------------")

def terna_grado(dicc):
    for nivel1, nivel2 in dicc.items():
        if nivel1 != "promedio":
            subdicc = dicc[nivel1]
            sorted_subdicc = sorted(subdicc.items(), key=lambda x: x[1]["nota_promedio"], reverse=True)
            for key, value in sorted_subdicc[:2]:
                print(f"Llave: {nivel1}")
                print(f"Subllave: {key}")
                print(f"Nombre: {value['nombre']}")
                print(f"Nota Promedio: {value['nota_promedio']}")
                print("-----------------")

def terna_inst(dicc):
        # Recopilar todas las notas promedio de todo el diccionario
    notas_promedio = []
    for nivel1, nivel2 in dicc.items():
        if isinstance(nivel2, dict) and "nombre" in nivel2 and "nota_promedio" in nivel2:
            if nivel1 != "promedio":
                notas_promedio.append(nivel2["nota_promedio"])

    # Ordenar las notas promedio en orden descendente
    notas_promedio.sort(reverse=True)

    # Imprimir las 5 mejores notas promedio
    for nota in notas_promedio[:5]:
        for nivel1, nivel2 in dicc.items():
            if isinstance(nivel2, dict) and "nombre" in nivel2 and "nota_promedio" in nivel2:
                if nivel2["nota_promedio"] == nota:
                    print(f"Llave: {nivel1}")
                    print(f"Nombre: {nivel2['nombre']}")
                    print(f"Nota Promedio: {nota}")
                    print("-----------------")

def ingresar_notas():
    if dicc:
        curso = {1: "noveno", 2: "decimo", 3: "undecimo"}
        grado = opcional(curso, "Curso para ingresar notas: 1:Noveno, 2:Decimo, 3:Undecimo -> ")
        if dicc[grado]:
            try:
                dicc[grado] = dict(sorted(dicc[grado].items(), key=lambda x: x[1]["nombre"]))
            except:
                return print("Ya se le han ingresado notas a este curso".center(50, "="))
            promedio_grado = 0
            contador = 0
            for estudiantes in dicc[grado].keys():
                dicc[grado][estudiantes]["notas"] = {}
                nombre = dicc[grado][estudiantes]["nombre"]
                print(f" Estudiante: {nombre} ".center(50, "="))
                cantidad_notas = validacion("Ingrese la cantidad N de notas: ")
                nota_promedio = 0
                for i in range(1, cantidad_notas+1):
                    nota = validacion_f(f"Ingrese la nota{i}: ")
                    dicc[grado][estudiantes]["notas"][f"nota{i}"] = nota
                    nota_promedio += nota
                nota_promedio = nota_promedio/cantidad_notas
                dicc[grado][estudiantes]["nota_promedio"] = nota_promedio
                escribir_en_disco(ruta, dicc)
                contador += 1
                promedio_grado += nota_promedio
            promedio_grado = promedio_grado/contador
            dicc[grado]["promedio"] = promedio_grado
            escribir_en_disco(ruta, dicc)
        else:
            print(" Grado Vacio ".center(50, "*"))           
    else:
        print(" No tiene ningún grado ".center(50, "*"))

ruta = "16_07_2023/instituto_acme.json"
while True:
  dicc = cargar_ruta(ruta)
  print(dicc)
  input("\nPRESIONE CUALQUIER TECLA PARA CONTINUAR AL PROGRAMA MENU")
  menu()
  escoger(validacion("Opcion 1 a 4: "))
  print("\n")
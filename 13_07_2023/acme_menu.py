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

id_producto = validacion("Ingrese el codigo del producto: ")
valor = validacion("Ingrese el valor del producto: ")
cantidad = validacion("Ingrese la cantidad comprada: ")

while True: 
    iva_condicion= validacion_t("Ingrese el tipo de IVA(Exento, Bienes ó General): ")
    iva_condicion= iva_condicion.lower().strip()
    largo = len(iva_condicion.strip().split(" "))
    if largo != 1:
        print("Solo ingrese una de las 3 palabras ")
        continue
    if iva_condicion == "exento":
        iva = 0
        break
    elif iva_condicion == "bienes":
        iva = 5
        break
    elif iva_condicion == "general":
        iva = 19
        break
    else: 
        print("")








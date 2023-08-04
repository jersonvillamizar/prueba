#{id_vend:{"nombre": nombre, "tipo": tipo, "clientes: {ID_cliente: {nombre: nombre, venta: venta, tipoventa: tp}}"}}

dicc = {}

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

def identificacion(msg):
    while True:
        id_vendedor = validacion(msg)
        if len(str(id_vendedor)) == 10:
            return id_vendedor
        else:
            print("-" * 50)
            print("Debe contener 10 numeros el ID")
            print("-" * 50)

def tipo_vendedor(n1, n2):
    while True:
        tipo = validacion(f"Digite una opción de {n1} a {n2}: ")
        if (n1 - 1) < tipo < (n2 + 1): 
            return tipo
        else:
            print("-" * 50)
            print(f"Debe ser un numero de {n1} a {n2}")
            print("-" * 50)

def comprobar_dicc(dicc, id_cliente):
    try:
        if dicc[id_cliente]:
            return False
        else:
            dicc[id_cliente] = {}
    except:
        dicc[id_cliente] = {}

    return dicc

def comision(tipo, tipo_cl):
    if tipo == 1:
        if tipo_cl == 1:
            comision = 25
        else:
            comision = 20
    elif tipo == 2:
        if tipo_cl == 1:
            comision = 15
        else:
            comision = 10
    else:
        if tipo_cl == 1:
            comision = 20
        else:
            comision = 15
    return comision

def cliente_id(msg):
    while True:
            id_cl = identificacion(msg)
            try:
                if dicc[id_vendedor]["ventas"][id_cl]:
                    print("ID ya registrado".center(100, "*"))
                    continue
                else:
                    dicc[id_vendedor]["ventas"][id_cl] = {}
                    return id_cl
                    
            except:
                dicc[id_vendedor]["ventas"][id_cl] = {}
                return id_cl

print("-" * 100)
n_vendedores = validacion("\nIngrese la cantidad N de empleados: ")

for i in range(1, n_vendedores + 1):
    existente = True
    while True:
        print("-" * 100)
        id_vendedor = identificacion(f"\nIngrese el ID del {i}.vendedor(10 digitos): ")
        existente = comprobar_dicc(dicc, id_vendedor)
        if not existente:
            print("Ya se ha ingresado este ID de Vendedor".center(100, "*"))
            continue 
        break
    nombre = validacion_t("Ingrese el nombre del vendedor: ")
    print("Tipo de vendedor: 1.Puerta a puerta - 2.Telemercadeo - 3.Ejecutivo en ventas")
    tipo = tipo_vendedor(1, 3)

    n_ventas = validacion(f"Ingrese la cantidad M de ventas del vendedor {nombre}: ")
    dicc[id_vendedor]["nombre"] = nombre
    dicc[id_vendedor]["tipo"] = tipo
    dicc[id_vendedor]["ventas"] = {}
    
    for j in range(1, n_ventas + 1):
        id_cl = cliente_id(f"\nIngrese el ID del {j}.cliente(10 digitos): ")
        nombre_cl = validacion_t("Ingrese el nombre del cliente: ")
        print("Tipo de venta: 1.Contado - 2.Credito ")
        tipo_cl = tipo_vendedor(1, 2)
        valor = validacion("Ingrese el valor de la venta: ")
        dicc[id_vendedor]["ventas"][id_cl]["nombre_cl"] = nombre_cl
        dicc[id_vendedor]["ventas"][id_cl]["tipo_cl"] = tipo_cl
        dicc[id_vendedor]["ventas"][id_cl]["valor"] = valor
        comi = comision(tipo, tipo_cl)
        dicc[id_vendedor]["ventas"][id_cl]["comision"] = comi
            
print("\n")
print("Valor a pagar por concepto de comisiones".center(100, "="))
total = 0
for ids in dicc.keys():
    nombre = dicc[ids]["nombre"] 
    tipo = dicc[ids]["tipo"] 
    print(f"\nVendedor ID:{ids} - Nombre:{nombre} - Tipo Vendedor:{tipo}")
    contador = 0
    total_comi = 0
    total_ventas = 0
    for id_clientes in dicc[ids]["ventas"].keys():
        contador += 1
        tipo_cl = dicc[ids]["ventas"][id_clientes]["tipo_cl"] 
        valor = dicc[ids]["ventas"][id_clientes]["valor"] 
        comi = dicc[ids]["ventas"][id_clientes]["comision"] 
        valor_comi = (valor * comi) / 100
        total_comi += valor_comi
        total_ventas += valor
        print(f"{contador}.Venta - Tipo Venta:{tipo_cl} - Valor:{valor} - Comision:{comi}% = {valor_comi:.0f}")
    print(f"Total comisión: {total_comi}")
    print(f"Total ventas: {total_ventas}")
    total += total_comi    

print("-" * 100)
print(f"Valor total a pagar por comisiones(Todos los vendedores): {total}")
print("-" * 100)



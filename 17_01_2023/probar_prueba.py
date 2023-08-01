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

def telefono_val():
    while True:
            telefono = validacion("Ingrese el numero de telefono de cliente(10 digitos): ")
            if len(str(telefono).strip()) == 10:
                return telefono
            else: 
                print("No contiene 10 digitos")

dicc = {"Visa":{1098:{"mes": 11, "año": 2014}, 1097:{"mes": 11, "año": 2014}}}

dicc["Visa"].pop(1098)

print(dicc)


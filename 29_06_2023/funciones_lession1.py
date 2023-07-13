# SINTAXIS GENERAL
# def nombre_funcion([param1, param, .., param3])
#    cuerpo_funcion

#Funcion que sume dos numeros

def sumar(num1, num2) :
    s = num1 + num2 
    return s

# Funcion validar

def validar(msg) :
    while True :
        try :
            n = int(input(msg))
            return n
        except ValueError:
            print("Error! Ingrese un numero entero valido")

a = validar("Ingrese un numero: ")
b = validar("Ingrese otro numero: ")
print("El resultado es:", sumar(a, b))

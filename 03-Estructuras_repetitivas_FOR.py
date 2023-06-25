number1 = 0
number2 = 0
ecuation = 0

print("\n")

for i in range(1,10) :
    for n in range(1,10):
        ecuation = (i ** 3) + (n ** 4) - 2 * (i ** 2)
        if ecuation < 680 :
            print(f"El numero P = {i} y el numero Q = {n} cumplen la condicion")

print("\n")
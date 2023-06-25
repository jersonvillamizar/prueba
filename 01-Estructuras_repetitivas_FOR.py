number = 0

print("\n")

for i in range(1,1000) :
    number = number + 1
    residual3 = number % 3
    residual7 = number % 7

    if residual3 == 0 or residual7 == 0 :
        print(f"El numero {number} cumple con las condiciones")
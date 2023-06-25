print("\n")

mayor = -100000000000
menor = 100000000000

for i in range(1,4) :
    number = int(input(f"Ingrese el numero {i}: "))
   
    if number > mayor :
        mayor = number
        
    if number < menor :
        menor = number
    
print(f"\nMayor: {mayor}\nMenor: {menor}\n")
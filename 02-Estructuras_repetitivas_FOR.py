number = int(input("\nIngrese el numero: "))

ecuation = 0

for i in range(1,number+1):
    i = i * -1
    ecuation = ecuation - 1/i 
    

print(f"\nEl resultado es {ecuation}\n")
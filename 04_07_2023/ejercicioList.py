voc = ["a", "e", "i", "o", "u"]

n = int(input("\nIngrese las N letras: "))

lstNotas = []

for i in range (1,n+1):

    nota = str(input(f"\nIngrese la letra {i}: "))
    lstNotas.append(nota)

for j in voc:
    a = j
    ca = lstNotas.count(j)
    print(f"\n{j} : {ca}")

print("\n")


notMen = -1
notMay = 6
sumNotas = 0
promNotas = 0.0
lstNotas = []
for est in range (1,11):
    nota = float(input(f"\nIngrese nota estudiante {est}: "))
    lstNotas.append(nota)

notMen = min(lstNotas)
print(f"La notar menor es: {notMen}")
notMay = max(lstNotas)
print(f"La notar mayor es: {notMay}")


promNotas = sum(lstNotas) / len(lstNotas)
print(f"El promedio de las notas es: {promNotas}")

lstNotas.sort(reverse=True)
tresNotas = lstNotas[0:3]
print(f"las tres mejores notas son: {tresNotas}")

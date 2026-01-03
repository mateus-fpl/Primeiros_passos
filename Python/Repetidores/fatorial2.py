numero = int(input("Fatorial de: "))
fatorial = 1

print(f"{numero}! =", end=" ")

for i in range(numero, 0, -1):
    fatorial *= i
    separador = " = " if i == 1 else " . "
    print(i, end=separador)

print(fatorial)

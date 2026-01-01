numero = int(input("Digite um número: "))
fatorial = 1

for i in range(numero, 0, -1):
    fatorial *= i  
    print(i, end=" . " if i > 1 else " = ")

print(fatorial)
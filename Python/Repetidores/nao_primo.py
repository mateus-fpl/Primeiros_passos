num = int(input("Digite um número: "))
total_divisores = 0
divisores = 0

for i in range(1, num + 1):
    if num % i == 0:
        total_divisores += 1 
        print(i, end=" ")

print()

if total_divisores != 2:
    print("Não é primo")
else:
    print("É primo")
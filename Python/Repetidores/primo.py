num = int(input("Digite um número: "))
total_divisores = 0

for i in range(1, num + 1):
    if num % i == 0:
        total_divisores += 1 

if total_divisores == 2:
    print("É primo")
else:
    print("Não é primo")
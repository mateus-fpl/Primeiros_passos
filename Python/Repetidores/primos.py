n = int(input("Mostrar primos até: "))
total_divisoes_geral = 0
primos = []

for num in range(1, n + 1):
    divisores_deste_num = 0
    
    for i in range(1, num + 1):
        total_divisoes_geral += 1 
        if num % i == 0:
            divisores_deste_num += 1
            
    if divisores_deste_num == 2:
        primos.append(num)

print(f"Os números primos entre 1 e {n} são: {primos}")
print(f"Para encontrar esses números, o programa executou {total_divisoes_geral} divisões.")
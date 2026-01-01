numeros = []
alg = int(input("Quantos números você quer digitar? "))

for i in range(alg):
    num = int(input(f"Digite o {i+1}° número: "))
    numeros.append(num)

print()
maior = max(numeros)
menor = min(numeros)

soma = sum(numeros)

print(f"O maior número foi: {maior}")
print(f"O menor número foi: {menor}")
print(f"A soma dos números foi: {soma}")
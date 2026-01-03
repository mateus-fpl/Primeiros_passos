import math

vetor = []

for i in range(5):
    num = int(input(f"Digite o {i +1}° numero: "))
    vetor.append(num)

soma = sum(vetor)
mult = math.prod(vetor)

print()
print(f"Os números digitados foram: {vetor}")
print(f"A soma dos números é: {soma}")
print(f"A multiplicação é: {mult:.2f}")


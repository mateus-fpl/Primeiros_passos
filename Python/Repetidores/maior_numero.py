numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    numeros.append(num)

maior = max(numeros)
print(f"O maior número foi: {maior}")

soma = sum(numeros)
media = sum(numeros)/len(numeros)

print(f"A soma dos números é: {soma:.2f}")
print(f"A média é: {media:.2f}")
vetor = []

print("Digite 5 números para o vetor abaixo:")
for i in range(5):
    numero = int(input(f"Digite o {i+1}° número:"))
    vetor.append(numero)

quadrados = [numero **2 for numero in vetor]
print(f"Os números que você digitou: {vetor}")
print(f"Eles ao quadrado: {quadrados}")


vetor = []

for i in range(10):
    num = float(input(f"Digite o {i + 1}° número: "))
    vetor.append(num)

for n,num in enumerate(reversed(vetor)):
    print(f"Em ordem reversa o {n+1}° número é: {num}")
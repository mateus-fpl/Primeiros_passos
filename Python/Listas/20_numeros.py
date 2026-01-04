vetor_A = []
vetor_B = []
vetor_C = []

print("Digite os 10 primeiros números do vetor A:")
for i in range(10):
    numero1 = int(input(f"Digite o {i+1}° número: "))
    vetor_A.append(numero1)
print()
print("Digite os 10 primeiros números do vetor B:")
for i in range(10):
    i = 10 + i
    numero2 = int(input(f"Digite o {i+1}° número: "))
    vetor_B.append(numero2)

print()

for i in range(10):
    vetor_C.append(vetor_A[i])
    vetor_C.append(vetor_B[i])

print(f"Vetor Intercalado: {vetor_C}")
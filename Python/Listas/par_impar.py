par = []
impar = []

print("Digite 20 números inteiros:")
print()
for i in range(20):
    numero = int(input(f"Digite o {i+1}° número: "))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f"Os números totais foram: {numero}")
print(f"Os números pares foram: {par}")
print(f"Os números ímpares foram: {impar}")
par = []
impar = []

for i in range(1,10):
    i = i + 1
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print("Número pares:")
print(*par, " ")
print("Números ímpares:")
print(*impar, " ")
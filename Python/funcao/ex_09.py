def numero_inverso(N):
    inverso = str(N[::-1])
    return inverso

numero = input ("Digite um número: ")
numero_contrario = numero_inverso(numero)

print(f"O numero {numero} ao contrário fica {numero_contrario}")
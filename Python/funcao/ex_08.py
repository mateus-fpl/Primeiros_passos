def quantidade_digitos(N):
    digitos = len(str(N))
    return digitos

numero = input("Digite um número: ")
contagem = quantidade_digitos(numero)

print(f"O número {numero} possuí {contagem} dígitos")
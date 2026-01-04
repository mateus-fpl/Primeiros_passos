frase = input("Escreva uma frase: ")
frase_limpa = frase.lower().replace(" ", "")

if frase_limpa == frase_limpa[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo")
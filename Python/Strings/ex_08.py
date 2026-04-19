frase = input("Digite uma frase: ")
frase_invertida = frase[::-1]

if frase.lower().replace(" ","") == frase_invertida.lower().replace(" ",""):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
palavra = "arara"
palavra_invertida = palavra[::-1]
eh_palindromo = palavra == palavra_invertida
if eh_palindromo:
    print("A palavra", palavra, "é um palíndromo.")
else:
    print("A palavra", palavra, "não é um palíndromo.")
frase = input("Escreva uma frase: ")
espaco = 0
vogal = 0

for caractere in frase.lower():
    if caractere == " ":
        espaco += 1
    if caractere in "aeiouáéíóúãõâêîôû":
        vogal += 1


print(f"A quantidade de espaços em branco é: {espaco}")
print(f"A quantidade de vogais presentes é: {vogal}")
consoantes = []
vogais = "aeiou"

for i in range (10):
    letras = input(f"Digite o {i+1}° caractere: ").lower()
    if letras.isalpha() and letras not in vogais:
        consoantes.append(letras)

print(f"As consoantes encontradas foram: {consoantes}")
print(f"O total de consoantes foram: {len(consoantes)}")
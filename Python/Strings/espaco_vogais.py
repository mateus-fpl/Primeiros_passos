nome = input("Digite o seu nome: ").lower()
vogais = "aeiou"

contador = 0
vazio = 0

for letra in nome:
    if letra in vogais:
        contador +=1

print(f"Eu encontrei {contador} vogais.")

for letra in nome:
    if letra == " ":
        vazio +=1

print(f"Eu encontrei {vazio} espaços vazios")
import random

palavras = []
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        palavras.append(linha.strip())

palavra_secreta = random.choice(palavras)

letras = list(palavra_secreta)
random.shuffle(letras)
palavra_embaralhada = "".join(letras)

tentativas = 6
ganhou = False

print("--- JOGO DA PALAVRA EMBARALHADA ---")
print(f"Descubra a palavra: {palavra_embaralhada}")

while tentativas > 0:
    chute = input(f"\nTentativa ({tentativas} restantes): ").lower()

    if chute == palavra_secreta:
        ganhou = True
        break
    else:
        tentativas -= 1
        print("Errado! Tente novamente.")

if ganhou:
    print(f"\nParabéns! Você acertou. A palavra era: {palavra_secreta}")
else:
    print(f"\nQue pena! Suas tentativas acabaram. A palavra era: {palavra_secreta}")
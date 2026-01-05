import random

palavras_da_forca = ["cachorro", "gato", "gorila", "girafa", "albatroz", "aveztruz", "raposa", "hipopotamo"]
palavra_secreta = random.choice(palavras_da_forca)
sombra_palavra = ["_"] * len(palavra_secreta)
erros = 0 

while erros < 6 and "_" in sombra_palavra:
    print("\nPalavra:", " ".join(sombra_palavra))
    
    chute = input("Digite uma letra: ").lower() 

    achou = False

    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == chute:
            sombra_palavra[i] = chute
            achou = True

    if not achou:
        erros += 1
        print(f"-> Você errou pela {erros}ª vez. Tente de novo!")

if "_" not in sombra_palavra:
    print("\nParabéns! Você descobriu a palavra:", palavra_secreta)
else:
    print("\nQue pena! Você foi enforcado.")
    print(f"A palavra era: {palavra_secreta}")
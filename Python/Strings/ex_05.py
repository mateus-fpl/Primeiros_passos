nome = input("Escreva seu nome: ")
tamanho_nome = len(nome)

for i in range (tamanho_nome):
    for j in range (tamanho_nome - i):
        print(nome[j], end="")
    print()
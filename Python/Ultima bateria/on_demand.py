# Crie um programa para uma nova plataforma de vídeo sob demanda o qual deve armazenar o título da série e o 
# nome dos 2 principais atores. Ao final, o programa deve exibir uma listagem contendo, de forma ordenada, o 
# nome da série e os nomes dos atores.

filmes = {}

for cadastro_filmes in range (2):
    nome_filme = input("Digite o nome do filme: ")
    ator_principal = input("Digite o nome do(a) protagonista: ")
    ator_coadjuvante = input("Digite o nome do(a) coadjuvante: ")
    ("")
    filmes[nome_filme] = [ator_principal, ator_coadjuvante]

ordem_alfabetica = sorted(filmes)
    
for filme in ordem_alfabetica:
    atores = filmes[filme]
    ator_principal = atores[0]
    ator_coadjuvante = atores[1]
    print(f"Filme: {nome_filme}")
    print(f"Protagonista: {ator_principal} | Coadjuvante: {ator_coadjuvante}")


    






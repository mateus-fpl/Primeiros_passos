salas = int(input("Números de salas: "))
qtde_alunos = []
media = 0

if salas >= 1:

    for i in range(salas):
        alunos = int(input(f"Digite a quantidade de alunos da {i+1}° sala: "))
        if alunos <= 40:
            qtde_alunos.append(alunos)
        else:
            print("Erro! Os alunos excederam o limite da sala")  

    if len(qtde_alunos) >0:     
        media = sum(qtde_alunos) / len(qtde_alunos)
    else:
        print("Erro! Digite ao menos uma sala")

print(f"São: {salas} salas com a média de {media} alunos por sala.")
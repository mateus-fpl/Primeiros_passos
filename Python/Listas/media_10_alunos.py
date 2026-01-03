todas_as_medias = []

for i in range(10):
    print(f"{i+1}° aluno(a): ")
    notas_aluno = []
    for j in range(4):
        nota = float(input(f"Insira a {j+1} nota do(a) {i+1}° aluno(a): "))
        notas_aluno.append(nota)

    media_desse_aluno = sum(notas_aluno)/len(notas_aluno)
    todas_as_medias.append(media_desse_aluno)


aprovados = 0

for m in todas_as_medias:
    if m >= 7:
        aprovados += 1

print(f"Os alunos com notas igual ou superior a 7 são: {aprovados}")
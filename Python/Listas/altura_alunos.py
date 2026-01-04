vetor_idade = []
vetor_altura = []

for i in range(30):
    print(f"Digite a idade e altura do(a) {i+1} aluno(a):")
    idade = int(input(f"Digite a idade do(a) {i+1}° aluno(a):"))
    altura = float(input(f"Digite a altura do(a) {i+1}° aluno(a): "))
    print()
    vetor_idade.append(idade)
    vetor_altura.append(altura)

media = sum(vetor_altura)/len(vetor_altura)

alunos = 0

for i in range(len(vetor_idade)): 
    if vetor_idade[i] > 13 and vetor_altura[i] < media:
        alunos += 1

print(f"Média de altura do grupo: {media:.2f}")
print(f"Os alunos(as) com altura abaixo da média são {alunos} alunos(as)")
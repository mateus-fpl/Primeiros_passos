vetor_idade = []
vetor_peso = []

for i in range(5):
    print(f"Digite a idade e altura do(a) {i+1} aluno(a):")
    idade = int(input(f"Digite a idade do(a) {i+1}° aluno(a):"))
    peso = float(input(f"Digite o peso do(a) {i+1}° aluno(a): "))
    print()
    vetor_idade.append(idade)
    vetor_peso.append(peso)
    
    
for i in reversed(range(5)):
    print(f"A idade do(a) {i+1}° aluno(a) é {vetor_idade[i]} e seu peso é {vetor_peso[i]} kg")
    

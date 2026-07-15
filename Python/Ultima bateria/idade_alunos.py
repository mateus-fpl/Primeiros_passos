# Crie um programa no qual o usuário informe a idade de um número indeterminado de alunos. Para encerrar a 
# leitura dos dados, o usuário deve informar uma idade negativa. No final, o programa deve mostrar a média 
# aritmética entre a maior e a menor idade.

alunos = []
print("Quando quiser parar, coloque uma idade negativa.")
while True:
    try:
        idade = int(input("Digite a idade do(a) aluno(a): "))
        if idade < 0:
            break
        alunos.append (idade)
    except ValueError:
        print("Apenas números inteiros são aceitos!")


if len(alunos) > 0:
    maior = max(alunos)
    menor = min(alunos)  
    media = (maior + menor)/2
    print(f"A média entre {max(alunos)} e {min(alunos)} é: {media:.2f}")
else:
    print("Nenhum aluno foi registrado.")
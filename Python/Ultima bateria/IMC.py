# Construa um programa no qual o usuário informe o nome, a estatura e o peso de vários alunos de uma turma. 
# Após o cadastro, o programa deve imprimir o nome e o IMC de cada aluno ordenados pelo nome do aluno
import math
print ("-------- Cadastro IMC --------")
print("")

cadastro_aluno = []
IMC_aluno = []

while True:
    try:
        n = (int(input("Alunos cadastrados: ")))
        if n > 0:
            break
        else:
            print("Número inválido!")
    except ValueError:
        print ("Apenas números inteiros maiores que zero serão aceitos!")

for i in range (n):
    nome = input(f"Digite o nome do(a) {i+1}º aluno(a): ")
    while True:
        try:
            peso = float(input(f"Digite o peso do(a) {i+1}º aluno(a): "))
            altura = float(input(f"Digite a altura do(a) {i+1}º aluno(a): "))
            imc = peso/math.pow(altura,2)
            if peso > 0 and altura > 0:
                cadastro_aluno.append([nome,peso,altura,imc])
                break
            else:
                print("Número inválido!")
        except ValueError:
            print ("Recadastre os dados do último aluno.")

imc_ordem_alfabetica = sorted(cadastro_aluno)

for aluno in imc_ordem_alfabetica:
    nome_aluno = aluno[0]
    imc_aluno = aluno[3]
    print(f"Nome do(a) aluno(a): {nome_aluno} | IMC: {imc_aluno:.2f}.")
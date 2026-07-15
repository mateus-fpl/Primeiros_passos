# Crie um programa no qual o usuário informe o número de linhas e o número de colunas de uma matriz M e, em seguida,
#  o usuário deve digitar os elementos de M. Ao fim, o programa deve informar se M é uma matriz identidade.

matriz = []

while True:
    try:
        linhas = int(input("Por favor, digite a quantidade de linhas da matriz: "))
        colunas = int(input("Por favor, digite a quantidade de colunas da matriz: "))
        if linhas > 0 and colunas > 0:
            break
        else:
            print("Para linhas ou colunas, digite apenas números positivos inteiros!")
    except ValueError:
        print("")
        print("Preencha os valores novamente")
        print("")

for i in range (linhas):
    linha_provisoria = []
    for j in range (colunas):
        n = int(input(f"Digite o {j+1}º valor: "))
        linha_provisoria.append(n)
    matriz.append(linha_provisoria)

print ("---------- Matriz ----------")
for linhas in matriz:
    print (linhas)


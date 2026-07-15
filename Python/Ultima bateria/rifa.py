# Uma turma de formandos está vendendo rifas para angariar recursos financeiros para sua cerimônia de formatura. 
# Construa um programa para cadastrar os nomes das pessoas que compraram a rifa. Ao fim, o programa deve sortear o 
# ganhador do prêmio e imprimir o seu nome.

import random

compradores_rifa = []
numero_rifa = []

print ("---------- Rifa da Esfirra ----------")
print("Tire o número premiado e encha o bucho de esfirras (bebidas não inclusas)!")


while True:
    try:
        n = int(input("Quantas pessoas compraram a rifa? \n"))
        break
    except ValueError:
        print("Apenas números são aceitos!")


for i in range (n):
    nome = input(f"Digite o nome da {i+1}º pessoa que comprou a rifa: ")
    compradores_rifa.append(nome)
    while True:
        try:
            numero = int(input("Digite o número que a pessoa comprou: "))
            if numero in numero_rifa:
                print("Apenas números diferentes são aceitos!")
            else:
                numero_rifa.append(numero)
                break
        except ValueError:
            print("Apenas números inteiros são aceitos!")


numero_vencedor = random.choice(numero_rifa)
indice_vencedor = numero_rifa.index(numero_vencedor)
comprador_vencedor = compradores_rifa[indice_vencedor]

print(f"O vencedor da Rifa foi {comprador_vencedor} com o número {numero_vencedor}.")
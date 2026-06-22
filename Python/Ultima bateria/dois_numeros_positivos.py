# Construa um programa que solicite ao usuário dois números positivos. Em seguida, o programa deve apresentar o seguinte menu:
# 1. Média ponderada, com pesos 2 e 3, respectivamente 2. Quadrado da soma dos 2 números 3. Cubo do menor número 
# Escolha uma opção: De acordo com a opção informada, o programa deve calcular a operação apresentada no menu. 
# Se a opção escolhida for inválida, o programa deve mostrar a mensagem “Opção inválida” e ser encerrado.

import math

continuar = 's'

while continuar.lower() == 's':


    while True:
        try:
            numero1 = int(input("Por favor, digite um número inteiro positivo:"))
            numero2 = int(input("Por favor, digite outro número inteiro positivo: "))
            if numero1 <=0 or numero2 <=0:
                print("Número inválido! Devem ser maiores que zero")
                continue
            break
        except ValueError:
            print("Erro! Você deve digitar apenas números inteiros. Tente novamente.")
   

print(" ")
print("Por favor, escolha uma das opções abaixo:\n 1-Media Ponderada\n 2-Quadrado da Soma\n 3-Cubo do Menor valor")
print(" ")
opcao = int(input("Sua opção: "))

match opcao:
    case 1:
      media_ponderada = ((numero1 * 2) + (numero2 * 3))/5
      print(f"O resultado da média ponderada é {media_ponderada}")
    case 2:
      if opcao == 2:
         soma = numero1 + numero2
         quadrado = math.pow(soma,2)
         print(f"O quadrado da soma dos dois números é: {quadrado}")
    case 3:
      
      if opcao == 3:
        if numero1 < numero2:
           cubo = math.pow(numero1,3)
           print(f"O cubo do menor numero é: {cubo}")
        elif numero1 > numero2:
           cubo = math.pow(numero2,3)
           print(f"O cubo do menor numero é: {cubo}")
           cubo = math.pow(numero2,3)
        else:
           print(f"{numero1} e {numero2} são equivalentes.")
    case _:
            print("Opção Inválida")
print("—" * 30)
continuar = input("Deseja realizar outra operação? (s/n): ")

print("\nObrigado por usar o sistema! Programa encerrado.")
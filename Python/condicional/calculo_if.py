num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))

print("Escolha uma das operações abaixo: \n")
print(" +\n -\n /\n *\n")

operacao = input("Qual operação você gostaria de realizar?")

match operacao:
    case '+':
        print("Você escolheu a SOMA")
        resultado = num1 + num2
        print(f"O resultado é:\n {resultado}")
    case '-':
        print ("Você escolheu a Subtração")
        resultado = num1 - num2
        print(f"O resultado é:\n {resultado}")
    case '/':
       if num2 != 0:
        print ("Você escolheu a DIVISÃO:")
        resultado = num1 / num2
        print(f"O resultado é:\n {resultado}")
       else:
        print("ERRO! Não é possível dividir por 0!")
    case '*':
        print ("Você escolheu a MULTIPLICAÇÃO:")
        resultado = num1 * num2
        print(f"O resultado é:\n {resultado}")
    case _:
        print("Por favor, escolha uma das operações acima")



if resultado >0:
        print(f"O resultado é POSITIVO")
elif resultado <0:
        print(f"O resultado é NEGATIVO")
else: 
        print("O resultado é 0")

numero = int(input("Digite um número para fazer a tabuada: "))

for i in range(10):
    i = i + 1
    resultado = numero * i
    print(f"{numero} * {i} = {resultado} ")
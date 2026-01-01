numero = int(input("Digite um número para fazer a tabuada: "))
i = 0
for i in range(10):
    i = i + 1
    resultado = numero * i
    print(f"{numero} * {i} = {resultado} ")
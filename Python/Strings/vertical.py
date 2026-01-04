nome = input("Escreva seu nome: ")

nome_invertido = nome[::-1]

for i in range(len(nome_invertido)):
    print (nome_invertido[:i+1])
def imprimir_piramide(n):
    for i in range(1, n + 1):
        linha = ""
        for j in range(i):
            linha += str(j + 1) + " "
        print(linha)

numero = int(input("Digite o valor de n: "))
imprimir_piramide(numero)
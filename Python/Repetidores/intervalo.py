numeros = []
while True:
    try:
        num1 = float(input("Digite o primeiro número inteiro: "))
        num2 = float(input("Digite o segundo número inteiro: "))
        if num1 % 1 == 0 and num2 % 1 == 0:
            inicio = int(min(num1, num2))
            final = int(max(num1,num2))
            for i in range(inicio +1, final):
                numeros.append(i)
                print(i, end=" ")

            print()
            break
        else:
            print("Digite um número válido")
    except ValueError:
        print("Erro: Isso nem sequer é um número! Digite apenas algarismos.")

soma = sum(numeros)
print(f"A soma dos números é: {soma}")


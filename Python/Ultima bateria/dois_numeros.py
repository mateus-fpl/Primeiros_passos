# Crie um programa no qual o usuário informe 2 números inteiros: a e b. Para que o 
# programa continue sua execução, verifique se a < b. Se sim, calcule a soma dos números inteiros no intervalo [a, b].
# Caso contrário, informe uma mensagem de erro.

while True:
    try:
        numero1 = int(input("Por favor, digite o primeiro número inteiro: "))
        numero2 = int(input("Por favor, digite o segundo número inteiro: "))
        break
    except ValueError:
        print("Digite apenas números inteiros!")


soma = 0
if numero1 < numero2:
    for i in range (numero1,numero2 +1):
        soma += i
else:
    print("Erro!")

print(f"A soma dos do intervalo fechado entre {numero1} e {numero2} é {soma}")

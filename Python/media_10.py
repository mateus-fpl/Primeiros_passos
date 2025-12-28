soma = 0
num = int(input("Digite um número:"))

for i in range(num):
    valor_digitado = float(input(f"Digite o {i + 1}º valor: "))
    soma += valor_digitado


if num > 0:
    media = soma/num
print(f"O resultado final é {soma} e a média dos valores é {media}")

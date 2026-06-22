# Uma imobiliária paga aos seus corretores um salário base de R$ 1.500,00. 
# Além disso, uma comissão de R$ 200,00 por cada imóvel vendido e 5% do valor de cada venda. 
# Construa um programa que solicite o nome do corretor, a quantidade de imóveis vendidos e o valor total 
# de suas vendas. Ao fim, o programa deve calcular e escrever o salário final do corretor de imóveis.

casas_vendidas = []
total_vendas = []
salario = 1500.00

print("-------- Imobiliária Zezé --------")
vendedor = input("Por favor, digite seu nome: ")
vendas = int(input("Por favor, digite quantas casas você vendeu (Digite 0 em caso de nenhuma venda): "))
comissao = 0

if vendas > 0:
    for i in range (vendas):
        casa = float(input(f"Digite o valor da {i+1}º casa: "))
        casas_vendidas.append(casa)
        comissao = vendas * 200

        
else:
    print(" ")

total_vendas = sum(casas_vendidas) * 0.05
salario_final = salario + comissao + total_vendas

print ("-------- Resultado do mês --------")
print(" ")
print(f"Salário mensal: R$ {salario}")
print (f"O(A) funcionário(a) vendeu {vendas} imóveis.")
print (f"O bônus de R$ 200 a cada imóvel vendido totalizou: {comissao}")
print(f"A comissão de 5% sobre o valor total das vendas totalizou: R$ {total_vendas:.2f}")
print(f"O salário final a ser recebido é: R$ {salario_final:.2f}")
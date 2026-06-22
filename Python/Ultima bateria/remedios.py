# Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria 
# (considere que o usuário in-formou cinco medicamentos distintos). 
# O programa deve informar o nome e o preço do medicamento mais barato, 
# bem como a média aritmética dos preços informados.

while True:
    try:
        n = int(input("Por favor, digite quantos remédios você quer catalogar: "))
        break
    except ValueError:
        print("Apenas números inteiros serão aceitos.")

estoque = []
contagem = []

while True:
    try:
        for i in range (n):
            nome = str(input(f"Por favor, digite o nome do {i+1}º medicamento: "))     
            preco = float(input(f"Por favor, digite o preço do {i+1} medicamento: "))
            contagem.append([nome, preco])
            
        break
    except ValueError:
            print("Vamos ter que recomeçar o catálogo do zero para não salvar dados corrompidos.\n")
            contagem.clear()

    

estoque = contagem
media_precos = sum([item[1] for item in estoque]) / len(estoque)

menor_preco = min(estoque, key=lambda x: x[1])
maior_preco = max(estoque, key=lambda x: x[1])


print("------- Tabela de Preços -------")
print(estoque)
print(f"O menor preço é: {menor_preco[0]} por R$ {menor_preco[1]:.2f}")
print(f"O maior preço é: {maior_preco[0]} por R$ {maior_preco[1]:.2f}")
print(f"A média dos preços é: R$ {media_precos:.2f}")
def soma_imposto(taxa_imposto, custo):
    preco_com_imposto = custo + (custo * taxa_imposto / 100)
    return preco_com_imposto

c = float(input("Digite o custo do item: "))
t = float(input("Digite a taxa de imposto (ex: 15 para 15%):"))

resultado = soma_imposto(taxa_imposto=t,custo=c)
print(f"O preço com imposto é: R$ {resultado:.2f}")

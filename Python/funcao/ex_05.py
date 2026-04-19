def soma_imposto (custo, taxa_imposto):
    valor_final = custo + (custo * (taxa_imposto/100))
    return valor_final

preco = float(input("Digite o preço da compra: "))
taxa = float(input("Digite o valor da taxa: "))

preco2 = float(input("Digite o preço da compra: "))
taxa2 = float(input("Digite o valor da taxa: "))

preco_final = soma_imposto(preco, taxa)
preco_final2 = soma_imposto(preco2, taxa2)

print (preco_final)
print (preco_final2)
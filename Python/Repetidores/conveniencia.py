produto = int(input("Digite a quantidade de produtos comprados: "))
total = []
preco_total = 0
valor_recebido = 0
troco = 0

if produto == 0:
    print("Nenhum produto comprado")
    print()
else:

    for i in range(produto):
        compra = float(input(f"Produto {i+1}: R$  "))
        total.append(compra)

    preco_total = sum(total)
    print(f"Total: R$ {preco_total:.2f}")
    print()
    print('-' * 20)
    valor_recebido = float(input("Valor recebido: R$ "))
    print(f"Dinheiro: R$ {valor_recebido:>5.2f}")
    troco = valor_recebido - preco_total

print("Lojas Tabajara")

for indice, valor in enumerate(total):
    print(f"Produto {indice + 1}: R$ {valor:>5.2f}")
    
print(f"Total: R$ {preco_total:>5.2f}")
print(f"Dinheiro: R$ {valor_recebido:>5.2f}")
print(f"Troco: R$ {troco:>5.2f}")


preco_unitario = 1.99

print("Lojas Quase Dois - Tabela de Preços")

for i in range(1, 51):
    total = i * preco_unitario
    print(f"{i:2} - R$ {total:>5.2f}")
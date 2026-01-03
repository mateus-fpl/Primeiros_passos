pao = float(input("Digite o preço do pão: R$ "))

print("Padoca do Joaquim - Tabela de Preços")

for i in range(1, 51):
    total = i * pao
    print(f"{i:2} - R$ {total:>5.2f}")
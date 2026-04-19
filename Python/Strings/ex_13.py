numero_telefone = input("Digite um número de telefone: ").replace("-","")
print()
print(f"Telefone: {numero_telefone}")
if len(numero_telefone) == 8:
    print(f"O telefone é um número válido")
else:
    print("Telefone possui 7 dígitos. Vou acrescentar o número 3 na frente")
    print(f"Telefone corrigido sem formatação: 3{numero_telefone}")
    print(f"Telefone corrigido com formatação: 3{numero_telefone[:3]}-{numero_telefone[3:]}")
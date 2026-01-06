nome1 = input("Digite seu nome: ")
gastos1 = int(input("Digite seu gasto: "))
nome2 = input("Digite seu nome: ")
gastos2 = int(input("Digite seu gasto: "))

if gastos1 > gastos2:
    print(f"{nome1} teve mais gastos nesse mês")
elif gastos2 > gastos1:
    print(f"{nome2} teve mais gastos nesse mês")
else:
    print(f"{nome1} e {nome2} tiveram o mesmo gasto nesse mês")
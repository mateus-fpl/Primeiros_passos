def analisar_gasto(valor_salario, valor_despesa):
    despesa = (valor_despesa/valor_salario) * 100
    if despesa <= 30:
        return ("Gasto dentro do limite")
    else:
        return ("Gasto excessivo!")
    
gasto = analisar_gasto(1000,200)
gasto2 = analisar_gasto(1000,450)
print(gasto)
print(gasto2)
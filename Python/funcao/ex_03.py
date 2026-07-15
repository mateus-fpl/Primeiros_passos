def positivo_negativo(N):
    if N > 0:
        return "P"
    else:
        return "N"
    
valor_digitado = int(input("Número: "))
valor_digitado2 = int(input("Número: "))
    
etiqueta = positivo_negativo(valor_digitado)
etiqueta2 = positivo_negativo(valor_digitado2)
print(etiqueta)
print(etiqueta2)
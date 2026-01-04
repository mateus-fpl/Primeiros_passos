contadores = [0] * 9

print("--- Sistema de Comissões ---")
print("Digite as vendas (ou 0 para encerrar)")

while True:
    vendas = float(input("Vendas brutas do vendedor: "))
    
    if vendas == 0:
        break

    salario_total = 200 + (vendas * 0.09)
    
    indice = int((salario_total - 200) // 100)
    
    if indice > 8:
        indice = 8
    elif indice < 0:
        indice = 0
        
    contadores[indice] += 1

print("\n--- Resultado da Semana ---")

for i in range(8):
    faixa_inicio = 200 + (i * 100)
    faixa_fim = faixa_inicio + 99
    print(f"${faixa_inicio} - ${faixa_fim}: {contadores[i]} vendedor(es)")

print(f"$1000 em diante: {contadores[8]} vendedor(es)")
    
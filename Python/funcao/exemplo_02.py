def calcular_preco_final(valor_original, porcentagem_desconto):
    desconto = valor_original * porcentagem_desconto/100
    return valor_original - desconto


preco_final = calcular_preco_final(100,10)
preco_final_2 = calcular_preco_final(250,20)

print(f"O valor com desconto é {preco_final}")
print(f"O valor com desconto é {preco_final_2}")


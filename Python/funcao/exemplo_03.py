def verificar_disponibilidade(quantidade_estoque,quantidade_desejada):
       
    if quantidade_estoque >= quantidade_desejada:
        return("Compra aprovada")
    else:
        return("Estoque insuficiente")
    

compra = verificar_disponibilidade(10,5)
compra2 = verificar_disponibilidade(2,10)
compra3 = verificar_disponibilidade(5,5)

print(compra)
print(compra2)
print(compra3)


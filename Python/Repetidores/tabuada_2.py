num_tabuada = int(input("Montar a tabuada de: "))
comeco = int(input("Começar por: "))
fim = int(input("Terminar em: "))

if comeco > fim:
    print("Erro! O valor inicial não pode ser maior que o final.")
else:
    print(f"\nVou montar a tabuada de {num_tabuada} começando em {comeco} e terminando em {fim}:")
    
    for i in range(comeco, fim + 1):
        resultado = num_tabuada * i
        print(f"{num_tabuada} X {i} = {resultado}")
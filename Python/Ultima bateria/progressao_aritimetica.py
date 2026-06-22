while True:
    try:
        primeiro_termo = int(input("Por favor, digite o primeiro termo: "))
        razao = int(input("Por favor, digite a razão: "))
        quantidade_de_termos = int(input("Por favor, digite a quantidade de termos: "))
        break
    except ValueError:
        print("Serão aceitos apenas números inteiros.")

for i in range(quantidade_de_termos):
    print(primeiro_termo)
    primeiro_termo += razao


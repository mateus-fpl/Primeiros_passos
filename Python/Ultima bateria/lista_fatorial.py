# Crie um programa que solicite o usuário um número N ímpar maior que 1. Em seguida, preencha uma lista com N 
# números inteiros positivos (suponha que o usuário sempre digitará números inteiros positivos). Selecione o 
# elemento que está no centro da lista. Ao final, calcule e escreva o fatorial do elemento selecionado.

lista_numeros = []

while True:
    try:
        n = int(input("A quantidade de números da lista: "))
        if n <= 0:
           print("Apenas números positivos!") 
        else:
            break
    except ValueError:
        print("Apenas números inteiros!")

for i in range (n):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número da sua lista: "))
            if numero <= 0:
                print("Apenas números positivos!") 
            else:
                break
        except ValueError:
            print("Apenas números inteiros!")
    
    lista_numeros.append(numero)

indice_do_meio = len(lista_numeros) // 2


numero_do_meio = lista_numeros[indice_do_meio]
fatorial = 1

for i in range (numero_do_meio, 0, -1):
    fatorial = fatorial * i
    print(i)

print(f"O número do meio é {numero_do_meio} e o seu fatorial é {fatorial}")
# Imagine que você está desenvolvendo o backend de um sistema de RH. Você precisa criar uma função chamada 
# analisar_salarios.
# Essa função deve receber apenas um parâmetro: uma lista com os salários de vários funcionários da empresa.
# Dentro da função, você deve calcular e retornar uma tupla com duas informações:
# A média salarial da empresa.
# A quantidade de pessoas que ganham acima dessa média calculada.

def analisar_salarios(lista_salarios=None):
    if lista_salarios is None:
        lista_salarios = []
    if len(lista_salarios) == 0:
        return 0,0
    
    contador = 0

    media_salarial = sum(lista_salarios)/len(lista_salarios)

    for pagamento in lista_salarios:
        if pagamento > media_salarial:
            contador = contador + 1

    return media_salarial, contador

while True:
    try:
        funcionarios = int(input("Digite a quantidade de funcionários na empresa: "))
        if funcionarios > 0:
            print("Cadastro aceito")
            print(" ")
            break
        else:
            print("É funcionário fantasma?!")
            print("Faça de novo!")
    except ValueError:
        print("Apenas números inteiros são aceitos!")

media_soldos = []

for i in range(funcionarios):
    while True:
        try:
            salario = float(input(f"Digite o salário do(a) {i+1}º funcionário(a): "))
            if salario >= 1621.00:
                media_soldos.append(salario)
                break
            else:
                print("O coitado não merece nem um salário mínimo?!")
        except ValueError:
            print("Apenas números são aceitos!")
            print("Reiniciando cadastro...")
            print(" ")

            if salario > media_soldos:
                contador_salario = contador_salario + 1

media_final, total_acima = analisar_salarios(media_soldos)

print(f"\nA média dos salários é: R$ {media_final:.2f}.")
print(f"A quantidade de funcionários que ganham acima da média é: {total_acima}.")



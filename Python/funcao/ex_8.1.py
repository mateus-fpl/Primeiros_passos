# O mesmo sistema de RH agora precisa de um módulo para calcular o bônus de PLR (Participação nos Lucros e 
# Resultados) dos desenvolvedores no fim do ano. Crie uma função chamada calcular_plr. Ela deve receber um 
# parâmetro: uma lista contendo o salário de cada funcionário.
# A regra de negócio para o cálculo do bônus individual é:
# Se o funcionário ganha menos que R$ 3.000,00, o bônus dele será de 20% do seu salário.
# Se ele ganha R$ 3.000,00 ou mais, o bônus será de 15% do seu salário.
# Dentro da função, você deve calcular e retornar uma tupla com duas informações:
# O valor total que a empresa vai gastar somando o bônus de todo mundo.
# Uma nova lista contendo apenas os valores dos bônus calculados (ex: [500.0, 450.0, ...]).

def calcular_plr(lista_salarios=None):
    if lista_salarios is None:
        lista_salarios = []
    if len(lista_salarios) == 0:
        return 0, []
    
    gasto_total_bonus = 0
    lista_bonus = []
    
    for salario in lista_salarios:
        if salario <= 3000:
            bonus = salario * 0.20
        else:
            bonus = salario * 0.15
            
        lista_bonus.append(bonus)
        gasto_total_bonus = gasto_total_bonus + bonus
        
    return gasto_total_bonus, lista_bonus

while True:
    try:
        funcionarios = int(input("Digite a quantidade de funcionários: "))
        if funcionarios >= 1:
            break
        else:
            print("Cadastre ao menos um funcionário.\n")
    except ValueError:
        print("Apenas números inteiros positivos são aceitos!\n")

salarios_brutos = []

for i in range(funcionarios):
    while True:
        try:
            pagamento = float(input(f"O salário do(a) {i+1}º funcionário(a) é: "))
            if pagamento >= 1621:
                salarios_brutos.append(pagamento)
                break
            else:
                print("Cada funcionário deve receber ao menos um salário mínimo.")
        except ValueError:
            print("Apenas números são aceitos.\nReiniciando cadastro...\n")

custo_total_bonus, apenas_bonus = calcular_plr(salarios_brutos)

print("\n--- RELATÓRIO DE PLR ---")
for i, valor_bonus in enumerate(apenas_bonus):
    print(f"Bônus do(a) {i+1}º funcionário(a): R$ {valor_bonus:.2f}")

print(f"\nO gasto total da empresa APENAS com bônus é: R$ {custo_total_bonus:.2f}")



import math 

import math 

# ==========================================
# Ex 01 - Maior de dois números
# ==========================================
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
else:
    print(f"O maior número é: {num2}")

# ==========================================
# Ex 02 - Positivo ou Negativo
# ==========================================
num1 = float(input("Digite o primeiro número: "))

if num1 > 0:
    print(f"O número {num1} é positivo")
else:
    print(f"O número {num1} é negativo")

# ==========================================
# Ex 03 - Sexo Válido
# ==========================================
sexo = input("Digite 'M' para sexo masculino ou 'F' para sexo feminino: ")

if sexo == "M":
    print("M - masculino")
elif sexo == "F":
    print("F - feminino")
else:
    print("Sexo inválido!")

# ==========================================
# Ex 04 - Vogal ou Consoante
# ==========================================
letra = input("Digite uma letra ou uma palavra:")
primeiraLetra = letra[0]

if primeiraLetra.upper() in "AEIOU":
    print("A primeira letra é uma vogal")
else:
    print("A primeira letra é uma consoante")

# ==========================================
# Ex 05 - Média Aluno
# ==========================================
nota1 = float(input("Digite a primeira nota do aluno:"))
nota2 = float(input("Digite a segunda nota do aluno:"))
media = (nota1 + nota2)/2

if media == 10:
    print(f"Nota {media}, Aluno aprovado com distinção!")
elif media >= 7:
    print(f"Nota {media}, Aluno aprovado.")
else:
    print(f"Nota {media}, Aluno reprovado.")

# ==========================================
# Ex 06 - Maior de três
# ==========================================
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    print(f"O maior número é {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"O maior número é {num2}")
else:
    print(f"O maior número é {num3}")

# ==========================================
# Ex 07 - Menor de três
# ==========================================
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 <= num2 and num1 <= num3:
    print(f"O menor número é {num1}")
elif num2 <= num1 and num2 <= num3:
    print(f"O menor número é {num2}")
else:
    print(f"O menor número é {num3}")

# ==========================================
# Ex 08 - Menor Preço
# ==========================================
prod1 = float(input("Digite o primeiro produto: "))
prod2 = float(input("Digite o segundo produto: "))
prod3 = float(input("Digite o terceiro produto: "))

if prod1 <= prod2 and prod1 <= prod3:
    print(f"{prod1} tem o menor preço.")
elif prod2 <= prod1 and prod2 <= prod3:
    print(f"{prod2} tem o menor preço")
else:
    print(f"{prod3} tem o menor preço.")

# ==========================================
# Ex 09 - Ordem Decrescente
# ==========================================
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

meio = (num1 + num2 + num3) - maior - menor
print(f"Ordem descrescente: {maior}, {meio}, {menor}")

# ==========================================
# Ex 10 - Turno de Estudo
# ==========================================
periodo = input("Digite 'M' para matutino, 'V' para vespertino ou 'N' para noturno: ")
periodoEscolhido = periodo [0]

if periodoEscolhido.upper() == "M":
    print("Bom dia!")
elif periodoEscolhido == "V":
    print("Boa tarde!")
elif periodoEscolhido == "N":
    print("Boa noite!")
else:
    print("Período inválido!")

# ==========================================
# Ex 11 - Reajuste Salarial
# ==========================================
salario = float(input("Digite o valor do seu salário:"))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

valor_aumento = salario * (percentual / 100)
novo_salario = salario + valor_aumento 

print(f"Salário antes: R$ {salario:.2f}")
print(f"Percentual: {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

# ==========================================
# Ex 12 - Folha de Pagamento
# ==========================================
valorHora = float(input("Digite o valor da sua hora:"))
horasTrabalhadas = int(input("Digite suas horas trabalhadas:"))
pagamento = valorHora * horasTrabalhadas
if pagamento <= 900:
    IR = 0
elif pagamento <= 1500:
    IR = 5
elif pagamento <= 2500:
    IR = 10
else:
    IR = 20
descontoIR = pagamento * (IR / 100)
INSS = pagamento * 0.10
FGTS = pagamento * 0.11
totalDescontos = descontoIR + INSS
salarioLiquido = pagamento - totalDescontos

print(f"Salário bruto: ({valorHora} * {horasTrabalhadas}: R$ {pagamento:.2f})")
print(f"(-) IR ({IR}%): R$ {descontoIR:.2f}")
print(f"(-) INSS (10%): R$ {INSS:.2f}")
print(f"FGTS (11%): R$ {FGTS:.2f}")
print(f"Total de descontos: R$ {totalDescontos:.2f}")
print(f"Salário líquido: R$ {salarioLiquido:.2f}")

# ==========================================
# Ex 13 - Dia da Semana
# ==========================================
diaDaSemana = input("Digite um número:")

if diaDaSemana == "1":
    print("Domingo")
elif diaDaSemana == "2":
    print("Segunda")
elif diaDaSemana == "3":
    print("Terça")
elif diaDaSemana == "4":
    print("Quarta")
elif diaDaSemana == "5":
    print("Quinta")
elif diaDaSemana == "6":
    print("Sexta")
elif diaDaSemana == "7":
    print("Sábado")
else:
    print("Valor inválido!")

# ==========================================
# Ex 14 - Notas e Conceitos
# ==========================================
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2)/2

print(f"Média do(a) aluno(a): {media:.2f}")

if media >= 9:
    conceito = "A"
    print(conceito)
elif media > 7.5:
    conceito = "B"
    print(conceito)
elif media > 6:
    conceito = "C"
    print(conceito)
elif media > 4:
    conceito = "D"
    print(conceito)
else:
    conceito = "E"
    print(conceito)

if conceito == "A" or conceito == "B" or conceito == "C":
    print ("APROVADO!")
else:
    print("REPROVADO!")

# ==========================================
# Ex 15 - Triângulos
# ==========================================
ladoA = float(input("Coloque o primeiro lado do triângulo:"))
ladoB = float(input("Coloque o segundo lado do triângulo:"))
ladoC = float(input("Coloque o terceiro lado do triângulo:"))

if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
    print("Os lados formam um triângulo!")
    if ladoA == ladoB and ladoA == ladoC:
        print("Triângulo equilátero.")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("Triângulo Isósceles.")
    else:
        print("Triângulo escaleno!")
else:
    print("Não é um triângulo: a soma de dois lados deve ser maior que o terceiro.")

# ==========================================
# Ex 16 - Equação do 2º Grau
# ==========================================
a = float(input("Digite o valor de a: "))

if a == 0:
    print("O valor de 'a' não pode ser zero. Encerrando...")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
    delta = (b**2) - (4 * a * c)
    
    if delta < 0:
        print(f"Delta = {delta}. A equação não possui raízes reais.")
    else:
        raiz_delta = delta ** 0.5
        x1 = (-b + raiz_delta) / (2 * a)
        
        if delta == 0:
            print(f"A equação possui apenas uma raiz: {x1}")
        else:
            x2 = (-b - raiz_delta) / (2 * a)
            print(f"A equação possui duas raízes:")
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")

# ==========================================
# Ex 17 - Ano Bissexto
# ==========================================
ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    if ano % 100 != 0:
        print("Ano bissexto.")
    elif ano % 400 == 0:
        print("Ano bissexto.")
    else:
        print("Não é bissexto.")

# ==========================================
# Ex 18 - Data Válida
# ==========================================
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

valida = False 
ultimoDia = 0

if mes < 1 or mes > 12:
    print("Mês inválido!")
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    ultimoDia = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    ultimoDia = 30
elif mes == 2: 
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        ultimoDia = 29
    else:
        ultimoDia = 28

if ultimoDia > 0:
    if dia > 0 and dia <= ultimoDia:
            print(f"Data Válida! {dia}/{mes}/{ano}")
    else:
            print("Dia inválido para este mês!")

# ==========================================
# Ex 19 - Centenas, Dezenas e Unidades
# ==========================================
numero = int(input("Digite um numero menor que 1000: "))
centenas = numero // 100          
resto = numero % 100              
dezenas = resto // 10             
unidades = resto % 10             

print(f"{numero} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades")

# ==========================================
# Ex 20 - Média 3 Notas
# ==========================================
nota1 = float(input("Digite a primeira nota do aluno:"))
nota2 = float(input("Digite a segunda nota do aluno:"))
nota3 = float(input("Digite a terceira nota do aluno:"))
media = (nota1 + nota2 + nota3)/3

if media == 10:
    print(f"Nota {media}, Aluno aprovado com distinção!")
elif media >= 7:
    print(f"Nota {media}, Aluno aprovado.")
else:
    print(f"Nota {media}, Aluno reprovado.")

# ==========================================
# Ex 21 - Caixa Eletrônico
# ==========================================
dinheiro = float(input("Digite o valor que deseja sacar: "))
if dinheiro < 10 or dinheiro > 600:
    print("Programa encerrado")
else:
    notas100 = dinheiro // 100
    resto = dinheiro % 100
    notas50 = resto // 50
    resto = resto % 50
    notas10 = resto // 10
    resto = resto % 10
    notas5 = resto // 5
    resto = resto % 5
    notas1 = resto // 1
    resto = resto % 1
    print(f"Valor a sacar: {dinheiro}. Notas de 100: {notas100}. Notas de 50: {notas50}. Notas de 10: {notas10}. Notas de 5: {notas5}. Notas de 1: {notas1}")

# ==========================================
# Ex 22 - Par ou Ímpar
# ==========================================
numero = float(input("Digite um número: "))

if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número impar.")

# ==========================================
# Ex 23 - Inteiro ou Decimal
# ==========================================
numero = float(input("Digite um número: "))

if numero == int(numero):
    print(f"{numero} é um número inteiro.")
else:
    print(f"{numero} é um número decimal.")

# ==========================================
# Ex 24 - Operações Matemáticas
# ==========================================
num1 = float(input("Digite o primeiro valor:"))
num2 = float(input("Digite o segundo valor:"))

print("Qual operação você deseja realizar?")
print("1 - adição, 2- subtração, 3- multiplicação, 4- divisão")
operation = float(input())

deu_certo = True

if operation == 1:
    resultado = num1 + num2
elif operation == 2:
    resultado = num1 - num2
elif operation == 3:
    resultado = num1 * num2
elif operation == 4:
    if num2 == 0:
        print("Erro: Impossível divisão por 0")
        deu_certo = False
    else:
        resultado = num1 / num2
else:
    print("Opção inválida!")
    deu_certo = False

if deu_certo:
    print("-" * 20)
    print(f"Resultado da operação: {resultado}")

    if resultado % 2 == 0:
        print("É par.")
    else:
        print("É ímpar.")

    if resultado > 0:
        print("É positivo.")
    elif resultado < 0:
        print("É negativo.")
    else:
        print("É neutro (zero).")

    if resultado == int(resultado):
        print("É um número inteiro.")
    else:
        print("É um número decimal.")

# ==========================================
# Ex 25 - Investigação Criminal
# ==========================================
p1 = input("Telefonou para a vítima? (S/N): ").upper()
soma_sim = 0
if p1 == "S":
    soma_sim = soma_sim + 1
p2= input("Esteve no local do crime? (S/N):").upper()
if p2 == "S":
    soma_sim = soma_sim + 1
p3= input("Mora perto da vítima? (S/N):").upper()
if p3 == "S":
    soma_sim = soma_sim + 1
p4= input("Devia para a vítima? (S/N):").upper()
if p4 == "S":
    soma_sim = soma_sim + 1
p5= input("Já trabalhou com a vítima? (S/N):").upper()
if p5 == "S":
    soma_sim = soma_sim + 1

if soma_sim == 2:
    print("Suspeita")
elif soma_sim == 3 or soma_sim == 4:
    print("Cúmplice")
elif soma_sim == 5:
    print("Assassino")
else:
    print("Inocente")

# ==========================================
# Ex 26 - Posto de Combustível
# ==========================================
print("Qual combustível você deseja:")
print("A - álcool")
print("G - gasolina")
combustivel = input().upper()

valorGasolina = 2.50
valorAlcool = 1.90

if combustivel == "G":
    gasolina = float(input("Quantos litros de gasolina você deseja?"))

    if gasolina <= 20:
        tanqueGasolina = valorGasolina * 0.96
        totalGasolina = tanqueGasolina * gasolina
        print(f"Combustível vendido: {combustivel}. Valor a ser pago: R$ {totalGasolina:.2f}")
    else:
        tanqueGasolina = valorGasolina * 0.94
        totalGasolina = tanqueGasolina * gasolina
        print(f"Combustível vendido: {combustivel}. Valor a ser pago: R$ {totalGasolina:.2f}")
elif combustivel == "A":
    alcool = float(input("Quantos litros de álcool você deseja?"))

    if alcool <= 20:
        tanqueAlcool = valorAlcool * 0.97
        totalAlcool = tanqueAlcool * alcool
        print(f"Combustível vendido: {combustivel}. Valor a ser pago: R$ {totalAlcool:.2f}")
    else:
        tanqueAlcool = valorAlcool * 0.95
        totalAlcool = tanqueAlcool * alcool
        print(f"Combustível vendido: {combustivel}. Valor a ser pago: R$ {totalAlcool:.2f}")
else:
    print("Escolha inválida!")

# ==========================================
# Ex 27 - Fruteira
# ==========================================
kg_morango = float(input())
kg_maca = float(input())

if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

valor_total = preco_morango + preco_maca
peso_total = kg_morango + kg_maca

if peso_total > 8 or valor_total > 25:
    valor_total *= 0.90

print(f"R$ {valor_total:.2f}")

# ==========================================
# Ex 28 - Hipermercado Tabajara
# ==========================================
tipo = int(input())
qtd = float(input())
cartao = input().upper()

if tipo == 1:
    nome = "File Duplo"
    preco_kg = 4.90 if qtd <= 5 else 5.80
elif tipo == 2:
    nome = "Alcatra"
    preco_kg = 5.90 if qtd <= 5 else 6.80
else:
    nome = "Picanha"
    preco_kg = 8.50 if qtd <= 5 else 11.00

bruto = qtd * preco_kg
desconto = bruto * 0.05 if cartao == "S" else 0
liquido = bruto - desconto

print(f"Carne: {nome}")
print(f"Qtd: {qtd}kg")
print(f"Bruto: R$ {bruto:.2f}")
print(f"Desc: R$ {desconto:.2f}")
print(f"Total: R$ {liquido:.2f}")
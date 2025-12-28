import math
#1:
print ("Olá mundo!\n")

#2:
numero = int(input("Informe um número: "))
print (f"O número informado foi {numero}\n")

#3
print("Informe dois números:")
alg1 = int(input("Primeiro número: "))
alg2 = int(input("Segundo número:"))
soma = alg1 + alg2
print(f"A soma dos números é: {soma}\n")

#4:
print("Digite as notas do(a) aluno(a):")
not1 = float(input("Digite a primeira nota:"))
not2 = float(input("Digite a segunda nota:"))
not3 = float(input("Digite a terceira nota:"))
not4 = float(input("Digite a quarta nota:"))
media = (not1 + not2 + not3 + not4)/4
print(f"A média do(a) aluno(a) é: {media}\n")

#5
metro = float(input("Digite a distância em metros:"))
centimetros = metro * 100
print(f"{metro} em centímeros é: {centimetros}\n")

#6
raio = float(input("Digite o raio do círculo:"))
area = 3.14 * (raio ** 2)
print(f"A área do círculo é: {area}\n")

#7
tamanho = float(input("Digite o tamanho do quadrado:"))
areaQuad = tamanho ** 2
dobro = areaQuad * 2
print(f"A área do quadrado é: {areaQuad} e seu dobro é {dobro}\n")

#8
valorHora = float(input("Digite o valor da sua hora trabalhada:"))
HorasTrabalhadas = int(input("Digite quantas horas você trabalhou:"))
pagamento = valorHora * HorasTrabalhadas
print(f"Horas trabalhadas: {HorasTrabalhadas}. Valor da hora: {valorHora}. Salário a receber nesse mês é: R${pagamento}")

#9
F = float(input("Digite a temperatura em Fahrenheit: "))
C = 5 * ((F-32) / 9)
print(f"{F}º Fahrenheit convertido em Celsius é: {C:.2f}\n")

#10
Cc = float(input("Digite a temperatura em Celsius: "))
Ff = (Cc * 9/5) + 32
print(f"{Cc}º Celsius convertido em Fahrenheit é: {Ff:.2f}°\n")

#11
print("Digite dois números inteiros:")
int1 = int(input())
int2 = int(input())
print("Digite um número real:")
real = float(input())
result1 = (int1 * 2) * (int2 / 2)
result2 = (int1 * 3) + real
result3 = real ** 3
print(f"O produto do dobro do {int1} com metade do {int2} é: {result1}")
print(f"A soma do triplo do {int1} com o {real} é: {result2}")
print(f"O {real} elevado ao cubo é: {result3:.2f}")

#12
Gigabytes = int(input("Quantos GB tem sua máquina: "))
Megabytes = Gigabytes * 1024
print(f"Seu PC tem {Megabytes:.2f} MB.\n")

#13
Gigabytes = int(input("Quantos GB tem sua máquina: "))
Megabytes = Gigabytes * 1024
Kilobytes = Gigabytes * 1024 * 1024
print(f"Seu PC tem {Megabytes:2.f} MB e tem {Kilobytes:2.f} KB.\n")

14#
peso = float(input("Digite o peso do seu peixe: "))
excesso = peso - 50
multa = excesso * 4
if peso > 50:
    print(f"O peso total do peixe foi: {peso:.2f}. O excesso foi de {excesso:.2f} quilos. A multa é: {multa:.2f}")
else:
    print(f"O peso total do peixe foi: {peso:.2f}. Nenhuma multa imposta.\n")

#15
valorHora = float(input("Digite o valor da sua hora trabalhada: "))
HorasTrabalhadas = int(input("Digite quantas horas você trabalhou: "))
pagamento = valorHora * HorasTrabalhadas
IR = pagamento * 0.11
INSS = pagamento * 0.08
sindicato = pagamento * 0.05
descontos = IR + INSS + sindicato
pagamentoLiquido = pagamento - descontos
print(f"Horas trabalhadas: {HorasTrabalhadas:.2f}. Valor da hora: {valorHora:.2f}.")
print(f"Salário bruto do mês é: R${pagamento:.2f} reais.")
print(f"Desconto IR: {IR:.2f} reais.")
print(f"Desconto INSS: {INSS:.2f} reais.")
print(f"Desconto sindicato: {sindicato:.2f} reais.")
print(f"Total dos descontos: {descontos:.2f} reais.")
print(f"Salário líquido a receber: {pagamentoLiquido:.2f} reais.")

#16
metrosQuadrados = float(input("Informe os metros quadrado que serão pintados: "))
litros = metrosQuadrados/3
latas = math.ceil (litros/18)
precoTotal = latas * 80.00
print("A cobertura da tinta é de 1 litro para cada 3M². Quantidade da lata: 18 litros e custam R$ 80,00.")
print(f"Área de pintura: {metrosQuadrados:.2f}. Litros necessários: {litros:.2f}")
print(f"Quantidade de latas para uso: {latas}. Preço total: {precoTotal:.2f} reais.")

17#
metrosQuadrados = float(input("Informe os metros quadrados que serão pintados: "))
litrosComFolga = (metrosQuadrados / 6) * 1.1
# 1 - Situação apenas latas (18L)
latas = math.ceil(litrosComFolga / 18)
precoTotalLata = latas * 80.00
# 2 - Situação apenas galões (3.6L)
galao = math.ceil(litrosComFolga / 3.6)
precoTotalGalao = galao * 25.00
# 3 - Situação Mista (Latas e Galões)
misturaLatas = int(litrosComFolga / 18)
restoTinta = litrosComFolga - (misturaLatas * 18)
misturaGaloes = math.ceil(restoTinta / 3.6)
precoMistura = (misturaLatas * 80.00) + (misturaGaloes * 25.00)

print("-" * 50)
print(f"Litros necessários com folga de 10%: {litrosComFolga:.2f}L")
print(f"Opção 1 (Só latas): {latas} latas - R${precoTotalLata:.2f}")
print(f"Opção 2 (Só galões): {galao} galões - R${precoTotalGalao:.2f}")
print(f"Opção 3 (Mistura): {misturaLatas} latas e {misturaGaloes} galões - R${precoMistura:.2f}")

18#
tamanhoArquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidadeInternet = float(input("Digite a velocidade da internet em mbps: "))
mbps = velocidadeInternet/8
segundos = tamanhoArquivo / mbps
minutos = segundos/60
print(f"O arquivo tem {tamanhoArquivo} MB e a velocidade da internet está em {mbps} MB/s.")
print(f"Tempo estimado para download: {minutos:.2f} minutos")
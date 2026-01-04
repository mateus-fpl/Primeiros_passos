notas = []

print("Digite as notas (ou -1 para encerrar):")
while True:
    n = float(input("Nota: "))
    if n == -1:
        break
    notas.append(n)

quantidade = len(notas)
soma = sum(notas)
media = soma / quantidade if quantidade > 0 else 0

acima_media = 0
abaixo_sete = 0
for nota in notas:
    if nota > media:
        acima_media += 1
    if nota < 7:
        abaixo_sete += 1

print(f"\n--- RELATÓRIO FINAL ---")
print(f"a) Quantidade de valores lidos: {quantidade}")

print("b) Valores na ordem informada:", end=" ")
for n in notas:
    print(n, end=" ")
print() 

print("c) Valores na ordem inversa:")
notas_reversas = notas[::-1]
for n in notas_reversas:
    print(n)

print(f"d) Soma dos valores: {soma:.2f}")
print(f"e) Média dos valores: {media:.2f}")
print(f"f) Quantidade acima da média: {acima_media}")
print(f"g) Quantidade abaixo de sete: {abaixo_sete}")

print("\nPrograma encerrado com sucesso. Bons estudos!")
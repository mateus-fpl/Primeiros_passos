idades = []
num = int(input("Digite quantas idades você quer registrar: "))

for i in range(num):
    alg = int(input(f"Digite a {i+1}° idade: "))
    idades.append(alg)
print()

if len(idades) > 0:
    media = sum(idades)/len(idades)

    if len(idades) >= 0 and len(idades) <= 25:
        print(f"A média é: {media}")
        print("A média do grupo é composta de pessoas jovens.")
    elif len(idades) >= 26 and len(idades) <= 60:
        print(f"A média é: {media}")
        print("A média do grupo é composta de pessoas adultas")
    else:
        print(f"A média é: {media}")
        print("A média do grupo é composta de pessoas idosas")
else:
    print("Nenhuma idade digitada.")
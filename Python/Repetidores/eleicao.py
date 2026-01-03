candidato_A = 0
candidato_B = 0
candidato_C = 0
invalido = 0

eleitores = int(input("Digite o número de eleitores: "))
print()
print("Digite 13 para candidato A")
print("Digite 22 para candidato B")
print("Digite 45 para candidato C")
print()

for i in range(eleitores):
    voto = int(input(f"Digite o {i+1}° voto: "))
    if voto == 13:
        candidato_A += 1
    elif voto == 22:
        candidato_B += 1
    elif voto == 45:
        candidato_C += 1
    else:
        invalido += 1


if eleitores > 0:
    print(f"Candidato A recebeu: {candidato_A} votos.")
    print(f"Candidato B recebeu: {candidato_B} votos.")
    print(f"Candidato C recebeu: {candidato_C} votos.")
    print(f"Invalidos: {invalido} votos.")
else:
    print("Nenhuma pessoa votou. Eleição cancelada!")
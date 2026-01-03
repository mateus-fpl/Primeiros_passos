notas = []
alg = int(input("Digite quantas notas você vai avaliar: "))

for i in range(alg):
    num = float(input(f"Digite a {i+1}° nota: "))
    notas.append(num)
    
print()
if len(notas) > 0:
    media = sum(notas)/len(notas)
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi digitada")




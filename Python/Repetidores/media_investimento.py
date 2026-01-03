CDs = int(input("Digite quantos CDs você comprou: "))
investimento = []
media = 0

if CDs > 0:
    for i in range(CDs):
        compra = int(float(input(f"custo do {i+1}° CD: R$ ")))
        investimento.append(compra)
    
    media = sum(investimento)/len(investimento)
   

else:
    print("Mão de vaca!")

print(f"Você comprou: {CDs} e gastou em média {media:.2f} por cada CD.")
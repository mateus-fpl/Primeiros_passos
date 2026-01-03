temperaturas = int(input("Digite quantas temperaturas estão sendo avaliadas: "))
clima = []

for i in range(temperaturas):
    analise = float(input(f"Digite a {i + 1}° temperatura em °C: "))
    clima.append(analise)

maior = max(clima)
menor = min(clima)

media = sum(clima)/len(clima)

print()
print(f"A menor temperatura registrada foi de {menor:.2f}°C")
print(f"A maior temperatura registrada foi de {maior:.2f}°C")
print(f"A média das temperaturas foi de {media:.2f}°C")
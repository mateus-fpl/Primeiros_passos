temperatura_media = []

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for i in range(12):
    temperatura = float(input(f"Digite a temperatura no {i+1}° mês: "))
    temperatura_media.append(temperatura)

media = sum(temperatura_media)/len(temperatura_media)    

print(f"A média das temperaturas no últmo ano foi: {media:.2f}")
print(f"Os meses que superaram a média: ")

for i in range(len(temperatura_media)):
    if temperatura_media[i] > media:
        print(f"{i+1} - {meses[i]}: {temperatura_media[i]}°C")
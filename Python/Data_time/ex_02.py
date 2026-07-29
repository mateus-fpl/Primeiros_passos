from datetime import datetime

data_usuario = input("Digite uma data no fromato DD/MM/AAAA: ")

data_convertida = datetime.strptime(data_usuario, "%d/%m/%Y")
print(data_convertida)
hoje = datetime.now()

if data_convertida < hoje:
    print("Alerta: Esta data já passou!")
else:
    dias_restantes = data_convertida - hoje
    print(f"Faltam {dias_restantes.days} dias para essa data.")


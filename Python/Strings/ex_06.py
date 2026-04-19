data_nascimento = input("Coloque sua data de nascimento: ")

meses = ["","janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
partes_data = data_nascimento.split("/")
mes_numero = int(partes_data[1])

print(f"Data de nascimento: {partes_data[0]} de {meses[mes_numero]} de {partes_data[2]}")

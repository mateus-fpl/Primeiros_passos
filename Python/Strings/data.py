meses = ["","janeiro", "feveiro", "março", "abril", "maio", "junho", "julho", 
        "agosto", "setembro", "outubro", "novembro", "dezembro"]

data = input("Digite sua data de nascimento: ")
divisao = data.split("/")

mes_por_extenso = meses[int(divisao[1])] 

print(f"Você nasceu em {divisao[0]} de {mes_por_extenso} de {divisao[2]}")

from datetime import datetime

nascimento = input("Digite sua data de nascimento: ")
nascimento_convertido = datetime.strptime(nascimento, "%d/%m/%Y")

dias_existentes = datetime.now() - nascimento_convertido
print(f"Você está no mundo há {dias_existentes.days} dias.")
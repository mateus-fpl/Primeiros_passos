from datetime import datetime

inicio = datetime.now()

for i in range (1000000000):
    pass

fim = datetime.now()

duracao = fim - inicio
print(f"O processamento levou {duracao.total_seconds()} segundos.")
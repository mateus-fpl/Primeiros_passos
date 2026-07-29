from datetime import datetime
import calendar

agora = datetime.now()
dia_inicio, ultimo_dia = calendar.monthrange(agora.year, agora.month)

print(f"O mês {agora.month}/{agora.year} tem {ultimo_dia} dias.")
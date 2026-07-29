from datetime import datetime, timedelta

vencimento = input("Por favor, digite a data de vencimento da fatura: ")
vencimento_convertido = datetime.strptime(vencimento, "%d/%m/%Y")
dia_da_semana = vencimento_convertido.weekday()

if dia_da_semana == 5:
    vencimento_convertido = vencimento_convertido + timedelta(days=2)
    print(f"Vencimento cai no sábado. Data ajustada automaticamente para {vencimento_convertido.strftime('%d/%m/%Y')}.")
elif dia_da_semana == 6:
    vencimento_convertido = vencimento_convertido + timedelta(days=1)
    print(f"Vencimento cai no domingo. Data ajustada automaticamente para {vencimento_convertido.strftime('%d/%m/%Y')}.")
else:
    print(f"Data do vencimento: {vencimento_convertido.strftime('%d/%m/%Y')}")
import datetime

agora = datetime.datetime.now()
data_formatada = agora.strftime("%d/%m/%Y - %H:%M")
print(data_formatada)

hoje = datetime.datetime.now()
prazo_vencimento = hoje + datetime.timedelta(days=30)
print(f"Prazo para pagar a conta: {prazo_vencimento.strftime('%d/%m/%Y')}.")
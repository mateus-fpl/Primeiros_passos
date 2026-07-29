from datetime import datetime
from zoneinfo import ZoneInfo

agora = datetime.now(ZoneInfo("America/Sao_Paulo"))
agora_servidor = agora.astimezone(ZoneInfo("UTC"))

print(f"Data e hora local em São Paulo: {agora.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Data e hora local no servidor : {agora_servidor.strftime('%d/%m/%Y %H:%M:%S')}")
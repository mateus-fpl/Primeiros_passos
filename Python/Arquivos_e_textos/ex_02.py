log = "2026-07-27;ERROR;Falha na conexao com o banco de dados"
log_corte = log.split(';')
data = log_corte [0]
erro = log_corte [1]
falha = log_corte [2]

print(f"[{data}] Nível: {erro} - Mensagem: {falha}")
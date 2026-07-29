porta = "8080"
arquivo = "configuracao.json"

if porta.isdigit() and arquivo.endswith(".json"):
    print("Configuração de servidor válida")
else:
    print("Dados de configuração inválidos")
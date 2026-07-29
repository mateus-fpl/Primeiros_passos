caminho_arquivo = "C:/usuarios/documentos/relatorio_final.csv"

novo_caminho_arquivo = caminho_arquivo.replace("documentos", "projetos")
print(novo_caminho_arquivo)

if ".csv" in novo_caminho_arquivo:
    print(f"Arquivo CSV válido: {novo_caminho_arquivo}")
else:
    print("Formato não suportado.")
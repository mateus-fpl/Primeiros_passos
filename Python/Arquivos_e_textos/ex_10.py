# O Cenário:
# Um sistema legado gerou um arquivo chamado relatorio_bruto.txt com dados de servidores, mas algumas linhas vieram
#  incompletas/corrompidas.

with open("relatorio_bruto", "w", encoding="utf-8") as arquivo:
    arquivo.write("192.168.0.1;8080;ONLINE\n")
    arquivo.write("10.0.0.1;22;OFFLINE\n")
    arquivo.write("172.16.0.5;INVALIDO\n")
    arquivo.write("192.168.1.50;443;ONLINE\n")
    arquivo.write("10.0.0.99;80;ONLINE\n")
servidores_online = []
with open("relatorio_bruto","r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha_ajuste = linha.strip().split(';')
        if (len(linha_ajuste) == 3):
            ip = linha_ajuste[0]
            porta = linha_ajuste[1]
            status = linha_ajuste[2]

            if status == "ONLINE":
                texto_formatado = ":".join([linha_ajuste[0], linha_ajuste[1]])
                servidores_online.append(texto_formatado)

with open("servidores_prontos.txt","w",encoding="UTF-8") as novo_arquivo:
    novo_arquivo.write("\n".join(servidores_online))

with open("servidores_prontos.txt","r",encoding="utf-8") as novo_arquivo:
    for linha in novo_arquivo:
        print(linha)
    


# 1. Criando (ou sobrescrevendo) o arquivo de entrada
with open("lista_ip.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("200.135.80.9\n")
    arquivo.write("192.168.1.1\n")
    arquivo.write("8.35.67.74\n")
    arquivo.write("257.32.4.5\n")
    arquivo.write("85.345.1.2\n")
    arquivo.write("1.2.3.4\n")
    arquivo.write("9.8.234.5\n")
    arquivo.write("192.168.0.256\n")

validos = []
invalidos = []

# 2. Lendo e validando
with open("lista_ip.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        ip_limpo = linha.strip()
        blocos = ip_limpo.split('.')
        
        if len(blocos) == 4:
            ip_valido = True
            for bloco in blocos:
                numero = int(bloco)
                if numero < 0 or numero > 255:
                    ip_valido = False
                    break
            
            if ip_valido:
                validos.append(ip_limpo)
            else:
                invalidos.append(ip_limpo)
        else:
            invalidos.append(ip_limpo)

# 3. Escrevendo o relatório final no arquivo de saída
with open("relatorio.txt", "w", encoding="utf-8") as relatorio:
    relatorio.write("[Endereços válidos:]\n")
    for ip in validos:
        relatorio.write(f"{ip}\n")
        
    relatorio.write("\n[Endereços inválidos:]\n")
    for ip in invalidos:
        relatorio.write(f"{ip}\n")

print("Relatório gerado com sucesso em 'relatorio.txt'!")
with open("servidores.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(" 192.168.0.1:8080 \n")
    arquivo.write(" 10.0.0.1:22 \n")
    arquivo.write(" 172.16.0.5:443 \n")

with open("servidores.txt", "r",encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha_corte = linha.split(":")
        ip = linha_corte[0]
        porta = linha_corte[1]
        print(f"Servidor IP: {ip.strip()} | Porta: {porta.strip()}")
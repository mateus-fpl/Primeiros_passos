
# Abra o arquivo no modo "r".

# Crie duas listas vazias antes do loop: sucessos = [] e falhas = [].

# No loop for:

# Se o status for "SUCCESS", adicione o nome do usuário na lista sucessos.

# Se o status for "FAILED", adicione o nome do usuário na lista falhas.

# No final (fora do loop), imprima as duas listas.

# Saída esperada:

# Python
# Sucessos: ['mateus.paes', 'maria.souza']
# Falhas: ['joao.silva', 'admin']

with open("acessos.log","w",encoding="utf-8") as arquivo:
    arquivo.write("2026-07-29 08:00:00;mateus.paes;SUCCESS\n")
    arquivo.write("2026-07-29 08:05:00;joao.silva;FAILED\n")
    arquivo.write("2026-07-29 08:10:00;maria.souza;SUCCESS\n")
    arquivo.write("2026-07-29 08:15:00;admin;FAILED\n")

sucessos = []
falhas = []
with open("acessos.log","r",encoding="utf-8") as arquivo:
    
    for linha in arquivo:

        linha_corte = linha.strip().split(';')
        nome = linha_corte[1]
        status = linha_corte[2]

        if status == "SUCCESS":
            sucessos.append(nome)
        else:
            falhas.append(nome)

print(f"Sucessos: {sucessos}")
print(f"Falhas: {falhas}")
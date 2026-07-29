# No desenvolvimento backend, é super comum querer guardar registros de acesso ou erros sem apagar o histórico anterior (gerando um arquivo de Log).

# Sua missão:
# Abra o arquivo acessos.log no modo "a" (append).

# Adicione uma nova linha registrando um acesso:
# "2026-07-29 07:00:00;mateus.paes;SUCCESS\n"

# Logo em seguida, abra o arquivo acessos.log no modo "r" (read).

# Percorra o arquivo linha por linha, separando por ponto e vírgula (;), e imprima apenas os acessos que foram um "SUCCESS".

# Acesso confirmado: mateus.paes em 2026-07-29 07:00:00

with open("acessos.log","a",encoding="utf-8") as arquivo:
    arquivo.write("2026-07-29 07:00:00;mateus.paes;SUCCESS\n")
    arquivo.write("2026-07-29 07:00:00;mateus.paes;SUCCESS\n")

with open("acessos.log", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha)
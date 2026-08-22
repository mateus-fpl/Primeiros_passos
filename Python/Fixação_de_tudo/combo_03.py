nivel_risco_limite = int(input("Digite o risco limite dessa zona: "))
abaixo_limite = []
matriz_zonas = [
    ["Shibuya", "Shinjuku", "Roppongi"],
    ["Akihabara", "Ikebukuro", "Ueno"],
    ["Meguro", "Shinagawa", "Ginza"]
]

matriz_energia = [
    [8500, 12000, 3200],
    [1500, 9400, 6000],
    [4100, 2800, 15500]
]

for i in range(len(matriz_energia)):
    for j in range(len(matriz_energia[i])):
        matriz_energia[i][j]

        zona = matriz_zonas[i][j]
        energia = matriz_energia[i][j]

        if energia >= nivel_risco_limite:
            energia_ajustada = energia * 1.2
            print(f"Alerta crítico {zona} - Energia ajustada: {energia_ajustada:.2f}")

        if energia < nivel_risco_limite:
            abaixo_limite.append(energia)
            media = sum(abaixo_limite)/len(abaixo_limite)
        else:
            print("Não há cidades abaixo do limite")
    
print(f"A média de energia das cidades fora do risco limite é {media:.2f}")
print("")

relatorio_feiticeiros = {
    "Satoru Gojo": {"grau": "Especial", "missoes_concluidas": 140, "status": "Ativo"},
    "Megumi Fushiguro": {"grau": "1º Grau", "missoes_concluidas": 35, "status": "Em Missão"},
    "Nobara Kugisaki": {"grau": "3º Grau", "missoes_concluidas": 20, "status": "Inativo"},
    "Yuta Okkotsu": {"grau": "Especial", "missoes_concluidas": 80, "status": "Ativo"}
}

nova_lista = []
buscador = input("Digite um grau de feiticeiro: ")
for feiticeiro in relatorio_feiticeiros:
    if relatorio_feiticeiros[feiticeiro]["grau"] == buscador and relatorio_feiticeiros[feiticeiro]["status"] == "Ativo":
        nova_lista.append(feiticeiro)
    else:
        print("Nenhum grau válido.")

    if relatorio_feiticeiros[feiticeiro]["missoes_concluidas"] >= 50:
        relatorio_feiticeiros[feiticeiro]["veterano"] = True

print("------------ Feiticeiros especiais e ativos ------------")
print(nova_lista)
print("--------- Relatório de Feiticeiros ------------")
print(relatorio_feiticeiros)
print("")
        
print("--------- Horário da Missão ---------")
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

horario_tokyo = datetime.now(ZoneInfo("Asia/Tokyo"))
print(f"Data e horário atual em tokyo: {horario_tokyo.strftime("%d/%m/%Y %H:%M:%S")}")
horario_ny = horario_tokyo.astimezone(ZoneInfo("America/New_York"))
print(f"Data e horário atual em Nova York: {horario_ny.strftime("%d/%m/%Y %H:%M:%S")}")
expiracao_barreira = horario_tokyo + timedelta(hours=18,minutes=30)
print(f"A barreira em Tokyo se expirará em {expiracao_barreira.strftime("%d/%m/%Y %H:%M:%S")}")
print("")

with open ("registro_incidentes.txt","w",encoding="utf-8") as arquivo:
    arquivo.write("Plaintext\n")
    arquivo.write("INC-001;Shibuya;Grau Especial;Pendente\n")
    arquivo.write("INC-002;Shinjuku;1º Grau;Resolvido\n")
    arquivo.write("INC-003;Roppongi;2º Grau;Pendente\n")

linhas_processadas = []
print("--------- Relatório de Incidentes ---------")
with open("registro_incidentes.txt","r",encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha_corte = linha.strip().split(";")
        if len(linha_corte) <4:
            continue
        status = linha_corte[3]

        if status == "Pendente":
            linha_corte[3] = "Em Andamento"

        linhas_processadas.append(";".join(linha_corte))

with open("incidentes_processados.txt", "w", encoding="utf-8") as novo_arquivo:
    for linha in linhas_processadas:
        novo_arquivo.write(linha + "\n")

with open("incidentes_processados.txt", "r", encoding="utf-8") as novo_arquivo:
    for linha in novo_arquivo:
        print(linha)

print("")

class TecnicaAmaldicoada:
    def __init__(self, nome_tecnica, custo_energia):
        self.nome_tecnica = nome_tecnica
        self.custo_energia = custo_energia

class Feiticeiro:
    def __init__(self, nome, quantidade_energia, tecnica):
        self.nome = nome
        self.quantidade_energia = quantidade_energia
        self.tecnica = tecnica

    def usar_expansao_dominio(self):
        if self.quantidade_energia >= self.tecnica.custo_energia:
            self.quantidade_energia = self.quantidade_energia - self.tecnica.custo_energia
            print(f"{self.nome} usou a expansão de domínio {self.tecnica.nome_tecnica}!")
        else:
            print("Energia insuficiente")
print("")

vazio_roxo = TecnicaAmaldicoada("Vazio Roxo", 100)
gojo = Feiticeiro("Gojo", 400,vazio_roxo)
gojo.usar_expansao_dominio()
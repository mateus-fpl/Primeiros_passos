from datetime import datetime, timedelta

while True:
    try:
        limite_perigo = int(input("Por favor, digite o limite do perigo: "))
        if limite_perigo > 0:
            break
        else:
            print("Por favor, digite um número positivo")
            ("")
    except ValueError:
        print("Apenas numeros inteiros são aceitos.")
        print("")
    

cenarios = [
    ["Borda do Abismo", "Floresta da Tentação", "Grande Falha"],
    ["Taça dos Gigantes", "Mar dos Cadáveres", "Capital dos Sem Retorno"],
    ["Vila dos Hollows", "Cidade Dourada", "Ninho das Relíquias"]
]

riscos = [
    [1200, 3500, 6000],
    [8000, 9500, 14000],
    [4000, 18000, 7500]
]

risco_aceitavel = []

print("----------- LUGARES E SEUS RISCOS -----------")

for i in range(len(cenarios)):
    for j in range(len(riscos[i])):

        lugares_abismo = cenarios[i][j]
        nivel_risco = riscos[i][j]

        if nivel_risco >= limite_perigo:
            risco_nivelado = nivel_risco * 1.15
            print(f"ALERTA ABISSAL: {lugares_abismo} - Perigo Ajustado: {risco_nivelado:.2f}")

        if nivel_risco < limite_perigo:
            risco_aceitavel.append(nivel_risco)

if len(risco_aceitavel) > 0:
    media = sum(risco_aceitavel)/len(risco_aceitavel)
    print(f"A média de perigo dos lugares fora do risco no abismo é {media:.2f}")
else:
     print("Não há locais seguros...")

    

print("")

registro_delvers = {
    "Riko": {"apito":"branco","expedições concluídas":5,"status":"ativo"},
    "Reg": {"apito":"nenhum","expedições concluídas":5,"status":"ativo"},
    "Nanachi": {"apito":"nenhum","expedições concluídas":20,"status":"ativo"},
    "Ozen": {"apito":"branco","expedições concluídas":70,"status":"ativo"},
    "Bondrewd": {"apito":"branco","expedições concluídas":90,"status":"ativo"}
    }

print("")

busca = input("Digite a cor de apito: ")

nova_lista = []

for delver in registro_delvers:
    if registro_delvers[delver]["apito"] == busca and registro_delvers[delver]["status"] == "ativo":
        nova_lista.append(delver)
    else:
        print("Nenhum delver encontrado")

    if registro_delvers[delver]["expedições concluídas"] >= 50:
        registro_delvers[delver]["veterano"] = True

print("----------- RELATÓRIO DELVERS EXPERIENTES E ATIVOS -----------")
print(f"Os delvers filtrados foram {nova_lista}")
print("----------- LISTA COMPLETA DOS DELVERS -----------")
print(registro_delvers)
print("")

horario_atual = datetime.now()
fuso_abismo = horario_atual + timedelta(days=2,hours=14,minutes=45)
print("Última janela segura de comunicação\n"f"{fuso_abismo.strftime('%d/%m/%Y %H:%M:%S')}")
print("")

print("------------ RELATÓRIO DE RELÍQUIAS ------------")
with open("reliquias.txt","w",encoding="utf-8") as arquivo:
    arquivo.write("REL-001;Incinerador;Estável\n")
    arquivo.write("REL-002;Cartucho Experimental;Perigoso\n")
    arquivo.write("REL-003;Apito Branco Artificial;Perigoso\n")
    arquivo.write("REL-004;Ovo do Desejo;Estável\n")

linhas_alteradas = []
with open("reliquias.txt","r",encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha_corte = linha.strip().split(";")
        if len(linha_corte) < 3:
            continue
        perigoso = linha_corte[2]

        if perigoso == "Perigoso":
            linha_corte[2] = "Confinado"

        linhas_alteradas.append(";".join(linha_corte))

with open("reliquias_processadas.txt","w",encoding="utf-8") as novo_arquivo:
    for linha in linhas_alteradas:
        novo_arquivo.write(linha + "\n")

with open("reliquias_processadas.txt","r",encoding="utf-8") as novo_arquivo:
    for linha in novo_arquivo:
        print(linha)

print("")


class Reliquia:
    def __init__(self, nome, custo_uso):
        self.nome = nome
        self.ativa = True
        self.custo_uso = custo_uso

    def usar(self):
        pass


class Delver:
    def __init__(self, nome_delver, energia_delver, reliquia):
        self.nome_delver = nome_delver
        self.energia_delver = energia_delver
        self.reliquia = reliquia
        

    def usar_reliquia(self):
        if self.energia_delver >= self.reliquia.custo_uso:
            self.energia_delver = self.energia_delver - self.reliquia.custo_uso
            print(f"Energia atual do(a) {self.nome_delver} está em {self.energia_delver} pontos")
        elif self.energia_delver <=0:
            self.energia_delver = 0
            print(f"Energia zerada")
        else:
            print(f"Energia insuficiente. Energia atual do(a) {self.nome_delver} está em {self.energia_delver} pontos")

objeto_raro = Reliquia("Ovos dourados", 75)
boneco = Delver("Nanachi",300,objeto_raro)
boneco.usar_reliquia()
boneco.usar_reliquia()
boneco.usar_reliquia()
boneco.usar_reliquia()
boneco.usar_reliquia()
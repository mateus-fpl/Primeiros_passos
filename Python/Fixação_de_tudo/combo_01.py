from datetime import datetime, timedelta

grade_cidade = [
    [2, 5, 1],  # Linha 0
    [0, 8, 3],  # Linha 1
    [4, 1, 6]   # Linha 2
]

soma_total = 0

for linha in grade_cidade:
    for implantes in linha:
        soma_total = soma_total + implantes

print(f"A soma de todos os implantes é {soma_total}")
print("")

mercenario = {
            "nome": "V",
            "nivel":15,
            "reputacao":40
            }

mercenario["reputacao"] = mercenario["reputacao"] + 10
mercenario["arma_principal"] = "Katanas"

print("------------ Atributos ------------")
print(f"Mercenario: {mercenario['nome']}.")
print(f"Reputação: {mercenario['reputacao']}.")
print(f"Arma principal: {mercenario['arma_principal']}")
print("")

registro = datetime.now()
conversao = registro.strftime("%d/%m/%Y %H:%M")
seven_days = registro + timedelta(days=7)
conversao_7 = seven_days.strftime("%d/%m/%Y %H:%M")
print(f"Hora atual: {conversao}")
print(f"Prazo para terminar o serviço: {conversao_7}")
print("")

print("-------------- RELATÓRIO DAS MISSÕES --------------")
print("")

with open("log_missoes.txt","w", encoding="utf-8") as arquivo:
    arquivo.write("Roubo do Chip de Biochip\n")
    arquivo.write("Resgate no Distrito de Watson\n")
    arquivo.write("Infiltração na Arasaka\n")

with open("log_missoes.txt","r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())

print("")

# 5. Classe (POO): O Sistema de Cyberware 🦾
# Sua missão:

# Crie uma classe chamada Cibernetico.

# No método __init__, receba e inicialize três atributos:

# nome (string)

# durabilidade (número inteiro, ex: 100)

# ativo (booleano, iniciando como True)

class Cibernetico:
    def __init__(self, nome, durabilidade, ativo):
        self.nome = nome
        self.durabilidade = durabilidade
        self.ativo = True

    def receber_dano(self,dano):
        self.durabilidade = self.durabilidade - dano

        if self.durabilidade <= 0:
            self.durabilidade = 0
            self.ativo = False

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Durabilidade: {self.durabilidade}")
        if self.ativo == False:
            print(f"Status: Faleceu")
        else:
            print(f"Status: Continua na ativa")

print("---------- DADOS --------------")
implante = Cibernetico("Mãos de Gorila", 100, True)
implante.receber_dano(120)
implante.status()
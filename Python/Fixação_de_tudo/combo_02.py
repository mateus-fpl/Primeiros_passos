from datetime import datetime, timedelta

poderes = [
    [1200, 3000, 1500],  # Grupo Raditz, Nappa, Saibaman
    [5000, 1800, 8000],  # Grupo Kuririn, Piccolo, Gohan
    [18000, 24000, 42000] # Grupo Vegeta, Zarbon, Dodoria
]
poder_total = 0

for niveis in poderes:
    for analise in niveis:
        poder_total = poder_total + analise
print("--------- NIVEL DOS GUERREIROS ---------")
print(f"O poder de todos os guerreiros atingiu {poder_total} de ki")
print("")

sayajin ={
    "nome":"Goku",
    "transformacao": "Base",
    "ki":9000
}
sayajin["ki"] = sayajin["ki"] * 50
sayajin["transformacao"] = "Super Sayajin"
sayajin["tecnica_principal"] = "Kamehameha"

print("--------- FICHA GUERREIRO --------")
print(f"Nome: {sayajin['nome']}.")
print(f"Transformação: {sayajin['transformacao']}.")
print(f"Técnica principal: {sayajin['tecnica_principal']}.")
print("")

print("----------- SALA DO TEMPLO -----------")
entrada_goku = datetime.now()
entrada_gohan = datetime.now()
convert_entrada_goku = entrada_goku.strftime("%d/%m/%Y %H:%M:%S")
convert_entrada_gohan = entrada_gohan.strftime("%d/%m/%Y %H:%M:%S")
print (f"Goku entrou na sala do templo às {convert_entrada_goku} e Gohan entrou logo em seguida às {convert_entrada_gohan}.")

saida_goku = entrada_goku + timedelta(hours=24)
convert_goku = saida_goku.strftime("%d/%m/%Y %H:%M:%S")
saida_gohan = entrada_gohan + timedelta(hours=24)
convert_gohan = saida_gohan.strftime("%d/%m/%Y %H:%M:%S")
print(f"Goku tem o limite de deixar a sala do templo até {convert_goku} enquanto Gohan {convert_gohan}.")
print("")

print("------------ LISTA DE DESEJOS ------------")
with open("desejos_shenlong.txt","w",encoding="utf-8") as arquivo:
    arquivo.write("Ressuscitar o Kuririn\n")
    arquivo.write("Restaurar o Planeta Sayajin\n")
    arquivo.write("Imortalidade para o Mestre Kame\n")

with open("desejos_shenlong.txt","r",encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())

print("")


class GuerreiroSayajin:
    def __init__(self, nome, vida): #O que é zenkai?!
        self.nome = nome
        self.vida = vida
        self.zenkai = False

    def receber_ataque(self, dano):
        self.vida = self.vida - dano

        if self.vida <= 0:
            self.vida = 0
            self.zenkai = True

    def status(self):
        if self.zenkai == False:
            print(f"O guerreiro {self.nome} está com {self.vida} de vida. O zenkai está inativo.")
            print("")
        else:
            print(f"O guerreiro {self.nome} está com {self.vida} de vida. O zenkai está ativo") 
            print("")

guerreiro = GuerreiroSayajin("Yamcha", 15)
guerreiro.receber_ataque(200)
guerreiro.status()

guerreiro2 = GuerreiroSayajin("Vegeta", 10000)
guerreiro2.receber_ataque(500)
guerreiro2.status()
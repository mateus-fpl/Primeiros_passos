import random

print("==================================================")
print("              PAINEL DE CLASSES                   ")
print("==================================================")
print("GUERREIRO")
print("  • Vida: 300  | Energia: 100 | Ataque: 40")
print("  • Especial: Golpe Devastador (Dano: 100 | Max Usos: 3)")
print("--------------------------------------------------")
print("ROBÔ")
print("  • Vida: 250  | Energia: 180 | Ataque: 35")
print("  • Especial: Canhão de Plasma (Dano: 100 | Max Usos: 3)")
print("--------------------------------------------------")
print("MAGO")
print("  • Vida: 250  | Energia: 60  | Ataque: 10")
print("  • Especial: Meteoro Arcano (Dano: 100 | Max Usos: 3)")
print("==================================================\n")

print("==================================================")
print("            PAINEL DE COMPANHEIROS                ")
print("==================================================")
print("EMUL")
print("  • Efeito: Recupera +40 HP de todos os heróis")
print("  • Custo: -20 Energia do herói")
print("  • Recarga: 4 rodadas")
print("--------------------------------------------------")
print("CEECRUE")
print("  • Efeito: Aumenta em +20 o Ataque de todos os heróis")
print("  • Custo: -30 Energia do herói")
print("  • Recarga: 4 rodadas")
print("==================================================\n")


class Personagem:
    def __init__(self, nome, vida, energia, ataque):
        self.nome = nome
        self.vida = vida
        self.energia = energia
        self.ataque = ataque

    def atacar(self, alvo):
        alvo.receber_dano(self.ataque)
        print(f"⚔️  [{self.nome}] atacou [{alvo.nome}] e causou {self.ataque} de dano!")

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"💥 [{self.nome}] foi atingido e recebeu {dano} de dano! (HP restante: {max(0, self.vida)})")

    def status(self):
        print(f"📊 [{self.nome}] -> HP: {self.vida} | Energia: {self.energia}")


class Guerreiro(Personagem):
    def __init__(self):
        super().__init__("Guerreiro", 300, 100, 40)
        self.especial = "Golpe Devastador"
        self.usos_especial = 3

    def usar_especial(self, alvo):
        if self.usos_especial > 0:
            print(f"🔥 [{self.nome}] ativou o especial: {self.especial}!")
            alvo.receber_dano(100)
            self.usos_especial -= 1
            print(f"   (Usos restantes do especial: {self.usos_especial})")
        else:
            print(f"⚠️ [{self.nome}] não possui mais usos do especial!")


class Robo(Personagem):
    def __init__(self):
        super().__init__("Robô", 250, 180, 35)
        self.especial = "Canhão de Plasma"
        self.usos_especial = 3

    def usar_especial(self, alvo):
        if self.usos_especial > 0:
            print(f"⚡ [{self.nome}] ativou o especial: {self.especial}!")
            alvo.receber_dano(100)
            self.usos_especial -= 1
            print(f"   (Usos restantes do especial: {self.usos_especial})")
        else:
            print(f"⚠️ [{self.nome}] não possui mais usos do especial!")


class Mago(Personagem):
    def __init__(self):
        super().__init__("Mago", 250, 60, 10)
        self.especial = "Meteoro Arcano"
        self.usos_especial = 3

    def usar_especial(self, alvo):
        if self.usos_especial > 0:
            print(f"☄️ [{self.nome}] ativou o especial: {self.especial}!")
            alvo.receber_dano(100)
            self.usos_especial -= 1
            print(f"   (Usos restantes do especial: {self.usos_especial})")
        else:
            print(f"⚠️ [{self.nome}] não possui mais usos do especial!")


class Companheiro:
    def __init__(self, nome, custo_energia, resguardo):
        self.nome = nome
        self.custo_energia = custo_energia
        self.resguardo = resguardo

    def ajudar(self, alvo):
        pass


class Emul(Companheiro):
    def __init__(self):
        super().__init__("Emul", 20, 40)

    def ajudar(self, alvo):
        alvo.vida += 40
        alvo.energia -= self.custo_energia
        print(f"💚 [{alvo.nome}] recebeu +40 HP do Emul! (Custo: -20 de energia)")


class Ceecrue(Companheiro):
    def __init__(self):
        super().__init__("Ceecrue", 30, 60)

    def ajudar(self, alvo):
        alvo.ataque += 20
        alvo.energia -= self.custo_energia
        print(f"🗡️ [{alvo.nome}] recebeu +20 de ataque de Ceecrue! (Custo: -30 de energia)")


class Monstro:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        alvo.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"🎯 [{self.nome}] foi atingido e recebeu {dano} de dano! (HP do Inimigo: {max(0, self.vida)})")

    def status(self):
        print(f"👾 [{self.nome}] -> HP: {self.vida} | Ataque Base: {self.ataque}")


class Zumbi(Monstro):
    def __init__(self):
        super().__init__("Zumbi Gigante", 2000, 30)

    def usar_habilidade(self, alvo):
        print(f"🧟 [{self.nome}] usou a Horda das Moscas Infernais!")
        alvo.receber_dano(50)


class Alien(Monstro):
    def __init__(self):
        super().__init__("Alien Parasita", 2500, 45)

    def usar_habilidade(self, alvo):
        print(f"👽 [{self.nome}] ativou o Sonar Quântico!")
        alvo.receber_dano(65)


class Fantasma(Monstro):
    def __init__(self):
        super().__init__("Fantasma Egípcio", 3500, 50)

    def usar_habilidade(self, alvo):
        print(f"👻 [{self.nome}] invocou as Bestas do Nilo!")
        alvo.receber_dano(70)


print("==================================================")
print("              REGRAS DA BATALHA                   ")
print("==================================================")
print("• O jogador realiza 3 ações por rodada.")
print("• Ao fim das 3 ações, o monstro realiza seu ataque.")
print("• A cada 3 rodadas, o monstro usa uma habilidade especial de RAGE.")
print("• Vitória: Zerar a vida do monstro.")
print("• Derrota: Todos os heróis serem derrotados.")
print("==================================================\n")

print("==================================================")
print("              OPÇÕES DE COMANDO                   ")
print("==================================================")
print(" 1 - Ataque do Guerreiro   |  2 - Especial do Guerreiro")
print(" 3 - Ataque do Robô        |  4 - Especial do Robô")
print(" 5 - Ataque do Mago        |  6 - Especial do Mago")
print(" 7 - Chamar Emul           |  8 - Chamar Ceecrue")
print(" 9 - Status do Grupo       | 10 - Status do Inimigo")
print("==================================================\n")

inimigos = [Zumbi(), Alien(), Fantasma()]
inimigo_escolhido = random.choice(inimigos)
print(f"⚠️  UM INIMIGO APARECEU: {inimigo_escolhido.nome}! ⚠️\n")

guerreiro = Guerreiro()
robo = Robo()
mago = Mago()
emul = Emul()
ceecrue = Ceecrue()

lista_herois = [guerreiro, robo, mago]
rodada = 0
ultima_vez_emul = -4
ultima_vez_ceecrue = -4
emul_usada = False
ceecrue_usado = False

relatorio_da_batalha = []

while lista_herois and inimigo_escolhido.vida > 0:
    acao = 0

    if guerreiro in lista_herois and guerreiro.vida <= 0:
        guerreiro.vida = 0
        lista_herois.remove(guerreiro)

    if robo in lista_herois and robo.vida <= 0:
        robo.vida = 0
        lista_herois.remove(robo)

    if mago in lista_herois and mago.vida <= 0:
        mago.vida = 0
        lista_herois.remove(mago)

    if not lista_herois:
        break

    print(f"\n--- ⚔️ RODADA {rodada + 1} ⚔️ ---")

    while acao < 3:
        try:
            jogada = int(input(f"Ação {acao + 1}/3 -> Escolha um comando (1-10): "))
            print("")

            if 1 <= jogada <= 10:
                match jogada:
                    case 1:
                        guerreiro.atacar(inimigo_escolhido)
                        acao += 1
                        relatorio_da_batalha.append(f"{guerreiro.nome} atacou {inimigo_escolhido.nome}!")
                        relatorio_da_batalha.append(f"Vida atual do {inimigo_escolhido.nome}: {inimigo_escolhido.vida}")

                    case 2:
                        guerreiro.usar_especial(inimigo_escolhido)
                        acao += 1
                        relatorio_da_batalha.append(f"{guerreiro.nome} usou a habilidade especial em {inimigo_escolhido.nome}!")
                        relatorio_da_batalha.append(f"Vida atual do {inimigo_escolhido.nome}: {inimigo_escolhido.vida}")

                    case 3:
                        robo.atacar(inimigo_escolhido)
                        acao += 1
                        relatorio_da_batalha.append(f"{robo.nome} atacou {inimigo_escolhido.nome}!")
                        relatorio_da_batalha.append(f"Vida atual do {inimigo_escolhido.nome}: {inimigo_escolhido.vida}")

                    case 4:
                        robo.usar_especial(inimigo_escolhido)
                        acao += 1
                        relatorio_da_batalha.append(f"{robo.nome} usou a habilidade especial em {inimigo_escolhido.nome}!")
                        relatorio_da_batalha.append(f"Vida atual do {inimigo_escolhido.nome}: {inimigo_escolhido.vida}")

                    case 5:
                        mago.atacar(inimigo_escolhido)
                        acao += 1
                        relatorio_da_batalha.append(f"{mago.nome} atacou {inimigo_escolhido.nome}!")
                        relatorio_da_batalha.append(f"Vida atual do {inimigo_escolhido.nome}: {inimigo_escolhido.vida}")

                    case 6:
                        mago.usar_especial(inimigo_escolhido)
                        acao += 1
                        relatorio_da_batalha.append(f"{guerreiro.nome} usou a habilidade especial em {inimigo_escolhido.nome}!")
                        relatorio_da_batalha.append(f"Vida atual do {inimigo_escolhido.nome}: {inimigo_escolhido.vida}")

                    case 7:
                        if not emul_usada or (rodada - ultima_vez_emul >= 4):
                            emul_usada = True
                            emul.ajudar(guerreiro)
                            emul.ajudar(robo)
                            emul.ajudar(mago)
                            acao += 1
                            ultima_vez_emul = rodada
                            relatorio_da_batalha.append(f"Emul usou sua habilidade de cura!")
                        else:
                            print("⏳ Emul está em recarga...")

                    case 8:
                        if not ceecrue_usado or (rodada - ultima_vez_ceecrue >= 4):
                            ceecrue_usado = True
                            ceecrue.ajudar(guerreiro)
                            ceecrue.ajudar(robo)
                            ceecrue.ajudar(mago)
                            acao += 1
                            ultima_vez_ceecrue = rodada
                            relatorio_da_batalha.append(f"Ceecrue usou sua habilidade de cura!")
                        else:
                            print("⏳ Ceecrue está em recarga...")

                    case 9:
                        print("--- 🛡️ STATUS DOS HERÓIS ---")
                        guerreiro.status()
                        robo.status()
                        mago.status()
                        print("---------------------------")

                    case 10:
                        print("--- 👾 STATUS DO INIMIGO ---")
                        inimigo_escolhido.status()
                        print("----------------------------")

                print("")
            else:
                print("❌ Digite um número de 1 a 10!")

        except ValueError:
            print("❌ Apenas números inteiros são aceitos!")

    if inimigo_escolhido.vida <= 0:
        break

    rodada += 1
    print("\n--- 👹 TURNO DO INIMIGO ---")

    if rodada % 3 == 0:
        print("🔥 O INIMIGO ENTROU EM RAGE!")
    
        heroi_alvo = random.choice(lista_herois)
        inimigo_escolhido.usar_habilidade(heroi_alvo)
        relatorio_da_batalha.append(f"{inimigo_escolhido.nome} usou habilidade em {heroi_alvo.nome}!")
        relatorio_da_batalha.append(f"Vida atual de {heroi_alvo.nome}: {heroi_alvo.vida}")

    else:
        heroi_alvo = random.choice(lista_herois)
        inimigo_escolhido.atacar(heroi_alvo)
        relatorio_da_batalha.append(f"{inimigo_escolhido.nome} atacou {heroi_alvo.nome}!")
        relatorio_da_batalha.append(f"Vida atual de {heroi_alvo.nome}: {heroi_alvo.vida}")
        

print("\n==================================================")
if inimigo_escolhido.vida <= 0:
    print("🎉 VITÓRIA! O grupo de heróis derrotou o monstro!")
else:
    print("💀 DERROTA! Todos os heróis foram eliminados...")
print("==================================================")
        
with open ("relatorio_da_partida.txt", "w", encoding=("utf-8")) as arquivo:
    for linha in relatorio_da_batalha:
        arquivo.write(f"{linha}\n")

with open ("relatorio_da_partida.txt", "r", encoding=("utf-8")) as arquivo:
    for linha in arquivo:
        print(linha)
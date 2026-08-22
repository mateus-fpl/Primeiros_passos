slayer = {"nome":"Tanjiro", "vida":150,}

def treino(alvo, dano):
    alvo["vida"] = alvo["vida"] - dano
    print(f"{alvo['nome']} foi atingido! Vida atual: {alvo['vida']}")

treino(slayer, 15)

class Cacador:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def respiracao_do_javali(self, alvo):
        alvo.vida = alvo.vida - 20
        print(f"{self.nome} atacou {alvo.nome}")
        print(f"Vida atual do {alvo.nome}: {alvo.vida}")

javali = Cacador("Inosuke", 200)
oni = Cacador("Rui", 300)
javali.respiracao_do_javali(oni)
javali.respiracao_do_javali(oni)
javali.respiracao_do_javali(oni)
javali.respiracao_do_javali(oni)
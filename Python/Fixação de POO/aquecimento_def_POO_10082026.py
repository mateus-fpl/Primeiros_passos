Luffy = {"nome": "Luffy",
         "vida": 100}

def golpe_do_kaido(alvo, dano):
    alvo["vida"] = alvo["vida"] - dano
    print(f"O {alvo['nome']} foi atingido! Vida restante: {alvo['vida']}.")

golpe_do_kaido(Luffy, 20)
golpe_do_kaido(Luffy, 30)


class Pirata:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self, alvo):
        alvo.vida = alvo.vida - 20
        print(f"{self.nome} atacou {alvo.nome}")
        print(f"Vida atual do {alvo.nome}: {alvo.vida}")

zoro = Pirata("Zoro", 100)
mihawk = Pirata("Mihawk", 200)
zoro.atacar(mihawk)
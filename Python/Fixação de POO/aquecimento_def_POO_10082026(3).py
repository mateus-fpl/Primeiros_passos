sasuke = {
    "nome": "Sasuke",
    "vida": 120
}

def rasengan(alvo, dano):
    alvo["vida"] = alvo["vida"] - dano
    print(f"{alvo['nome']} foi atingido! Nível de vida atual: {alvo['vida']}")

rasengan(sasuke, 30)
rasengan(sasuke, 20)

class Ninja:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def chidori(self, alvo, dano):
        alvo.vida = alvo.vida - dano
        print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano")
        print(f"{alvo.nome} foi atingido e está com {alvo.vida} de vida")

kakashi = Ninja("Kakashi", 150)
zabuza = Ninja("Zabuza", 180)
kakashi.chidori(zabuza,50)

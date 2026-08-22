class Cacador:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def golpe_nen(self, alvo):
        dano = self.forca - alvo.armadura
        alvo.vida = alvo.vida - dano
        if alvo.vida < 0:
            alvo.vida = 0
            print(f"{self.nome} atacou {alvo.nome} e causou um dano de {dano} HP.")
            print(f"{alvo.nome} morreu")
        else:
            print(f"Vida restante de {alvo.nome}: {alvo.vida} HP")

    def jajanken(self, alvo):
        dano = self.forca
        alvo.vida = alvo.vida - dano

        print("Saichou...")
        print("")
        print("")
        print(f"Jan...")
        print(f"")
        print(f"ken...")
        print("")
        print(f"POOOOOOOOOOOOOOOO!!!!!!!!")
        print("")
        if alvo.vida < 0:
            alvo.vida = 0
            print(f"{self.nome} atacou {alvo.nome} e causou um dano de {dano} HP.")
            print(f"{alvo.nome} morreu")
        else:
            print(f"Vida restante de {alvo.nome}: {alvo.vida} HP")

    def fugir(self):
        print(f"{self.nome} fugiu!")

    def treinar(self):
        print(f"{self.nome} foi treinar que nem um desgraçado pra se vingar!")

    def voltar(self):
        print(f"{self.nome} está pronto para lutar de novo!")

    def boost(self):
        self.vida = self.vida * 5
        self.forca = self.forca * 100


class ChimeraAnt:
    def __init__(self, nome, vida, armadura):
        self.nome = nome
        self.vida = vida
        self.armadura = armadura

    def atacar_com_garras(self, alvo):
        dano = self.vida / 10
        alvo.vida = alvo.vida - dano
        if alvo.vida < 0:
            alvo.vida = 0
            print(f"{self.nome} atacou {alvo.nome} e causou um dano de {dano} HP.")
            print(f"{alvo.nome} morreu")
        else:
            print(f"Vida restante de {alvo.nome}: {alvo.vida} HP")


    
kaito = Cacador("Kaito", 200, 150)
pitou = ChimeraAnt("Neferpitou", 500, 60)
pitou.atacar_com_garras(kaito)
pitou.atacar_com_garras(kaito)
pitou.atacar_com_garras(kaito)
pitou.atacar_com_garras(kaito)
pitou.atacar_com_garras(kaito)

gon = Cacador("Gon", 100, 50)
gon.fugir()
gon.treinar()
gon.voltar()
gon.golpe_nen(pitou)
pitou.atacar_com_garras(gon)
gon.boost()
pitou.atacar_com_garras(gon)
pitou.atacar_com_garras(gon)
gon.jajanken(pitou)


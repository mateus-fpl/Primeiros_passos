class Personagem:
    def __init__(self, nome, vidas):
        self.nome = nome
        self.vidas = vidas

    def perder_vida(self):
        self.vidas = self.vidas - 1
        print(f"{self.nome} levou dano e agora tem {self.vidas} vidas!")

class Mario(Personagem):
    def usar_flor_de_fogo(self):
        print(f"{self.nome} comeu a Flor de Fogo e agora está atirando bolas de fogo! 🔥")

class Luigi(Personagem):
    def usar_super_pulo(self):
        print(f"{self.nome} pegou impulso e deu aquele pulo super alto flutuando no ar! 🚀")

player1 = Mario("Mario",3)
player1.perder_vida()
player1.perder_vida()
player1.usar_flor_de_fogo()

player2 = Luigi("Luigi",4)
player2.perder_vida()
player2.usar_super_pulo()
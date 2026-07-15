#Objetivo: criar um sistema de batalha de algum dos protagonistas da Frieren contra algum demônio.

class Heroi:
    def __init__(self, nome, classe, mana):
        self.nome = nome
        self.classe = classe
        self.mana = mana

    def acao(self, dano_causado, alvo_demonio, custo_mana):
        self.dano_causado = dano_causado
        self.alvo_demonio = alvo_demonio
        self.custo_mana = custo_mana
        # Altera o poder do demônio usando o dano causado pelo herói
        self.alvo_demonio.poder = alvo_demonio.poder - dano_causado

class Demonio:
    def __init__(self, especie, tipo, poder):
        self.especie = especie
        self.tipo = tipo
        self.poder = poder

    def atitude(self, dano_causado, alvo_heroi, custo_poder):
        self.dano_causado = dano_causado
        self.alvo_heroi = alvo_heroi
        self.custo_poder = custo_poder
        # Altera a mana do herói usando o dano causado pelo demônio
        self.alvo_heroi.mana = alvo_heroi.mana - dano_causado

# Criação dos personagens
mocinho = Heroi("Stark", "Guerreiro", 500)
vilao = Demonio("Malek", "Demonio", 2000)

while mocinho.mana > 0 and vilao.poder > 0:
    mocinho.acao(150, vilao, 20)
    vilao.atitude(30, mocinho, 340)

    print(f"{mocinho.nome}: {mocinho.mana} de Mana |||| {vilao.especie}: {vilao.poder} de Poder")

# Verificação do vencedor
if mocinho.mana <= 0:
    print(f"{mocinho.nome} derrotado!")
else:
    print(f"{vilao.especie} derrotado!")
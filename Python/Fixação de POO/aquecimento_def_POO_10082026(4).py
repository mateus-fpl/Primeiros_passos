luffy = {"nome":"Luffy", "vida": 100}
zoro = {"nome":"Zoro", "vida": 100}
sanji = {"nome":"Sanji", "vida": 100}

def ataque_em_area(alvo1, alvo2, alvo3, dano):
    alvo1['vida'] = alvo1['vida'] - dano
    alvo2['vida'] = alvo2['vida'] - dano
    alvo3['vida'] = alvo3['vida'] - dano

    print(f"{alvo1['nome']} foi atingido e sua vida está em {alvo1['vida']} HP")
    print(f"{alvo2['nome']} foi atingido e sua vida está em {alvo2['vida']} HP")
    print(f"{alvo3['nome']} foi atingido e sua vida está em {alvo3['vida']} HP")

ataque_em_area(luffy,zoro, sanji, 15)
ataque_em_area(luffy,zoro, sanji, 10)

# Exercício 2: Classe (class)
# (Goku x Vegeta com Ataque Normal e Especial)
# Crie uma classe chamada Saiyajin que receba nome, ki e energia_especial no __init__.
# Crie um método chamado soco que receba o alvo:
# Tira 20 pontos do ki do alvo.
# Imprime quem atacou e o ki restante do alvo.

# Crie um método chamado especial que receba o alvo:
# Tira do ki do alvo o valor de 20 + self.energia_especial
#  (ou seja, o dano base mais o bônus de energia especial do atacante!).
# Imprime o nome do golpe especial, quem usou e a vida restante do alvo.
# Crie duas instâncias: goku (ki 200, energia_especial 50) e vegeta (ki 200, energia_especial 40).
# Faça o goku dar um soco no vegeta.
# Faça o vegeta mandar o especial no goku.

class Sayajin:
    def __init__(self, nome, ki, energia_especial):
        self.nome = nome
        self.ki = ki
        self.energia_especial = energia_especial

    def ataque(self,alvo):
        alvo.ki = alvo.ki - 20
        print(f"{alvo.nome} foi atingido com um ataque e perdeu 20 HP.")
        print(f"{alvo.nome} está com {alvo.ki} de HP.")

    def ataque_especial(self, alvo):
        alvo.ki = alvo.ki - 20 - self.energia_especial
        print(f"{alvo.nome} foi atingido com um ataque especial e está com {alvo.ki} de HP.")

goku = Sayajin("Goku", 200, 50)
vegeta = Sayajin("Vegeta", 200, 45)

goku.ataque(vegeta)
vegeta.ataque(goku)
vegeta.ataque(goku)
goku.ataque(vegeta)
vegeta.ataque(goku)
goku.ataque_especial(vegeta)



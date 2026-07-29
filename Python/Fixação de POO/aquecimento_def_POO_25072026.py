def elevar_cosmos():
    nome = input("Digite o nome do seu cavaleiro: ")
    nivel_atual = float(input("Digite o nível do seu cavaleiro: "))
    setimo_sentido = float(input("Coloque quantas vezes o cosmo aumentou: "))
    nivel_atual = nivel_atual * setimo_sentido

    if nivel_atual <= 50:
        print(f"O cavaleiro {nome} aumento seu poder em {setimo_sentido} vezes e está com o cosmo em {nivel_atual}. Ele é um cavaleiro de bronze!")
    elif nivel_atual <= 120:
        print(f"O cavaleiro {nome} aumento seu poder em {setimo_sentido} vezes e está com o cosmo em {nivel_atual}. Ele é um cavaleiro de prata!")
    elif nivel_atual <= 450:
        print(f"O cavaleiro {nome} aumento seu poder em {setimo_sentido} vezes e está com o cosmo em {nivel_atual}. Ele é um cavaleiro de ouro!")
    else:
        print(f"O cavaleiro {nome} aumento seu poder em {setimo_sentido}  vezese está com o cosmo em {nivel_atual}. Ele é um cavaleiro divino!")

    return nome, setimo_sentido, nivel_atual

cavaleiro1 = elevar_cosmos()

class Cavaleiro:
    def __init__(self, nome, constelacao, categoria, cosmos):
        self.nome = nome
        self.constelacao = constelacao
        self.categoria = categoria
        self.cosmos = cosmos

    def golpe(self, nome_do_golpe):
        self.nome_do_golpe = nome_do_golpe
        print(f"{self.nome} da constelação de {self.constelacao}, {self.categoria}, disparou o {nome_do_golpe}.")

    def treinar_horas(self,horas):
        self.horas = horas
        for i in range (horas):
            self.cosmos = self.cosmos + 50

        print(f"{self.nome} treinou por {horas} e seu cosmo está com {self.cosmos} de nível.")

guerreiro1 = Cavaleiro("Yoga", "Cisne", "bronze", 50)
guerreiro1.golpe("Execução Aurora!")
guerreiro1.treinar_horas(4)


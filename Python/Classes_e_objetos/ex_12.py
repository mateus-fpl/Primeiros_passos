# 🔮 Classe Mago
# Atributos:
# nome (str)
# mana (int)
# grimorios (list) -> Inicializa vazia []
# Métodos:
# __init__(self, nome, mana): Inicializa os atributos.
# estudar_grimorio(self, nova_magia): Adiciona a magia na lista grimorios.
# lancar_magia(self, nome_magia, custo):
# Se não conhece a magia -> Retorna "Magia desconhecida!"
# Se conhece, mas não tem mana -> Retorna "Mana insuficiente!"
# Se conhece e tem mana -> Subtrai o custo da mana e retorna o sucesso do feitiço.

class Mago:
    def __init__(self, nome, mana):
        self.nome = nome
        self.mana = mana
        self.grimorio = []

    def estudar_grimorio(self, nova_magia):
        self.nova_magia = nova_magia
        self.grimorio.append(nova_magia)
        print(f"{self.nome} aprendeu a magia {nova_magia}!")

    def lancar_magia(self, nome_magia,custo):
        
        if nome_magia in self.grimorio:
            if custo > self.mana:
                print("Magia insuficiente!")
            else:
                self.mana = self.mana - custo
        else:
            print("Magia desconhecida, impossível utilizar")

feiticeiro = Mago("Frieren", 100000)
feiticeiro.estudar_grimorio("Magia de raios")
feiticeiro.estudar_grimorio("Zootrak")
combate = feiticeiro.lancar_magia("Zootrak", 700)
combate = feiticeiro.lancar_magia("Espinhos rochosos", 500)


print(f"O(a) mago(a) {feiticeiro.nome} tem {feiticeiro.mana} de mana.")
print(f"O(a) mago(a) {feiticeiro.nome} adquiriu a {feiticeiro.grimorio[-1]}. Seu grimório atual é {feiticeiro.grimorio}")
print(f"O(a) mago(a) {feiticeiro.nome} lançou {feiticeiro.grimorio[-2]} e está com {feiticeiro.mana} pontos de mana")
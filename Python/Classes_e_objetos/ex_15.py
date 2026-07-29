class Cacador:
    def __init__(self, nome, classe, ouro):
        self.nome = nome
        self.classe = classe
        self.ouro = ouro
        self.inventario = []

    def adquirir_item(self, nome_item, custo):
        if self.ouro >= custo:
            self.inventario.append(nome_item)
            self.ouro = self.ouro - custo
        else:
            print("Tá sem grana! Fez aula com a Frieren?!")

    def exibir_ficha(self):
        print("----------- Ficha do Personagem -----------")
        print(f"O personagem {self.nome} da classe {self.classe} possui {self.ouro} de ouro disponível.")
        print(f"Items em sua mochilha: {self.inventario}")
        print("")

personagem = Cacador("sung_jinwoo", "Assassino", 100)
personagem.adquirir_item("Espada de Chamas", 80)
personagem.adquirir_item("Poção de Cura", 50)
personagem.exibir_ficha()

personagem2 = Cacador("Killua", "Assassino", 500)
personagem2.adquirir_item("Iôiô", 100)
personagem2.adquirir_item("Skate", 100)
personagem2.adquirir_item("Ilha da Cobiça", 250)
personagem2.exibir_ficha()
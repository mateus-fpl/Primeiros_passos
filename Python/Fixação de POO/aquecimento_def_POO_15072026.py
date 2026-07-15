def clone_das_sombras(ninja, quantidade):
    total = (ninja +  " ") * quantidade
    return total

genin = input("Digite o nome do ninja: ")
clones = int(input("Digite a quantidade de clones: "))
ninjas_extras = clone_das_sombras(genin, clones)
print(f"No meio da luta apareceu {ninjas_extras}.")

class Ninja:
    def __init__(self, nome, vila, chackra, nome_do_jutsu):
        self.nome = nome
        self.vila = vila
        self.chackra = chackra
        self.nome_do_jutsu = nome_do_jutsu

    def usar_jutsu(self, custo):
        self.chackra = self.chackra - custo
        

boneco = Ninja("Rock Lee", "Vila da folha", 1000, "Chute furação da folha")
boneco.usar_jutsu(120)

print(f"O {boneco.nome} veio da {boneco.vila}. Com seu {boneco.nome_do_jutsu} ficou com {boneco.chackra} de chackra")


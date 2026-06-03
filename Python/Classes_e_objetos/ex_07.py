class Tamagoshi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def AlteraNome (self, novo_nome):
        self.nome = novo_nome

    def NivelFome (self, quanta_fome):
        self.fome = quanta_fome

    def NovaIdade (self, idade_atual):
        self.idade = idade_atual



nome_bichinho = input("Digite o nome do seu monstrinho: ")
fome_bichinho = input("Quão faminto tá esse monstrinho: ")
saude_bichinho = input("Como tá a condição desse monstrinho: ")
idade_bichinho = input("Qual a idade desse monstrinho: ")

bichinho_virtual = Tamagoshi(nome_bichinho, fome_bichinho, saude_bichinho, idade_bichinho)

print(f"A criaturinha se chama {bichinho_virtual.nome}, está {bichinho_virtual.fome}, a saúde tá {bichinho_virtual.saude} e está com {bichinho_virtual.idade} meses de idade.")
class pessoa :
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def engordar(self,quilos):
        self.peso = self.peso + quilos
        return self.peso

    def emagrecer(self,quilos):
        self.peso = self.peso - quilos
        return self.peso
    
homem = pessoa("Mateus", 33, 90)
print(f"O homem se chama {homem.nome}, tem {homem.idade} ano e pesa {homem.peso} quilos.")

homem.engordar(10)
print(f"O Homem engordou e agora pesa {homem.peso} quilos.")

homem.emagrecer(5)
print(f"O homem emagreceu e agora pesa {homem.peso} quilos.")

    

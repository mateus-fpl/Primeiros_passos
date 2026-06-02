class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade <=20:
            self.altura += 0.5
        return self.idade

    def engordar(self):
        self.peso += 1
        return self.peso

    def emagrecer(self):
        self.peso -= 1
        return self.peso
    
nome1 = input("Digite seu nome: ")
idade1 = int(input("Digite sua idade: "))
peso1 = float(input("Digite seu peso: "))
altura1 = float(input("Digite sua altura: "))


    
pessoa1 = pessoa(nome1, idade1, peso1, altura1)
pessoa1.engordar()
pessoa1.engordar()
pessoa1.engordar()
pessoa1.envelhecer()

print(f"A pessoa se chama {pessoa1.nome}, tem {pessoa1.idade} anos, pesa {pessoa1.peso} kg e sua altura é {pessoa1.altura} cm.")


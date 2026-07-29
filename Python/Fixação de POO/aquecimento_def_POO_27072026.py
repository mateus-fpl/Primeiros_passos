def calcular_fumaca(nome,quantidade_mg):
    if quantidade_mg >= 500:
        return f"{nome} é um feiticeiro de elite!"
    else:
        return f"{nome} é um feiticeiro comum!"

jacare = print(calcular_fumaca("Shin", 600))

class MembroFamiliaEn:
    def __init__(self, nome, mascara):
        self.nome = nome
        self.mascara = mascara

    def apresentar(self):
        print(f"Eu sou {self.nome} e uso uma máscara de {self.mascara}")

boneco = MembroFamiliaEn("Adailton", "Tamanduá-bandeira")
boneco.apresentar()
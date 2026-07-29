class Veiculo:
    def __init__(self, piloto, velocidade_maxima):
        self.piloto = piloto
        self.velocidade_maxima = velocidade_maxima

    def acelerar(self):
            print(f"{self.piloto} está acelerando a {self.velocidade_maxima} Km/h!")

class KartStandard(Veiculo):
     def __init__(self, piloto, velocidade_maxima, moedas):
          super().__init__(piloto, velocidade_maxima)
          self.moedas = moedas

     def coletar_moedas(self):
        if self.moedas >= 10:
            print(f"{self.piloto} atingiu o máximo de moedas. Quantidade: {self.moedas}.")
        else:
             self.moedas = self.moedas + 1
             print(f"{self.piloto} coletou uma moeda. Quantidade: {self.moedas}")
             self.velocidade_maxima = self.velocidade_maxima + 2
             print(f"{self.piloto} ganhou +2 de velocidade. Velocidade atual {self.velocidade_maxima} Km/h.")     
class MotoSuper(Veiculo):
    def __init__(self, piloto, velocidade_maxima,turbo_nivel):
        super().__init__(piloto, velocidade_maxima)
        self.turbo_nivel = turbo_nivel

    def soltar_drift(self):
         if self.turbo_nivel == "roxo":
              print(f"{self.piloto} soltou o Ultra Mini-Turbo ROXO!")

boneco1 = KartStandard("Toad",50,5)
boneco1.coletar_moedas()
boneco1.coletar_moedas() 
boneco1 = MotoSuper("Toad",boneco1.velocidade_maxima,"roxo") 
boneco1.soltar_drift()

class carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self):
        self.velocidade = self.velocidade +10

    def frear(self):
        self.velocidade = self.velocidade -10

calhambeque = carro("Gol")
calhambeque.acelerar()
calhambeque.acelerar()
calhambeque.acelerar()
calhambeque.acelerar()
calhambeque.acelerar()

print(f"O modelo do carro é {calhambeque.modelo} e está correndo com a {calhambeque.velocidade} km/h")


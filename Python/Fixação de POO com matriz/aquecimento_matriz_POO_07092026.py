class Veiculo:
    def __init__(self, modelo, combustivel):
        self.modelo = modelo
        self.combustivel = combustivel

    def rodar(self,distancia):
        self.combustivel = self.combustivel - distancia

        if self.combustivel <= 0:
            self.combustivel = 0
            self.status = "Sem Combustivel"
            print(f"Sem combustível no {self.modelo}! Chame o Pica-Pau doidão.")
        else:
            print(f"{self.modelo} - Combustivel atual: {self.combustivel}")

frota = []

for i in range(2):
    linha = []
    for j in range(2):
        carro = input("Digite o modelo do carro: ")
        while True:
            try:
                tanque = float(input("Digite a quantidade de combustível:"))
                if tanque > 0:
                    break
                else:
                    print("Impossível!")
                    print("")
            except ValueError:
                print("Digite um valor válido!")
                print("")
        cars = Veiculo(carro,tanque)
        linha.append(cars)
    frota.append(linha)

for linha in frota:
    for unidade in linha:
        print(f"Carro: {unidade.modelo} | Tanque: {unidade.combustivel}", end="")
    print()

carro_escolhido = frota[0][0].rodar(30)
    
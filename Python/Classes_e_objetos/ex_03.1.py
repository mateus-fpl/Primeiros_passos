class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_dinheiro):
        litros_abastecidos = valor_dinheiro / self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        
        return litros_abastecidos

    def abastecer_por_litros(self, quantidade_litros):
        valor_pagar = quantidade_litros * self.valor_litro
        self.quantidade_combustivel -= quantidade_litros
        
        return valor_pagar

    def encher_bomba(self, quantidade):
        self.quantidade_combustivel += quantidade

bomba = BombaCombustivel("Gasolina", 5.80, 1000)

litros = bomba.abastecer_por_valor(100)

print(f"Foram colocados {litros:.2f} litros no carro.")
print(f"Restam {bomba.quantidade_combustivel:.2f} litros na bomba do posto.")
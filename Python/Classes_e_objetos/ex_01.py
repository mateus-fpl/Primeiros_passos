class tipos_de_bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor):
        self.cor = nova_cor
    
    def mostra_cor(self):
        return self.cor

bola = tipos_de_bola("azul", "20 cm", "borracha")
print(f"A cor da bola é {bola.cor}, sua circunferência é de {bola.circunferencia} e é feita de {bola.material}.")

bola.troca_cor("Verde")
cor_atual = bola.mostra_cor()

print(f"A nova cor da bola é: {cor_atual}")




def subir_camada(numero_da_camada):

    match numero_da_camada:
        case 1:
            print("Tontura leve e náuseas.")
        case 2:
            print("Dor de cabeça intensa, dormência nos membros e vômito.")
        case 3:
            print("Alucinações visuais e auditivas, além de perda de equilíbrio.")
        case 4:
            print("Dor intensa em todo o corpo e sangramento pelos poros.")
        case 5:
            print("Perda de todos os sentidos e confusão mental extrema.")
        case _:
            print("Perda da humanidade ou morte imediata!")

descida = int(input("Digite o número da camada que você pretende ir: ")) 
abismo = subir_camada(descida)

class Explorador:
    def __init__(self, nome, cor_apito, profundidade_maxima):
        self.nome = nome
        self.cor_apito = cor_apito
        self.profundidade_maxima = profundidade_maxima

    def promover_apito(self, nova_cor):
        self.cor_apito = nova_cor

personagem = Explorador("Riko", "vermelho", 500)
print(f"A {personagem.nome} desceu {personagem.profundidade_maxima} metros usando seu apito {personagem.cor_apito}")
personagem.promover_apito("Alvo")
print(f"A {personagem.nome} está com o apito {personagem.cor_apito}")


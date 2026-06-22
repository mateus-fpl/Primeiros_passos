# Possua uma classe chamada Ponto, com os atributos x e y.
# Possua uma classe chamada Retangulo, com os atributos largura e altura.
# Possua uma função para imprimir os valores da classe Ponto
# Possua uma função para encontrar o centro de um Retângulo.
# Você deve criar alguns objetos da classe Retangulo.
# Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
# A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
# O valor do centro do objeto deve ser mostrado na tela
# Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordenadas(self):
        print(f"O valor de x é: {self.x}")
        print(f"O valor de y é: {self.y}")

class retangulo:
    def __init__(self, altura, largura, ponto_partida):
        self.altura = altura
        self.largura = largura
        self.ponto_partida = ponto_partida

    def vertice_retangulo(self):
        x_centro = self.ponto_partida.x + (self.largura/2)
        y_centro = self.ponto_partida.y + (self.altura/2)

        centro_da_caixa = ponto(x_centro,y_centro)

        return centro_da_caixa
    
    def mudar_retangulo(self):
        self.altura = float(input("Digite a nova altura do retângulo: "))
        self.largura = float(input("Digite a nova largura do retângulo: "))
    
ponto_x = float(input("Digite o valor de X: "))
ponto_y = float(input("Digite o valor de Y: "))

calculo_pontos = ponto(ponto_x,ponto_y)


altura_retangulo = float(input("Digite a altura do retângulo: "))
largura_retangulo = float(input("Digite a largura do retângulo: "))

meu_retangulo = retangulo(altura_retangulo, largura_retangulo, calculo_pontos)

opcao = 0

while opcao != 3:
    print("1 - Mudar tamanho do retângulo")
    print("2 - Ver o centro atual")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Digite os novos valores de altura e largura:")

        meu_retangulo.mudar_retangulo()
        print("Medidas alteradas com sucesso!")
        
    elif opcao == 2:
        centro_atual = meu_retangulo.vertice_retangulo()
        centro_atual.coordenadas()

    elif opcao == 3:
        print("Programa encerrado.")
    else:
        print("Opção inválida. Por favor digite 1, 2 ou 3.")
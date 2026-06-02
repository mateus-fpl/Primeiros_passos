class smartphone:
    def __init__(self, modelo, bateria, ligado):
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.ligado == False:
            self.ligado = True
            print("O celular está ligado!")
        else:
            self.ligado = False
            print("O celular está desligado!")

    def fazer_chamada(self, duracao_minutos):
        if self.ligado == True:
            gasto = duracao_minutos * 2
            self.bateria -= gasto

            if self.bateria <= 0:
                self.bateria = 0
                self.ligado = False
                print("Bateria acabou. Celular desligado")
            else:
                print(f"Chamada de {duracao_minutos} feita com sucesso.")
        else:
            print("Não dá pra fazer chamada. O celular está desligado!")
    
    def carregar(self, quantidade):
        if self.ligado == True:
            self.bateria += quantidade
        
        if self.bateria >= 100:
            self.bateria = 100
            print("Celular carregado.")
        else:
            print(f"O celular está com {self.bateria}% de bateria.")

modelo1 = input("Digite o modelo do seu celular: ")
bateria1 = int(input("Digite quantidade de bateria do seu celular: "))

celular1 = smartphone(modelo1, bateria1, True)
celular1.ligar()
celular1.fazer_chamada(5)

print(f"O celular é da marcar {celular1.modelo} e está com {celular1.bateria}% de bateria")


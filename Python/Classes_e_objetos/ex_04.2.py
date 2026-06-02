class ArCondicionado:
    def __init__(self,temperatura, ligado):
        self.temperatura = temperatura
        self.ligado = False

    def ligar_desligar(self):
        if self.ligado == False:
           self.ligado = True
           print("Ar-condicionado ligado")
        else:
            self.ligado = False
            print("Ar-condicionado desligado")

    def aumentar_temperatura(self):
        if self.ligado == True:
            self.temperatura += 1
            

        if self.temperatura >=30:
            print("Quer morar no inferno, maluco?!")

    def diminuir_temperatura(self):
        if self.ligado == True:
            self.temperatura -= 1

        if self.temperatura <= 15:
            print("Quer morar no gelo, ô pinguim?!")

arzim = int(input("Manda a temperatura aí, meu patrão: "))

ar_condicionado = ArCondicionado(arzim, True)
ar_condicionado.ligar_desligar()
ar_condicionado.aumentar_temperatura()
print (f"A temperatura do ar-condicionado está em {ar_condicionado.temperatura}ºC.")


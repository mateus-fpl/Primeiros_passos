class SomCarro:
    def __init__(self):
        self.volume = 10
        self.ligado = False

    def ligar_desligar(self):
        if self.ligado == False:
            self.ligado = True
            print("Som ligado!")
        else:
            self.ligado = False
            print("Som desligado!")

    def aumentar_volume(self):
        if self.ligado == True:
            self.volume += 2

        if self.volume >= 30:
            print("Tá surdo, mano?!")

    def diminuir_volume(self):
        if self.ligado == True:
            self.volume -= 2
               
        if self.volume <=0:
            print("O som está no mudo. Quer ouvir por língua de sinais?")

meu_som = SomCarro()
meu_som.ligar_desligar()
meu_som.aumentar_volume()
meu_som.aumentar_volume()
print(f"O volume do rádio está em {meu_som.volume}")
    
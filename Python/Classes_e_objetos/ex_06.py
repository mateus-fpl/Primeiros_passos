# Faça um programa que simule um televisor criando-o como um objeto. 
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class televisor:
    def __init__(self, canal, volume, ligado):
        self.canal = canal
        self.volume = volume
        self.ligado = False

    def ligar_desligar(self):
        if self.ligado == False:
            self.ligado = True
            print("TV ligada")
        else:
            self.ligado = False
            print("TV desligada")
    
    def AumentarCanal (self):
        if self.ligado == True:
            self.canal += 1

            if self.canal > 13:
                self.canal = 2

    def DiminuirCanal (self):
        if self.ligado == True:
            self.canal -= 1

            if self.canal < 2:
                self.canal = 13

    def AumentarVolume (self):
        if self.ligado == True:
            self.volume += 5

        if self.volume >= 50:
            self.volume = 50
            print("Já tá no talo!")

    def DiminuirVolume (self):
        if self.ligado == True:
            self.volume -= 5
        
        if self.volume <= 0:
            self.volume = 0
            print("Aumenta um pouco que aqui não tem libras não.")

emissora = int(input("Digite um canal para assistir: "))
audio = int(input("Escolha o volume: "))

tv = televisor(emissora, audio, True)
tv.ligar_desligar()
tv.AumentarCanal()
tv.AumentarCanal()
tv.AumentarVolume()

print(f"A TV está no canal {tv.canal} no volume {tv.volume}.")
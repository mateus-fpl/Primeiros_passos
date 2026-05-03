class televisor:
    def __init__(self,canal, volume):
        self.canal = canal
        self.volume = volume

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

    def aumentar_volume(self):
        self.volume = self.volume +1
    
    def diminuir_volume(self):
        self.volume = self.volume -1

emissora = televisor(5, 9)
print (f"A TV está no canal {emissora.canal} com {emissora.volume} de volume")

emissora.mudar_canal(7)
emissora.aumentar_volume()
print (f"A TV está no canal {emissora.canal} com {emissora.volume} de volume")

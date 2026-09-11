class Server:
    def __init__(self, nome, memoria_ram):
        self.nome = nome
        self.memoria_ram = memoria_ram
        self.status = "Online"

    def consumir_memoria(self, quantidade):
        self.memoria_ram = self.memoria_ram - quantidade
    
        if self.memoria_ram <= 0:
            self.memoria_ram = 0              
            self.status = "Offline"
        
        print(f"RAM atual: {self.memoria_ram}")
        print(f"Status atual: {self.status}")


cluster = []

for i in range (2):
    linha = []
    for j in range (2):
        servidor = input(f'Cadastre o nome do servidor: ')
        ram = int(input(f"A memória RAM do servidor: "))
        s = Server(servidor,ram)
        linha.append(s)
    cluster.append(linha)
        
for linha in cluster:
    for elemento in linha:
        print(f"{elemento.nome} | RAM: {elemento.memoria_ram} | Status: {elemento.status}\t", end="")
    print()

servidor_algo = cluster[0][0].consumir_memoria(100)
servidor_algo = cluster[0][0].consumir_memoria(100)
servidor_algo = cluster[0][0].consumir_memoria(100)


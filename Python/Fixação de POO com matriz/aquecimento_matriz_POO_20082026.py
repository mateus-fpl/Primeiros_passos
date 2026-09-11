matriz = []

for i in range (3):
    linha = []
    for j in range (3):
        linha.append(0)
    matriz.append(linha)

matriz[0][0] = "Nossa Senhora de Aparecida"
matriz[0][1] = "Sainte Jeanne D'Arc"
matriz[0][2] = "São Justo Takayama"
matriz[1][0] = "São Francisco de Assis"
matriz[1][1] = "Santo Antônio de Pádua"
matriz[1][2] = "Santa Bárbara"
matriz[2][0] = "Santa Catarina Tekakwitha"
matriz[2][1] = "Santo Elesbão"
matriz[2][2] = "Santo Expedito"

print("--- MATRIZ FORMATADA ---")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]:<30}", end=" | ")
    print()

class Igreja:
    def __init__(self, nome, titulo):
        self.nome = nome
        self.titulo = titulo

    def militante(self):
        print(f"{self.nome} atua sob a fé de {self.titulo}.")

class JeanneDarc(Igreja):
    def __init__(self, nome, titulo):
        super().__init__(nome, titulo)

    def militante(self):
        print(f"{self.nome}, a {self.titulo}, lidera as tropas com a bandeira de Deus!")

class Takayama(Igreja):
    def __init__(self, nome, titulo):
        super().__init__(nome, titulo)

    def militante(self):
        print(f"{self.nome}, o {self.titulo}, renuncia ao feudo por sua fé e luta com a palavra!")

print()
print()

# Criando a lista com as instâncias das classes
santos = [
    JeanneDarc("Jeanne D'arc", "Donzela de Orléans"),
    Takayama("Iustus Takayama", "Samurai de Cristo"),
    Igreja("São Bento", "Abade")
]
for santo in santos:
    santo.militante()
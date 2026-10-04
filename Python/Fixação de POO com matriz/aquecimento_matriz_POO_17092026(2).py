class DominioEn:
    def __init__(self, nen_base):

        self.nen_base = nen_base

        self.grade = [
            [nen_base, nen_base, nen_base],
            [nen_base, nen_base, nen_base],
            [nen_base, nen_base, nen_base]
        ]

    def varredura_en(self,linha,drenagem):
        self.linha = linha
        self.drenagem = drenagem

        for coluna in range(len(self.grade[linha])):
            self.grade[linha][coluna] = self.grade[linha][coluna] - drenagem

            if self.grade[linha][coluna] <= 0:
                self.nen_base = 0

    def mostrar_sala(self):
        for linha in self.grade:
            print(linha)

sala = DominioEn(200)
sala.varredura_en(0, 70)
sala.mostrar_sala()


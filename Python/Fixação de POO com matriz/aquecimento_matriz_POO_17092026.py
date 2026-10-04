class ExameHunter:
    def __init__(self, nen_inicial):
        self.nen_inicial = nen_inicial

        self.grade = [
            [nen_inicial, nen_inicial, nen_inicial],
            [nen_inicial, nen_inicial, nen_inicial],
            [nen_inicial, nen_inicial, nen_inicial]
        ]

    def ataque_ren(self,linha,coluna,dano):
        self.linha = linha
        self.coluna = coluna
        self.dano = dano

        self.grade[linha][coluna] = self.grade[linha][coluna] - dano

        if self.grade[linha][coluna] <= 0:
            self.nen_inicial = 0

    def ver_candidatos(self):
        for linha in self.grade:
            print (linha)

exame = ExameHunter(150)
exame.ataque_ren(1, 1, 80)
exame.ver_candidatos()
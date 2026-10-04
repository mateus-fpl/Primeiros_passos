class PatrulhaPublica:
    def __init__(self, vida_inicial):
        self.vida_inicial = vida_inicial
        self.grade = [
            [vida_inicial, vida_inicial],
            [vida_inicial, vida_inicial]
        ]

    def receber_ataque(self,linha,coluna,dano):
        self.linha = linha
        self.coluna = coluna
        self.dano = dano

        self.grade[linha][coluna] = self.grade[linha][coluna] - dano

        if self.grade[linha][coluna] <= 0:
            self.grade[linha][coluna] = 0

    def status_setor(self):
        for linha in self.grade:
            print (linha)

setor = PatrulhaPublica (100)
setor.receber_ataque(1, 0, 45)
setor.status_setor()
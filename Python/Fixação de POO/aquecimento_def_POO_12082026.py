class Paciente:
    def __init__(self, nome, possui_convenio):
        self.nome = nome
        self.possui_convenio = possui_convenio


class Exames:
    def __init__(self, nome_exame, preco):
        self.nome_exame = nome_exame
        self.preco = preco


class Convenio:
    def __init__(self, nome_plano, porcentagem_cobertura):
        self.nome_plano = nome_plano
        self.porcentagem_cobertura = porcentagem_cobertura


class Atendimento:
    def __init__(self, paciente):
        self.paciente = paciente
        self.exames_realizados = []
        self.convenio = None
        self.total = 0
        self.desconto = 0
        self.valor_final = 0

    def adicionar_exame(self, exame):
        self.exames_realizados.append(exame.preco)

    def calcular_total_bruto(self):
        self.total = sum(self.exames_realizados)
        return self.total

    def aplicar_convenio(self, convenio):
        self.convenio = convenio
        if self.paciente.possui_convenio:
            self.desconto = self.total * convenio.porcentagem_cobertura
            self.valor_final = self.total - self.desconto
        else:
            self.desconto = 0
            self.valor_final = self.total

    def fechar_atendimento(self):
        print(f"Paciente: {self.paciente.nome}")
        print(f"Total dos exames: R$ {self.total:.2f}")
        print(f"A cobertura pelo plano é R$ {self.desconto:.2f}")
        print(f"O valor que o(a) paciente deve pagar é R$ {self.valor_final:.2f}")


# Instanciação e Execução
cliente = Paciente("Mateus", True)
exame = Exames("Checkup completo", 950.0)
conveniado = Convenio("Bradesco Saúde", 0.90)

pagamento = Atendimento(cliente)
pagamento.adicionar_exame(exame)
pagamento.calcular_total_bruto()
pagamento.aplicar_convenio(conveniado)
pagamento.fechar_atendimento()
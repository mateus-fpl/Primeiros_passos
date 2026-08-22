class Cupom:
    def __init__(self, codigo, porcentagem_desconto):
        self.codigo = codigo
        self.porcentagem_desconto = porcentagem_desconto


class Carrinho:
    def __init__(self, usuario, valor_total):
        self.usuario = usuario
        self.valor_total = valor_total

    def aplicar_cupom(self, cupom_alvo):
        desconto = self.valor_total * (cupom_alvo.porcentagem_desconto/100)
        self.valor_total -= desconto
        print(f"Cupom {cupom_alvo.codigo} aplicado! Novo total do carrinho: R$ {self.valor_total:.2f}")


black_friday = Cupom("BLACK20",20)
meu_carrinho = Carrinho("Mateus", 300)
meu_carrinho.aplicar_cupom(black_friday)
class Cliente:
    def __init__(self, nome, eh_membro_clube):
        self.nome = nome
        self.eh_membro_clube = eh_membro_clube


class Produto:
    def __init__(self, item, preco):
        self.item = item
        self.preco = preco


class Cupom:
    def __init__(self, codigo, porcentagem_desconto):
        self.codigo = codigo
        self.porcentagem_desconto = porcentagem_desconto

class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.cupons_aplicados = []

    def adicionar_produto(self,produto_escolhido):
        self.itens.append(produto_escolhido.preco)

    def aplicar_cupom(self,cupom):
        self.cupons_aplicados.append(cupom.porcentagem_desconto)

    def calcular_total_bruto(self):
        return sum(self.itens)

    def fechar_pedido(self):
        valor_total = self.calcular_total_bruto()
        total_cupons = sum(self.cupons_aplicados)
        desconto = valor_total * (total_cupons / 100)
        valor_final = valor_total - desconto

        print(f"Cliente: {self.cliente.nome}")
        print(f"Total Bruto: R$ {valor_total:.2f}")
        print(f"Desconto ({total_cupons}%): R$ {desconto:.2f}")
        print(f"Valor Final a Pagar: R$ {valor_final:.2f}")
        
        return valor_final

cliente1 = Cliente("Mateus","sim")
item = Produto("Air Fryer", 500)

cupom = Cupom ("Casado15", 15)

caixa = Carrinho(cliente1)
caixa.adicionar_produto(item)
caixa.aplicar_cupom(cupom)
caixa.fechar_pedido()
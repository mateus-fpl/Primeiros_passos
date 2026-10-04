# O Desafio: Pergaminho de Invocação — Tabela de Contrato (3x2)Crie uma classe chamada PergaminhoInvocacao que gerencie uma matriz $3 \times 2$, onde cada linha é um sapo e as colunas contêm o nome e o custo de chakra.

# Requisitos da Classe:__init__(self, matriz_invocacoes):Recebe a matriz $3 \times 2$ e salva em self.matriz.Método invocar(self, chakra_disponivel):Recebe a quantidade de chakra_disponivel.Percorre a matriz linha por linha (usando for linha in self.matriz: ou range).Para cada linha, acessa o nome (linha[0]) e o custo (linha[1]).Compara o chakra_disponivel com o custo:Se for maior ou igual: imprime "Invocado: [Nome]!"Caso contrário: imprime "Chakra insuficiente para invocar [Nome]."

# dados = [
#     ["Gamakichi", 50],
#     ["Gamaken", 120],
#     ["Gamabunta", 300]
# ]

# pergaminho = PergaminhoInvocacao(dados)

# # Naruto tenta invocar usando 150 de Chakra
# pergaminho.invocar(150)
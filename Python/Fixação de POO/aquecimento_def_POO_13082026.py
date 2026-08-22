# 1. Classe Veiculo

# Atributos no __init__: placa (texto) e tipo (texto, ex: "carro" ou "moto").

# 2. Classe TabelaPreco

# Atributos no __init__: valor_hora (número) e taxa_desconto_moto (número decimal, ex: 0.20 para 20% de desconto).

# 3. Classe Estadia

# Atributos no __init__: recebe um objeto veiculo e inicializa horas_estacionado = 0, total_bruto = 0, desconto = 0 e valor_final = 0.

# Método registrar_horas(self, horas): define a quantidade de horas que o veículo ficou.

# Método calcular_cobranca(self, tabela):

# Recebe o objeto tabela (instância de TabelaPreco).

# Calcula o total_bruto multiplicando as horas pelo tabela.valor_hora.

# Regra de Negócio: Se o self.veiculo.tipo == "moto", calcula o desconto usando tabela.taxa_desconto_moto e subtrai do total. Se for carro, o desconto é zero e o valor final é o total bruto.

# Método emitir_recibo(self):

# Exibe na tela:

# Placa do veículo

# Tipo do veículo

# Tempo permanecido (horas)

# Valor total bruto

# Desconto aplicado

# Valor final a pagar

# Dados de teste para validar o fluxo:

# Caso 1 (Carro): Placa "ABC-1234", tipo "carro", 3 horas. Valor hora: R$ 15.00. (Deve pagar: R$ 45.00, desconto: R$ 0.00).

# Caso 2 (Moto): Placa "XYZ-9876", tipo "moto", 2 horas. Valor hora: R$ 15.00, desconto moto: 0.20. (Bruto: R$ 30.00, desconto: R$ 6.00, final: R$ 24.00).
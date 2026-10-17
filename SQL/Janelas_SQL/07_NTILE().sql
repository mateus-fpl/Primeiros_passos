-- Dividir os dados em quartis, permitindo classificar, segmentar ou dividir valores por faixas.alter
-- Criar 4 grupos de clientes com rena semelhante. Cada cliente deve ser classificado em uma "faixa de renda" (mais alto para o mais baixo)

select * from clientes;

select
	ID_Cliente,
    Nome,
    Renda_Anual,
    ntile(4) over (order by Renda_Anual desc) as faixa_renda
from clientes;
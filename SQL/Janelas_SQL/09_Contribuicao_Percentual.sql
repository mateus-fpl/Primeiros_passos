-- Identificar os principais produtos ou clientes responsáveis pela receitas

select
	date_format(data_venda,'%Y-%m') as mes,
    sum(qtd_vendida) as total_vendidos_mes,
    sum(qtd_vendida)/sum(sum(Qtd_Vendida)) over () as total_geral
from vendas
group by date_format(data_venda,'%Y-%m');
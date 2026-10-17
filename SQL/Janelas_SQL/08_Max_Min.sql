-- Determinar os valores máximos e mínimos em janelas específicas
-- Obter o maior valor de vendas dentro de um grupo de 3 meses consecutivos.

select * from vendas;

select
	date_format(data_venda, '%Y-%m') as mes,
    sum(qtd_vendida) as total_vendido_mes,
    sum(sum(qtd_vendida)) over(order by date_format(data_venda, '%Y-%m') rows between 2 preceding and current row) as max_vendas_3_meses
from vendas
group by date_format(data_venda,'%Y-%m')
order by
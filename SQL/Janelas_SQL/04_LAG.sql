-- Comparação de valores com LAG()

-- Exemplo prático Comparar as vendas de um mês cpom o mês anterior (ou próximo)

select * from vendas;

select
	date_format(data_venda, '%Y-%m') as mes,
    sum(qtd_vendida) as total_vendido_mes
from vendas
group by date_format(data_venda, '%Y-%m')
order by mes;

with vendas_mensais as (

select
	date_format(data_venda, '%Y-%m') as mes,
    sum(qtd_vendida) as total_vendido_mes
from vendas
group by date_format(data_venda, '%Y-%m')
order by mes
)

select mes, total_vendidos_mes, lag(total_vendido_mes) 
	over (order by mes) as vendas_mes_anterior
from vendas_mensais order by mes;

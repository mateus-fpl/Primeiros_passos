-- Calcule a soma acumulada da quantidade de vendas ao longo do tempo

select * from vendas;

with vendas_normais as (
select
   date_format(data_venda,'%Y-%m') as mes,
   sum(qtd_vendida) as total_vendido_mes
from vendas
group by date_format(data_venda, '%Y-%m')
order by mes
)

select 
	mes,
    total_venvido_mes,
    sum(total_vendido_mes) over (order by mes) as acumulado
from vendas_mensais
order by mes
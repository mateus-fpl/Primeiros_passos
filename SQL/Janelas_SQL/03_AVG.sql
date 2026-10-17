-- Aplicação: Analisar tendências em séries temporais, como vendas nos preços
-- Exemplo prático: Calcule a média manual da receita de vendas dos últimos 3 meses

select * from vendas;

select
	date_format(data_vendas,'%Y-%m') as mes,
    sum(receita_venda) as total_receita_mes,
    avg(sum(receita_venda)) over(order by date_format(data_vendas,'%Y-%m') rows between 2 preceding and
current row) as media_movel_3_meses
from
	vendas
group by data_format(data_vendas,'%Y-%m')
order by mes;
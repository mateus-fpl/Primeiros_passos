-- Aplicação : Criar rankings de registros ordenados, como em competições ou resultados de vendas.
-- Exemplo prático: Ordenar os clientes de acordo com a Renda_Anual, identificando empates corretamente

select * from clientes order by renda_anual;

select
	nome, email, renda_anual,
    dense_rank() over(order by renda_anual desc) as posicao
from clientes;
    
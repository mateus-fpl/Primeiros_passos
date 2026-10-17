-- Aula 2. Encontrando o N-ésimo maior valor com ROW_NUMBER()

-- Aplicação: Identificar a linha ou registro em uma ordem específica.
-- Exemplo prático: Encontrar o segundo maior salário da base de clientes.

select * from clientes;

select
	nome,email,renda_anual,
    row_number() over(order by renda_anual desc) as posicao
from clientes where posicao = 2;

-- Como resolver: Para filtrar os resultados de funções de janela, como ROW_NUMBER(), você precisa usar uma subquery.

select * from (

	select
		nome,email,renda_anual,
		row_number() over(order by renda_anual desc) as posicao
	from clientes
) as resultado 
where posicao = 2;
-- COUNT, COUNT(*), COUNT (DISTINCT)

select * from clientes;
select 
	count(nome)
from clientes;

select 
	count(Telefone)
from clientes;

select 
	count(*)
from clientes;

select
	count(distinct Escolaridade)
from clientes;

-- SUM, AVG, MIN, MAX

select
	sum(Receita_Venda) as 'Soma de Receita',
    avg(Receita_Venda) as 'Media de Receita',
    min(Receita_Venda) as 'Menor Receita',
    max(Receita_Venda) as 'Maior Receita'
from pedidos;
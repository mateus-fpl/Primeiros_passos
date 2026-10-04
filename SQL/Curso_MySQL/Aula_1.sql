-- Exemplo 1. Selecionando todas as linhas e colunas da:
-- a) tabela pedidos
SELECT * FROM categorias;

-- b) tabela clientes
select * from clientes;

select * from locais;
select * from lojas;
select * from pedidos;
select * from produtos;

-- Exemplo 2. Selecionar apenas algumas colunas da tabela clientes

select 
	ID_Cliente as 'ID Cliente', 
	Nome as 'Nome do Cliente', 
	Data_Nascimento as 'Data de Nascimento', 
	Email as 'Email do Cliente'
from clientes;

-- Exemplo3. Selecionar apenas as 5 primeiras linhas da tabeça de produtos

select * from produtos
limit 5;

-- Exemplo 4. Selecionar todas as linhas da tabela produto, MAS...
-- ordenando pela coluna Preco_Unit

select * from produtos
order by Preco_Unit desc;
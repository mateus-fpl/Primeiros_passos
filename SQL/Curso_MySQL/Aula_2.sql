-- Aula 2: Criando Filtros no SQL.

select ID_Produto, Nome_Produto,Preco_Unit from produtos;

-- Exemplo1. Mostre apenas os produtos com preços iguais ou maiores a R$ 1.800,00

select * 
from produtos
where Preco_Unit >= 1800;

-- Exemplo 2. Mostre apenas or produtos com preços iguais a R$ 3.1000.

select *
from produtos
where Preco_Unit = 3100;

-- Exemplo 3. Mostre apenas os produtos com a marca Dell.

select * 
from produtos
where Marca_Produto = 'Dell';

-- Exemplo 4. Mostre apenas os pedidos feito no dia 03/01/2019

select *
from pedidos
where Data_Venda = '2019-01-03';

-- Exemplo 5. Mostre apenas os clientes SOLTEIROS e do sexo MASCULINO

select *
from clientes
where Estado_Civil = 'S' and Sexo ='M';

-- Exemplo 6.Mostre apenas os produtos da marcas DELL ou SAMSUNG
select *
from produtos
where Marca_Produto = 'Dell' or Marca_Produto = 'Samsung';




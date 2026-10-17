select * from pokemon;

select count(*) from pokemon;

select
	tipo1 as '1º_Tipo',
    tipo2 as '2º_Tipo',
    AtaqueEspecial as 'Ataque_Especial',
    DefesaEspecial as 'Defesa_Especial'
from pokemon;

select Nome, Tipo1, Ataque from pokemon where Tipo1 = 'Fire' and Ataque >= 100 order by Ataque asc;

select Tipo1, count(Nome) as 'Total de Cada Tipo' from pokemon group by Tipo1;

select Nome as 'Os Pokemons mais rápidos', Velocidade from pokemon order by Velocidade desc limit 5;

select Geração, avg(Total) as 'Média dos Status' from pokemon group by Geração order by Geração desc;

select Nome, Tipo1, HP from pokemon where Lenda = 'True' and HP < 100;

select Nome, Tipo1 from pokemon where Nome LIKE 'Mega%';

select Tipo1, avg(Ataque) as 'Média de ataque maior que 80' from pokemon group by Tipo1 having avg(Ataque) > 80 ;

select max(Defesa), min(Defesa) from pokemon where Tipo1 = 'Steel' or Tipo2 = 'Steel';

select Geração, count(Geração) as 'Geração com mais lendas' from pokemon where Lenda = 'True' group by Geração order by count(Geração) desc;


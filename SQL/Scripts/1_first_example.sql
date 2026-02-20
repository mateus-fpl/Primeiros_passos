show databases;
create database if not exists first_example;
use first_example;
CREATE table person(
	person_id smallint unsigned,
	fname varchar(20),
	lname varchar(20),
	gender enum('M','F'),
	birth_date DATE,
	street varchar(20),
	city varchar(20),
	state varchar(20),
	country varchar(20),
	postal_code varchar(20),
    constraint pk_person primary key (person_id)
    );
    
    
create table favorite_food(
	person_id smallint unsigned,
	food varchar(20),
	constraint pk_favorite_food primary key (person_id, food),
	constraint fk_favorite_food_person_id foreign key (person_id) 
	references person(person_id)
    );    
    
desc favorite_food;
show databases;
desc information_schema.table_constraints;
select * from information_schema.table_constraints
where constraint_schema = 'first_example';

insert into person values ('4','Carolina','Silva','F','1979-08-21',
							'rua tal', 'Cidade J', 'RJ','Brasil','265021-023')
                            ,('5','Luis','Gustavo','F','1979-08-21',
							'rua tal', 'Cidade J', 'RJ','Brasil','265021-023');
select * from person;

delete from person where person_id = 2 or person_id = 3 or person_id = 4 ;

desc favorite_food;
desc person;
insert into favorite_food values (0,'lasanha'),
								 (1, 'carne assada'),
                                 (5, 'fetuccine');
select * from favorite_food;

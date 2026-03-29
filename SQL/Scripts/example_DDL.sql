-- explorando DDL --

select now() as Timestamp;
create database if not exists manipulation;
use manipulation;

create table bankAccounts (
	Id_account int auto_increment primary key,
    Ag_num int not null,
    Ac_num int not null,
    Saldo float,
    constraint identification_account_constraint unique (Ag_num, Ac_num)
);

-- Tô inserindo um cliente pra mexer na tabela lá de baixo --
insert into bankAccounts (Ag_num, Ac_num, Saldo) values(156,264358,0);
select * from bankAccounts;

alter table bankAccounts add LimiteCredito float not null default 500.00;

-- Esse vai ser um teste pra eu remover em seguida --
alter table bankAccounts add email varchar(60);
alter table bankAccounts drop column email;

desc bankAccounts;

create table bankClient (
	Id_client int auto_increment,
	ClientAccount int,
    CPF char(11) not null,
    RG char(9) not null,
    Nome varchar(50) not null,
    Endereço varchar(100) not null,
    Renda_mensal float,
    primary key (Id_Client,ClientAccount),
    constraint fk_account_client foreign key (ClientAccount) references bankAccounts (Id_account)
    on update cascade
);

insert into bankClient (ClientAccount, CPF, RG, Nome, Endereço, Renda_mensal) values(1,12345678911,'123456789','Fulano','rua de lá',6500.6);
select * from bankClient;
alter table bankClient add UF char(2) not null default 'RJ';

create table bankTransactions(
	Id_transation int auto_increment primary key,
	Ocorrência datetime,
	Status_transaction varchar(20),
	Valor_transferido float,
    Source_account int,
    Destination_account int,
    constraint fk_source_transaction foreign key (Source_account) references
    bankAccounts(id_Account),
    constraint fk_destination_transaction foreign key (destination_account) references
    bankAccounts(Id_Account)
);

show tables;


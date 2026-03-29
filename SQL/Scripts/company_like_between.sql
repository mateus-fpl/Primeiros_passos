use company_constraints;

select * from dept_locations;

-- O caracter de % é um coringa que busca qualquer coisa que termine em Houston(exemplo) não importando o tanto de caracteres
-- que vieram antes da palavra de busca
select concat(Fname, ' ',Lname) as Complete_Name, Dname as Department_Name from employee, departament
	where (Dno=Dnumber and Address like 'Houston%');
 
 -- between é uma maneira mais enxuta de fazer entre coluna > and coluna < --
select Fname, Lname from employee where (Salary > 30000 and Salary < 40000);
select Fname, Lname from employee where (Salary between 20000 and 40000);

-- operadores lógicos --
-- and --
select Bdate, Address from employee where Fname='John' and Minit='B' and Lname='Smith';
-- or --
select * from departament where Dname= 'Research' or Dname = 'Administration';
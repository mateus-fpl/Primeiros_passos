use company_constraints;

select Fname, Lname from employee, departament where Dname = 'Reserach' and Dnumber=Dno;
select concat(Fname, Lname) as Complete_name from employee, departament where Dname = 'Research' and Dnumber=Dno;

-- Aqui eu tô calculando o desconto para INSS em cima do salário do cabra --

select Fname, Lname, Salary, Salary*0.011 from employee;
select Fname, Lname, Salary, Salary*0.011 as INSS from employee;
-- Aqui tô colocando a quantidae casas decimais --
select Fname, Lname, Salary, round(Salary*0.011,2) as INSS from employee;

-- definir um aumento de salário para os gerentes que trabalham no projeto associado ao produto X--
desc project;
desc works_on;
select * from employee e, works_on as w, project as p where (e.Ssn = w.Essn and w.Pno=p.Pnumber and p.Pname = 'ProductX');
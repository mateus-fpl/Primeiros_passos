use company_constraints;

-- Expressões e concatenação de strings --

-- recuperando informação dos departamentos presentes em Stanfford
desc dept_locations;
select * from dept_locations;

-- recuperando informçãoes dos departamentos presentes em Stafford --

select Dname as Department_Name, Mgr_ssn as Manager, Address from departament d, dept_locations l, employee e
	where d.DNumber = l.Dnumber and Dlocation='Stafford' and Mgr_ssn = e.Ssn;
 
 -- recuperando todos os gerentes que trabalham em Stafford --
select Dname as Department_Name, concat(Fname,' ', Lname) as Manager from departament d, dept_locations l, employee e
	where d.DNumber = l.Dnumber and Mgr_ssn = e.Ssn;
    
 -- recuperando todos os gerentes e seus nomes --
select Dname as Department_Name, concat(Fname,' ', Lname) as Manager, Dlocation from departament d, dept_locations l, employee e
	where d.DNumber = l.Dnumber and Mgr_ssn = e.Ssn;
use company_constraints;

-- Cláusulas com exites e unique

-- Quais employees possuem dependentes?
select e.Fname, e.Lname from employee as e
where exists (select * from dependent as d where e.Ssn = d.Essn and Relationship = 'Son'); 




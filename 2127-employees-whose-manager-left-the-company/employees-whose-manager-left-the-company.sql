# Write your MySQL query statement below
Select employee_id
from employees
where salary < 30000 
and manager_id not in (Select employee_id from employees)
order by employee_id


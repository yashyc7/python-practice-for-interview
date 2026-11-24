"""
Problem statement

Given an employees table, find the second highest salary.

Sample table:

id	name	salary
1	Asha	50000
2	Ravi	70000
3	Meena	70000
4	Kiran	40000
"""


select max(SALARY) as second_highest
FROM employees 
where salary < (select MAX(SALARY) FROM employees)
# Write your MySQL query statement below
SELECT e1.name AS EMPLOYEE FROM EMPLOYEE e1 LEFT JOIN EMPLOYEE e2 ON e1.managerId = e2.Id WHERE e1.salary > e2.salary;
# Write your MySQL query statement below
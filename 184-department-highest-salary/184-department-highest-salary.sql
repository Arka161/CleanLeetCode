# Write your MySQL query statement below
WITH CTE AS (
    SELECT *, DENSE_RANK() OVER(PARTITION BY DEPARTMENTID ORDER BY SALARY DESC) AS SALARY_RANK FROM EMPLOYEE
)

SELECT d.name as Department, e.name as Employee, e.salary as salary FROM CTE e JOIN DEPARTMENT d ON d.id = e.departmentId WHERE SALARY_RANK = 1;




# Write your MySQL query statement below
SELECT Id, CASE

WHEN P_ID is NULL THEN "Root"
WHEN P_ID is not NULL AND ID IN (SELECT P_ID FROM TREE) THEN "Inner" 
ELSE "Leaf" 
END AS TYPE

FROM TREE
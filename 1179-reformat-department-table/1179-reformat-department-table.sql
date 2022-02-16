SELECT id,
SUM(CASE WHEN month = 'Jan' THEN revenue END) AS Jan_Revenue,
MIN(CASE WHEN month = 'Feb' THEN revenue END) AS Feb_Revenue,
MIN(CASE WHEN month = 'Mar' THEN revenue END) AS Mar_Revenue,
MIN(CASE WHEN month = 'Apr' THEN revenue END) AS Apr_Revenue,
MIN(CASE WHEN month = 'May' THEN revenue END) AS May_Revenue,
MIN(CASE WHEN month = 'Jun' THEN revenue END) AS Jun_Revenue,
MIN(CASE WHEN month = 'Jul' THEN revenue END) AS Jul_Revenue,
MIN(CASE WHEN month = 'Aug' THEN revenue END) AS Aug_Revenue,
MIN(CASE WHEN month = 'Sep' THEN revenue END) AS Sep_Revenue,
MIN(CASE WHEN month = 'Oct' THEN revenue END) AS Oct_Revenue,
MIN(CASE WHEN month = 'Nov' THEN revenue END) AS Nov_Revenue,
MIN(CASE WHEN month = 'Dec' THEN revenue END) AS Dec_Revenue

FROM Department
GROUP BY Id ORDER BY ID
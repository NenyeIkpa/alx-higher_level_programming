-- displays the average temperature (Fahrenheit) by city
-- of top 3 cities with highest temp in july and august 
-- ordered by temperature (descending)
USE hbtn_0c_0;
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE MONTH = 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
